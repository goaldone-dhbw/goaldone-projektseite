import os
import json
import shutil

DOCS_DIR = 'docs'
PUBLIC_DIR = 'public'

# Erstelle den public-Ordner neu und kopiere die docs hinein
if os.path.exists(PUBLIC_DIR):
    shutil.rmtree(PUBLIC_DIR)
os.makedirs(PUBLIC_DIR)

# Falls der docs Ordner noch nicht existiert, erstelle einen leeren
if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)

shutil.copytree(DOCS_DIR, os.path.join(PUBLIC_DIR, DOCS_DIR))

# Alle Dateien im docs Ordner auslesen
def get_files(dir_path):
    file_tree = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(root, file)
            # Relativen Pfad für die URLs erstellen
            rel_path = os.path.relpath(path, PUBLIC_DIR)
            file_tree.append(rel_path.replace('\\', '/'))
    return sorted(file_tree)

files = get_files(os.path.join(PUBLIC_DIR, DOCS_DIR))

# HTML-Gerüst mit CSS und JavaScript
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dokumenten Vorschau</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {{ display: flex; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 0; height: 100vh; background-color: #f9f9f9; }}
        #sidebar {{ width: 300px; background: #ffffff; padding: 20px; overflow-y: auto; border-right: 1px solid #e1e4e8; flex-shrink: 0; }}
        #content {{ flex: 1; padding: 40px; overflow-y: auto; display: flex; flex-direction: column; background: #ffffff; margin: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        h2, h3 {{ margin-top: 0; color: #24292e; }}
        ul {{ list-style-type: none; padding-left: 0; }}
        li {{ margin: 8px 0; font-size: 14px; word-break: break-all; }}
        a {{ text-decoration: none; color: #0366d6; cursor: pointer; }}
        a:hover {{ text-decoration: underline; }}
        iframe {{ flex: 1; border: none; width: 100%; height: 80vh; }}
        img {{ max-width: 100%; border-radius: 6px; }}
        .markdown-body {{ line-height: 1.6; color: #24292e; }}
        .markdown-body code {{ background: #f6f8fa; padding: 0.2em 0.4em; border-radius: 3px; font-family: monospace; }}
        .markdown-body pre code {{ display: block; padding: 16px; overflow: auto; }}
    </style>
</head>
<body>
    <div id="sidebar">
        <h3>Dateien</h3>
        <ul id="file-list"></ul>
    </div>
    <div id="content">
        <h2 id="preview-title">Willkommen</h2>
        <div id="preview-container" class="markdown-body">Bitte wähle eine Datei aus der linken Leiste aus, um eine Vorschau zu sehen.</div>
    </div>

    <script>
        const files = {json.dumps(files)};
        const list = document.getElementById('file-list');
        const preview = document.getElementById('preview-container');
        const title = document.getElementById('preview-title');

        files.forEach(file => {{
            const li = document.createElement('li');
            const a = document.createElement('a');
            // 'docs/' aus dem Anzeigenamen entfernen
            a.textContent = file.replace('docs/', '');
            a.onclick = () => loadPreview(file);
            li.appendChild(a);
            list.appendChild(li);
        }});

        async function loadPreview(file) {{
            const ext = file.split('.').pop().toLowerCase();
            const displayName = file.replace('docs/', '');
            title.textContent = displayName;

            if (ext === 'md') {{
                try {{
                    const response = await fetch(file);
                    const text = await response.text();
                    preview.innerHTML = marked.parse(text);
                }} catch (e) {{
                    preview.innerHTML = "<p>Fehler beim Laden der Markdown-Datei.</p>";
                }}
            }} else if (ext === 'pdf') {{
                preview.innerHTML = `<iframe src="${{file}}"></iframe>`;
            }} else if (['jpg', 'jpeg', 'png', 'gif', 'svg'].includes(ext)) {{
                preview.innerHTML = `<img src="${{file}}" alt="${{displayName}}" />`;
            }} else {{
                preview.innerHTML = `<p>Vorschau für diese Datei nicht verfügbar. <br><br> <a href="${{file}}" target="_blank" style="background:#0366d6; color:white; padding:8px 16px; border-radius:6px; display:inline-block;">Datei herunterladen / öffnen</a></p>`;
            }}
        }}
    </script>
</body>
</html>
"""

with open(os.path.join(PUBLIC_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Statische Seite erfolgreich im 'public' Ordner generiert.")