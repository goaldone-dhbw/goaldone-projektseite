# Wie lade ich Dateien auf die Projektseite hoch?

Klone das Repository auf deinen Computer:

```bash
git clone https://github.com/Joinsider/goaldone-projektseite.git
```

Anschließend kannst du das Projekt auf deinem Computer bearbeiten. 
Alle Markdown Dateien `.md`, die du in den Ordner `docs` legst, werden auf der Webseite angezeigt.

Nachdem du deine Änderungen vorgenommen hast, kannst du die Änderungen einfach committen und pushen:

```bash
git add .
git commit -m "Deine Nachricht hier"
git push origin main
```


## Aufbau von Dokumenten
Die Dokumente auf der Webseite sind in Markdown geschrieben. Markdown ist eine einfache textbasiertes Dateiformat, das leicht zu lesen und zu schreiben ist. 

Hier sind einige grundlegende Markdown-Syntaxelemente, die du verwenden kannst:

- Überschriften: `#` für H1, `##` für H2, `###` für H3 usw.
- Fett: `**Text**` oder `__Text__`
- Kursiv: `*Text*` oder `_Text_`
- Listen: `-` oder `*` für ungeordnete Listen, `1.` für geordnete Listen
- Links: `[Linktext](URL)`
- Bilder: `![Alt-Text](URL)`
- Zitate: `> Zitat`
- Code: `` `Code` `` für Inline-Code oder `` ``` Codeblock über mehrere Zeilen ``` `` für Codeblöcke
- Tabellen: 
```
|Spalte 1 | Spalte 2 |
|----------|----------|
| Inhalt 1 | Inhalt 2 |
```

### Einbinden von Dateien
Du kannst auch Dateien wie Bilder oder PDFs in deine Markdown-Dokumente einbinden.

- Bilder: `![Alt-Text](Pfad/zum/Bild.jpg)`
- PDFs: `[PDF-Name](Pfad/zur/Datei.pdf)`

Dabei müssen die Dateien im `/docs/assets`-Ordner liegen, damit sie auf der Webseite eingebunden werden können.

Ein Beispiel:
[Beispiel-PDF](../assets/moodle/Aufgabenblatt1.pdf){ .md-button .md-button--primary }
[Andere Dateien](../assets/moodle/03-Aufwandserfassung.pdf){ .md-button .md-button--primary }