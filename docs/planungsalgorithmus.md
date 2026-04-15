# Modell für Planungsalgorithmus

## Goaldone Planungsalgorithmus: Gesamtüberblick (Helicopter-Ansicht)

Das Diagramm zeigt den vollständigen Ablauf des Planungsalgorithmus von der API-Anfrage bis zur gespeicherten Lösung. Nach dem Eingang eines Schedule-Requests werden zunächst alle relevanten Daten geladen (Arbeitszeiten, Termine, Tasks), dann validiert und in Chunks aufgeteilt. Anschließend durchläuft der CustomSolver zwei Phasen: eine Konstruktionsheuristik zur Erstellung einer Erstlösung und eine lokale Suche zur iterativen Verbesserung. Je nach Score-Ergebnis wird entweder ein vollständiger Plan persistiert oder – bei verletzten Constraints – eine Konfliktauflösung mit Nutzerfeedback eingeleitet.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/01.png" alt="Goaldone Planungsalgorithmus" />

</details>

---

## Datenaufbereitung & Vorvalidierung

Dieses Diagramm beschreibt die Schritte, die vor der eigentlichen Optimierung stattfinden. Es zeigt, wie Arbeitszeiten und fixe Termine (inkl. wiederkehrender Termine per RRule) geladen und zu freien Zeitfenstern (TimeSlots) verrechnet werden. Parallel dazu wird der Task-Pool aufgebaut, ein Abhängigkeitsgraph erstellt und auf zirkuläre Abhängigkeiten geprüft. Abschließend werden Deadlines vorab gegen die verfügbare Arbeitszeit geprüft – Tasks mit unlösbaren Deadlines werden mit einer Warnung markiert, aber trotzdem an den Solver übergeben.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/02.png" alt="Datenaufbereitung" />

</details>

---

## Chunking-Logik (Aufgabenzerlegung)

Dieses Diagramm erklärt, wie eine Aufgabe vor der Übergabe an den Solver in zeitliche Teilstücke (Chunks) zerlegt wird. Die Chunk-Größe hängt von der kognitiven Last ab. Nach jedem Chunk wird eine Pause als Soft-Constraint berücksichtigt.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/06.png" alt="Chunking" />

</details>

---

## Eigenbau-Solver: Gesamtüberblick

Ein Überblick über die zwei zentralen Phasen: Konstruktionsheuristik und lokale Suche. Der Solver verbessert iterativ die Lösung.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/10.png" alt="Solver Overview" />

</details>

---

## Move-Strategien (Nachbarschaftssuche)

Dieses Diagramm erklärt die drei Move-Typen: Change, Swap und Pillar Move.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/12.png" alt="Moves" />

</details>

---

## Akzeptanzkriterien (Late Acceptance + Tabu Search)

Das Diagramm zeigt, wann ein Move akzeptiert oder abgelehnt wird.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/13.png" alt="Acceptance" />

</details>

---

## Konstruktionsheuristik (Erstlösung)

Das Diagramm beschreibt, wie die erste gültige Lösung erzeugt wird.

<details>
<summary><strong>Diagramm anzeigen</strong></summary>

<img src="../assets/algorithmus/14.png" alt="Heuristik" />

</details>