# Kalender und Planung

Der Kalender ist das zentrale Herzstück von GoalDone. Hier laufen alle Fäden zusammen: Ihre Arbeitszeiten, Ihre festen Termine und Ihre Aufgaben werden automatisch zu einem optimalen Zeitplan kombiniert.

## Der automatische Planer
Das Besondere an GoalDone ist, dass Sie Ihren Zeitplan nicht manuell "basteln" müssen. Das System übernimmt die Planung für Sie.

### Wie Ihr Zeitplan entsteht (Abhängigkeiten)
Damit der Planer arbeiten kann, benötigt er zwei Informationen:
1.  **Ihre Verfügbarkeit:** Wann arbeiten Sie? (Definiert in den [Arbeitszeiten](Arbeitszeiten.md), [Pausen](Arbeitszeiten.md) und Termine)
2.  **Ihre Arbeit:** Was muss erledigt werden? (Definiert in den [Aufgaben](Aufgaben.md))

Sobald diese Informationen vorliegen, berechnet GoalDone automatisch, welche Aufgabe in welches Zeitfenster passt. Dabei werden Fristen und Prioritäten berücksichtigt. Aufgaben, die nicht in Ihre aktuelle Arbeitszeit passen, werden für spätere Zeitpunkte eingeplant.

## Visuelle Darstellung im Kalender
Damit Sie auf einen Blick sehen, womit Sie es zu tun haben, verwendet GoalDone eine eindeutige farbliche Kennzeichnung:

| Element               | Darstellung            | Bedeutung                                                                                                           |
|:----------------------|:-----------------------|:--------------------------------------------------------------------------------------------------------------------|
| **Aufgaben**          | **Blau**               | Arbeitsschritte, die vom System eingeplant wurden. Längere Aufgaben werden ggf. geteilt (z. B. "Aufgabe XY (1/2)"). |
| **Termine**           | **Dunkelgrau**         | Feste Termine, die zu einer bestimmten Zeit stattfinden müssen.                                                     |
| **Pausen**            | **Grün**               | Geplante Erholungszeiten innerhalb Ihrer Arbeitszeit.                                                               |
| **Nicht-Arbeitszeit** | **Diagonal gestreift** | Zeiträume, in denen Sie nicht arbeiten (z. B. Feierabend oder Wochenende). Hier werden keine Aufgaben geplant.      |

### Aufgaben-Stückelung
Wenn eine Aufgabe länger dauert als ein verfügbares Zeitfenster (oder Ihre Konzentration es erfordert), teilt GoalDone diese automatisch auf. Im Kalender sehen Sie dann Bezeichnungen wie "Projektbericht (1/3)", was bedeutet, dass dies der erste von drei Teilen der Aufgabe ist.
## Arbeitszeiten und Standardverfügbarkeit

Graue Bereiche im Kalender liegen außerhalb Ihrer Arbeitszeiten. In diesen Bereichen werden keine flexiblen Aufgaben eingeplant.

Wenn keine Arbeitszeiten konfiguriert sind, verwendet GoalDone standardmäßig Montag bis Freitag von 08:00 bis 17:00 Uhr als verfügbare Arbeitszeit. Feste Termine und Pausen blockieren die automatische Planung und können nicht für flexible Aufgaben genutzt werden.

## Rückmeldung nach Ablauf eines Aufgabenblocks

Wenn ein eingeplanter Aufgabenblock abgelaufen ist, kann GoalDone einen Dialog anzeigen. In diesem Dialog fragt das System, ob die Aufgabe abgeschlossen wurde.

Dabei gibt es je nach Aufgabe unterschiedliche Möglichkeiten:

* **Die ganze Aufgabe als erledigt markieren:**  
  Die Aufgabe wird vollständig abgeschlossen. Falls die Aufgabe aus mehreren Zeitblöcken besteht, werden alle zugehörigen Zeitblöcke als erledigt markiert.

* **Dialog schließen – nicht mehr anzeigen:**  
  Die Aufgabe bleibt offen und der konkrete Zeitblock wird nicht als erledigt markiert. Der Dialog wird für diesen Zeitblock nicht erneut angezeigt.

Bei Aufgaben, die nur aus einem einzigen Zeitblock bestehen, weist GoalDone darauf hin, dass dies die einzige Einheit der Aufgabe ist. Bei aufgeteilten Aufgaben kann sichtbar werden, welcher Teil der Aufgabe gerade betroffen ist.

## Wiederkehrende Aufgaben
Aufgaben, die sich regelmäßig wiederholen (z. B. "Wöchentliches Reporting"), erscheinen automatisch an den entsprechenden Tagen in Ihrem Kalender, sobald sie vom System für diesen Zeitraum eingeplant wurden. Sie müssen diese nicht jede Woche neu erstellen.

## Querverweise
*   [Arbeitszeiten definieren](Arbeitszeiten.md)
*   [Aufgaben verwalten](Aufgaben.md)
*   [Konten verknüpfen (für mehrere Organisationen)](Kontoverknuepfung.md)

[Zurück zur Übersicht](../README.md)
