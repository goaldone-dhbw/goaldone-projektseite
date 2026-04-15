# Planungsalgorithmus – Technische Dokumentation

Diese Seite beschreibt den Planungsalgorithmus von Goaldone, der dynamische Aufgaben automatisch auf die verfügbaren Arbeitszeiten der Nutzer verteilt. Der Algorithmus arbeitet pro Arbeitgeber-Account isoliert; Arbeitszeiten zwischen Accounts werden bereits beim Anlegen validiert, um Überschneidungen zu vermeiden.

---

## Goaldone Planungsalgorithmus: Gesamtüberblick

Das Diagramm zeigt den vollständigen Ablauf des Planungsalgorithmus von der API-Anfrage bis zur gespeicherten Lösung. Der Algorithmus folgt einem dreistufigen Ansatz:

1.  **Phase 1 (Datenaufbereitung):** Laden und Validieren von Arbeitszeiten, Blockern und Tasks.
2.  **Phase 2 (Konstruktionsheuristik):** Erzeugung einer ersten Lösung mittels einer CPM-basierten (Critical Path Method) Heuristik.
3.  **Phase 3 (Lokale Suche):** Iterative Verbesserung der Erstlösung durch eine Metaheuristik (Late Acceptance Hill Climbing + Tabu Search).

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/01.png" alt="Goaldone Planungsalgorithmus" />

</details>

---

## Phase 1: Datenaufbereitung & Vorvalidierung

In dieser Phase werden die Eingabedaten für den Solver materialisiert und validiert:

*   **Arbeitszeiten & Blocker:** Reguläre Arbeitszeiten werden für den Planungshorizont (heute + N Tage) in konkrete Tages-Zeitfenster umgerechnet. Fixe Blocker (Termine, Pausen) und wiederkehrende Termine (RRule-Format inkl. Ausnahmen) werden materialisiert. Die Differenz ergibt die freien **TimeSlots**.
*   **Task-Pool:** Alle offenen Aufgaben (OPEN, IN_PROGRESS) werden geladen. Der Abhängigkeitsgraph wird mittels topologischer Sortierung auf Zyklen geprüft.
*   **Logische Prüfung:** Aufgaben mit Deadlines in der Vergangenheit oder logischen Konflikten (z. B. "Nicht planen vor"-Datum liegt nach der Deadline) werden abgefangen und führen zu Fehlermeldungen.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/02.png" alt="Datenaufbereitung" />

</details>

---

## Chunking-Logik (Aufgabenzerlegung)

Um eine flexible Planung zu ermöglichen, werden Aufgaben in Arbeitsblöcke (**Chunks**) unterteilt. Die maximale Chunk-Dauer richtet sich nach der kognitiven Last:

-   **HIGH:** max. 2 Stunden
-   **MODERATE:** max. 4 Stunden
-   **LOW:** max. 8 Stunden

Nutzer können diese Werte pro Aufgabe durch eine manuell festgelegte Chunk-Größe überschreiben; diese Chunks werden dann als nicht weiter unterteilbar behandelt. Der letzte Chunk einer Aufgabe erhält die verbleibende Restdauer. Nach jedem Chunk wird eine 10-minütige Pause reserviert, sofern ein weiterer Chunk folgt.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/06.png" alt="Chunking" />

</details>

---

## Phase 2: Konstruktionsheuristik (Erstlösung)

Die Erstlösung wird durch eine Greedy-Heuristik erzeugt, deren Priorisierung auf dem **vollständigen Critical Path Method (CPM) Algorithmus** mit minutengenauer Slack-Berechnung beruht.

**CPM-Algorithmus (ES, EF, LS, LF):**
Der vollständige CPM-Algorithmus wird angewendet:

- **Forward Pass:** Berechnung der Early Start (ES) und Early Finish (EF) für jede Aufgabe basierend auf Abhängigkeiten
- **Backward Pass:** Berechnung der Late Start (LS) und Late Finish (LF) ausgehend von den Deadlines
- **Slack-Berechnung:** Der Slack für jede Aufgabe ergibt sich aus (LS - ES) bzw. (LF - EF) und wird zur Priorisierung genutzt

Chunks werden sortiert nach:

1.  Topologische Ebene der Abhängigkeiten
2.  "Nicht planen vor"-Datum
3.  Slack-Wert (aufsteigend)
4.  Kognitive Last (HIGH vor MODERATE vor LOW)

Anschließend wird jeder Chunk dem frühesten passenden freien Slot zugewiesen. Bereits gepinnte Chunks bleiben dabei fixiert.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/14.png" alt="Heuristik" />

</details>

---

## Phase 3: Lokale Suche (Iterative Verbesserung)

Die Erstlösung wird durch eine Metaheuristik iterativ verbessert, bis ein Zeitlimit (z. B. 2 Sekunden) erreicht ist. Dabei werden zufällige Änderungen (**Moves**) vorgenommen und deren Auswirkung auf einen lexikographisch geordneten **HardSoftScore** bewertet.

*   **Hard-Constraints:** Dürfen nie verletzt werden (Zeitüberlappungen, Abhängigkeitsreihenfolge, "Nicht vor"-Datum, Account-Zuordnung).
*   **Soft-Constraints:** Optimieren Slack-Priorisierung, Pausen-Verschmelzung und Chunk-Kompaktheit.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/10.png" alt="Solver Overview" />

</details>

---

### Move-Strategien

Drei Typen von Moves werden eingesetzt, um den Lösungsraum zu explorieren:

*   **ChangeMove (~50%):** Ein Chunk wird in einen anderen freien Slot verschoben.
*   **SwapMove (~30%):** Zwei Chunks tauschen ihre jeweiligen Slots.
*   **PillarMove (~20%):** Alle Chunks einer Aufgabe werden gemeinsam verschoben, um die Kompaktheit zu wahren.

Gepinnte Chunks (manuelle Verschiebung) sind von allen Moves ausgeschlossen.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/12.png" alt="Moves" />

</details>

---

### Akzeptanzkriterien (Late Acceptance + Tabu Search)

Um lokale Optima zu verlassen, nutzt der Solver zwei Mechanismen:

*   **Late Acceptance Hill Climbing (LAHC):** Ein Move wird akzeptiert, wenn er die aktuelle Lösung verbessert oder besser ist als die Lösung von vor $L=400$ Iterationen.
*   **Tabu Search:** Eine Tabu-Liste (Größe 7) verhindert das unmittelbare Zurückspringen in vorherige Zustände. Ein Aspiration-Kriterium erlaubt die Aufhebung eines Tabus, wenn der Move den globalen Bestwert übertrifft.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/13.png" alt="Acceptance" />

</details>

---

## Konflikterkennung und Nutzer-Feedback

Kann der Solver keine gültige Lösung finden (Hard-Score < 0) oder müssen Deadlines verletzt werden, erfolgt ein Feedback an den Nutzer.