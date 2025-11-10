import os, json

vakmappen = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]

for mapnaam in vakmappen:
    bestanden = [f for f in os.listdir(mapnaam) if f.endswith('.html')]
    if not bestanden:
        continue
    data = [{"titel": f.replace('.html', '').capitalize(), "bestand": f"{mapnaam}/{f}"} for f in bestanden]
    with open(os.path.join(mapnaam, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✔ {mapnaam}/index.json bijgewerkt ({len(bestanden)} bestanden)")
