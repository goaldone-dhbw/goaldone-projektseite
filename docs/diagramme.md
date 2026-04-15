# Diagramme

<details>
<summary><strong> Goaldone Planungsalgorithmus: Gesamtüberblick (Helicopter-Ansicht)</strong></summary>

<br>

Das Diagramm zeigt den vollständigen Ablauf des Planungsalgorithmus von der API-Anfrage bis zur gespeicherten Lösung. Nach dem Eingang eines Schedule-Requests werden zunächst alle relevanten Daten geladen (Arbeitszeiten, Termine, Tasks), dann validiert und in Chunks aufgeteilt. Anschließend durchläuft der CustomSolver zwei Phasen: eine Konstruktionsheuristik zur Erstellung einer Erstlösung und eine lokale Suche zur iterativen Verbesserung. Je nach Score-Ergebnis wird entweder ein vollständiger Plan persistiert oder – bei verletzten Constraints – eine Konfliktauflösung mit Nutzerfeedback eingeleitet.

![Goaldone Planungsalgorithmus](assets/diagramme/01.png)

</details>

---

<details>
<summary><strong> Datenaufbereitung & Vorvalidierung</strong></summary>

<br>

Dieses Diagramm beschreibt die Schritte, die vor der eigentlichen Optimierung stattfinden. Es zeigt, wie Arbeitszeiten und fixe Termine (inkl. wiederkehrender Termine per RRule) geladen und zu freien Zeitfenstern (TimeSlots) verrechnet werden. Parallel dazu wird der Task-Pool aufgebaut, ein Abhängigkeitsgraph erstellt und auf zirkuläre Abhängigkeiten geprüft. Abschließend werden Deadlines vorab gegen die verfügbare Arbeitszeit geprüft – Tasks mit unlösbaren Deadlines werden mit einer Warnung markiert, aber trotzdem an den Solver übergeben.

![Datenaufbereitung](assets/diagramme/02.png)

</details>

---

<details>
<summary><strong> Domänenmodell (Custom Solver, Plain Java)</strong></summary>

<br>

Das Klassendiagramm stellt das interne Datenmodell des selbst entwickelten Solvers vor. Zentrale Klassen sind TaskSchedule (die gesamte Lösung), TaskAssignment (ein eingeplanter Aufgaben-Chunk), TimeSlot (ein freies Zeitfenster), Task (die eigentliche Aufgabe) und HardMediumSoftScore (die dreigliedrige Bewertungsstruktur). Zusätzlich sind die drei Move-Typen (ChangeMove, SwapMove, PillarMove) als Interface-Implementierungen abgebildet. Ein zentraler Unterschied zum Framework-Ansatz: Pinning und Account-Validierung müssen in jeder Move-Klasse manuell implementiert werden.

![Domänenmodell](assets/diagramme/03.png)

</details>

---

<details>
<summary><strong> Constraint-Evaluation (ScoreCalculator)</strong></summary>

<br>

Dieses Aktivitätsdiagramm zeigt den Ablauf der imperativen Score-Berechnung. Der Calculator iteriert über alle zugewiesenen Chunks und prüft sequenziell sämtliche Hard-, Medium- und Soft-Constraints (H1–H6, M1–M3, S1–S4). Hard-Constraints schließen Zeitüberlappungen, Kapazitätsüberschreitungen, Abhängigkeitsverletzungen und Reihenfolge-Fehler ein. Medium-Constraints betreffen Deadlines und nicht eingeplante Chunks. Soft-Constraints optimieren Dringlichkeit, Pausen und Kompaktheit. Am Ende wird ein HardMediumSoftScore-Objekt zurückgegeben, das lexikographisch verglichen wird.

![Constraint Evaluation](assets/diagramme/04.png)

</details>

---

<details>
<summary><strong> Constraint-Übersicht</strong></summary>

<br>

Eine strukturierte Referenz-Übersicht über alle Constraints des Systems, aufgeteilt in drei Kategorien. Die Hard-Constraints (H1–H6) dürfen nie verletzt werden. Medium-Constraints erlauben suboptimale Lösungen. Soft-Constraints optimieren die Qualität des Plans.

![Constraint Übersicht](assets/diagramme/04b.png)

</details>

---

<details>
<summary><strong> Solver-Ausführung im SchedulerService</strong></summary>

<br>

Das Diagramm zeigt den vollständigen Ausführungsablauf des Solvers aus Sicht des SchedulerService. Nach dem Aufbau der TaskSchedule wird der Solver gestartet. Phase 1 erzeugt eine Erstlösung, Phase 2 verbessert diese iterativ. Nach Ablauf des Zeitlimits wird der beste Plan analysiert und persistiert.

![Solver Ablauf](assets/diagramme/05.png)

</details>

---

<details>
<summary><strong> Chunking-Logik (Aufgabenzerlegung)</strong></summary>

<br>

Dieses Diagramm erklärt, wie eine Aufgabe vor der Übergabe an den Solver in zeitliche Teilstücke (Chunks) zerlegt wird. Die Chunk-Größe hängt von der kognitiven Last ab. Nach jedem Chunk wird eine Pause als Soft-Constraint berücksichtigt.

![Chunking](assets/diagramme/06.png)

</details>

---

<details>
<summary><strong> Multi-Account Scheduling</strong></summary>

<br>

Das Diagramm beschreibt, wie das System mit mehreren Accounts umgeht. Solver-Läufe können sequenziell oder parallel erfolgen. Die Ergebnisse werden anschließend zusammengeführt.

![Multi Account](assets/diagramme/07.png)

</details>

---

<details>
<summary><strong> Konflikterkennung & Relaxierung</strong></summary>

<br>

Dieses Diagramm zeigt, was passiert, wenn keine vollständig gültige Lösung gefunden wird. Constraint-Verletzungen werden analysiert und dem Nutzer konkrete Lösungsvorschläge gegeben.

![Konflikte](assets/diagramme/08.png)

</details>

---

<details>
<summary><strong> Aufgabe verschieben & Pinning</strong></summary>

<br>

Dieses Diagramm beschreibt den Workflow beim manuellen Verschieben eines Tasks. Gepinnte Chunks werden vom Solver nicht mehr verändert.

![Pinning](assets/diagramme/09.png)

</details>

---

<details>
<summary><strong> Eigenbau-Solver: Gesamtüberblick</strong></summary>

<br>

Ein Überblick über die zwei zentralen Phasen: Konstruktionsheuristik und lokale Suche. Der Solver verbessert iterativ die Lösung.

![Solver Overview](assets/diagramme/10.png)

</details>

---

<details>
<summary><strong> Score-Berechnung (HardMediumSoftScore)</strong></summary>

<br>

Das Diagramm zeigt die dreistufige Score-Berechnung. Hard-Constraints haben höchste Priorität.

![Score](assets/diagramme/11.png)

</details>

---

<details>
<summary><strong> Move-Strategien (Nachbarschaftssuche)</strong></summary>

<br>

Dieses Diagramm erklärt die drei Move-Typen: Change, Swap und Pillar Move.

![Moves](assets/diagramme/12.png)

</details>

---

<details>
<summary><strong> Akzeptanzkriterien (Late Acceptance + Tabu Search)</strong></summary>

<br>

Das Diagramm zeigt, wann ein Move akzeptiert oder abgelehnt wird.

![Acceptance](assets/diagramme/13.png)

</details>

---

<details>
<summary><strong> Konstruktionsheuristik (Erstlösung)</strong></summary>

<br>

Das Diagramm beschreibt, wie die erste gültige Lösung erzeugt wird.

![Heuristik](assets/diagramme/14.png)

</details>

---

<details>
<summary><strong> Vergleich: Timefold AI vs. Eigenbau-Solver</strong></summary>

<br>

Vergleich zwischen Framework und Eigenbau hinsichtlich Aufwand und Funktionalität.

![Vergleich](assets/diagramme/15.png)

</details>