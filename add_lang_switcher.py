#!/usr/bin/env python3
"""
Ajoute un sélecteur de langue horizontal dans le footer de chaque page.
"""

import os

BASE = '/root/ai-affi/candy-ai-porn.com'
LANGS = ['fr', 'de', 'es', 'it', 'pt', 'nl', 'pl', 'ru', 'tr', 'kr', 'ja', 'hi']

# Configuration des langues avec drapeaux emoji
LANG_CONFIG = {
    'en': {'name': 'English', 'flag': '🇬🇧', 'path': '/'},
    'fr': {'name': 'Français', 'flag': '🇫🇷', 'path': '/fr/'},
    'de': {'name': 'Deutsch', 'flag': '🇩🇪', 'path': '/de/'},
    'es': {'name': 'Español', 'flag': '🇪🇸', 'path': '/es/'},
    'it': {'name': 'Italiano', 'flag': '🇮🇹', 'path': '/it/'},
    'pt': {'name': 'Português', 'flag': '🇵🇹', 'path': '/pt/'},
    'nl': {'name': 'Nederlands', 'flag': '🇳🇱', 'path': '/nl/'},
    'pl': {'name': 'Polski', 'flag': '🇵🇱', 'path': '/pl/'},
    'ru': {'name': 'Русский', 'flag': '🇷🇺', 'path': '/ru/'},
    'tr': {'name': 'Türkçe', 'flag': '🇹🇷', 'path': '/tr/'},
    'kr': {'name': '한국어', 'flag': '🇰🇷', 'path': '/kr/'},
    'ja': {'name': '日本語', 'flag': '🇯🇵', 'path': '/ja/'},
    'hi': {'name': 'हिन्दी', 'flag': '🇮🇳', 'path': '/hi/'},
}

# CSS pour le sélecteur de langue
LANG_SWITCHER_CSS = """
    /* ---- LANGUAGE SWITCHER ---- */
    .lang-switcher {
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 18px 0;
      margin: 22px 0;
    }
    .lang-switcher-label {
      color: var(--text-secondary);
      font-size: .78rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: .5px;
      margin-bottom: 10px;
      text-align: center;
    }
    .lang-switcher-list {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px 14px;
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .lang-switcher-list li { margin: 0; }
    .lang-switcher-list a {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      color: var(--text-secondary);
      font-size: .82rem;
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid transparent;
      transition: all .2s;
      text-decoration: none;
    }
    .lang-switcher-list a:hover {
      color: var(--text-primary);
      background: rgba(255,255,255,.06);
      border-color: var(--border);
    }
    .lang-switcher-list a.active {
      color: var(--accent);
      background: rgba(255,71,133,.1);
      border-color: var(--accent);
      font-weight: 600;
      pointer-events: none;
    }
    .lang-switcher-list .flag { font-size: 1rem; line-height: 1; }
    @media (max-width: 640px) {
      .lang-switcher-list { gap: 6px 10px; }
      .lang-switcher-list a { font-size: .75rem; padding: 4px 8px; }
    }
"""

# Génère le HTML du sélecteur pour une langue donnée
def generate_lang_switcher(current_lang):
    items = []
    for code, cfg in LANG_CONFIG.items():
        active_class = 'active' if code == current_lang else ''
        items.append(f'          <li><a href="{cfg["path"]}" class="{active_class}"><span class="flag">{cfg["flag"]}</span> {cfg["name"]}</a></li>')
    
    return """    <div class="lang-switcher">
      <div class="lang-switcher-label">🌐 Languages / Langues / Sprachen</div>
      <ul class="lang-switcher-list">
""" + "\n".join(items) + """
      </ul>
    </div>
"""

# 1. Ajouter le CSS dans le <style> du fichier racine
root_path = os.path.join(BASE, 'index.html')
with open(root_path, 'r', encoding='utf-8') as f:
    root_content = f.read()

# Insérer le CSS avant /* ---- MODAL ---- */
if '/* ---- LANGUAGE SWITCHER ---- */' not in root_content:
    root_content = root_content.replace('    /* ---- MODAL ---- */', LANG_SWITCHER_CSS + '\n    /* ---- MODAL ---- */')
    
    # Ajouter le sélecteur avant footer-bottom
    lang_html = generate_lang_switcher('en')
    root_content = root_content.replace('    <div class="footer-bottom">', lang_html + '    <div class="footer-bottom">')
    
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(root_content)
    print("✅ EN (root): lang switcher ajouté")
else:
    print("⚠️  EN (root): déjà présent")

# 2. Ajouter dans chaque sous-dossier langue
for lang in LANGS:
    path = os.path.join(BASE, lang, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si déjà présent
    if '/* ---- LANGUAGE SWITCHER ---- */' in content:
        print(f"⚠️  {lang}: déjà présent")
        continue
    
    # Ajouter le CSS
    content = content.replace('    /* ---- MODAL ---- */', LANG_SWITCHER_CSS + '\n    /* ---- MODAL ---- */')
    
    # Ajouter le HTML
    lang_html = generate_lang_switcher(lang)
    content = content.replace('    <div class="footer-bottom">', lang_html + '    <div class="footer-bottom">')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {lang}: lang switcher ajouté")

print("\n🎉 Terminé!")
