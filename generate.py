import os
import json
import shutil

DOCS_DIR = 'docs'
PUBLIC_DIR = 'public'

# Erstelle den public-Ordner neu und kopiere die docs hinein
if os.path.exists(PUBLIC_DIR):
    shutil.rmtree(PUBLIC_DIR)
os.makedirs(PUBLIC_DIR)

# Create the CNAME file for GitHub Pages
with open(os.path.join(PUBLIC_DIR, 'CNAME'), 'w', encoding='utf-8') as f:
    f.write("projekt.goaldone.de")

if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)

shutil.copytree(DOCS_DIR, os.path.join(PUBLIC_DIR, DOCS_DIR))

# Alle Dateien im docs Ordner auslesen
def get_files(dir_path):
    file_tree = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, PUBLIC_DIR)
            file_tree.append(rel_path.replace('\\', '/'))
    return sorted(file_tree)

files = get_files(os.path.join(PUBLIC_DIR, DOCS_DIR))

# Aktualisiertes HTML-Gerüst mit neuen Buttons und Styles
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
        #sidebar {{ width: 350px; background: #ffffff; padding: 20px; overflow-y: auto; border-right: 1px solid #e1e4e8; flex-shrink: 0; box-sizing: border-box; }}
        #content {{ flex: 1; padding: 40px; overflow-y: auto; display: flex; flex-direction: column; background: #ffffff; margin: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        h2, h3 {{ margin-top: 0; color: #24292e; }}
        ul {{ list-style-type: none; padding-left: 0; margin: 0; }}
        
        /* Neues Styling für die Listen-Elemente */
        li.file-item {{ display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 4px 0; border-bottom: 1px solid #f0f0f0; }}
        li.file-item:last-child {{ border-bottom: none; }}
        
        /* Datei-Link in der Sidebar */
        a.file-link {{ flex: 1; text-decoration: none; color: #0366d6; cursor: pointer; word-break: break-word; font-size: 14px; padding-right: 10px; }}
        a.file-link:hover {{ text-decoration: underline; }}
        
        /* Kleiner Download-Button Sidebar */
        a.dl-small {{ background: #eaeff5; color: #0366d6; text-decoration: none; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; border: 1px solid #c8e1ff; transition: all 0.2s; white-space: nowrap; }}
        a.dl-small:hover {{ background: #0366d6; color: white; }}

        /* Großer Download-Button für die Mitte */
        .unsupported-view {{ display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh; text-align: center; color: #586069; }}
        a.dl-large {{ background: #2ea44f; color: white; padding: 16px 32px; border-radius: 6px; text-decoration: none; font-size: 18px; font-weight: 600; margin-top: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: background 0.2s; }}
        a.dl-large:hover {{ background: #2c974b; }}

        iframe {{ flex: 1; border: none; width: 100%; min-height: 80vh; }}
        img {{ max-width: 100%; border-radius: 6px; }}
        
        /* Markdown Styles */
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
            li.className = 'file-item';

            // Vorschau-Link
            const a = document.createElement('a');
            a.className = 'file-link';
            a.textContent = file.replace('docs/', '');
            a.onclick = () => loadPreview(file);

            // Kleiner Download-Button
            const dl = document.createElement('a');
            dl.className = 'dl-small';
            dl.textContent = 'Download ↓';
            dl.href = file;
            dl.download = ''; // Das "download" Attribut zwingt den Browser zum Herunterladen
            dl.title = 'Datei herunterladen';

            li.appendChild(a);
            li.appendChild(dl);
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
                // Fallback: Großer Button in der Mitte für nicht unterstützte Dateien
                preview.innerHTML = `
                    <div class="unsupported-view">
                        <svg height="64" width="64" viewBox="0 0 24 24" fill="none" stroke="#586069" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 20px;">
                            <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                            <polyline points="13 2 13 9 20 9"></polyline>
                        </svg>
                        <h3>Keine Vorschau verfügbar</h3>
                        <p>Das Format dieser Datei (<b>.${{ext}}</b>) kann nicht direkt im Browser angezeigt werden.</p>
                        <a href="${{file}}" download class="dl-large">Datei herunterladen</a>
                    </div>
                `;
            }}
        }}
    </script>
</body>
</html>
"""

with open(os.path.join(PUBLIC_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Statische Seite mit Download-Buttons erfolgreich im 'public' Ordner generiert.")