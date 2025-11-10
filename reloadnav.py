import os, json

# Alle mappen in huidige directory behalve verborgen
vakmappen = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]

# Toegestane bestandstypes voor documentatie
toegelaten_bestanden = (
    '.html', '.htm', '.pdf', '.doc', '.docx', '.xlsx', '.xls',
    '.ppt', '.pptx', '.png', '.jpg', '.jpeg', '.gif', '.txt', '.csv', '.zip'
)

for mapnaam in vakmappen:
    # Zoek ALLE .html-bestanden in de vakmap (lessen)
    html_bestanden = [
        f for f in os.listdir(mapnaam)
        if f.lower().endswith('.html')
        and not f.startswith('index')
    ]

    # Maak de data voor de lessenlijst
    lessen_data = [
        {"titel": os.path.splitext(f)[0].replace('_', ' ').capitalize(),
         "bestand": f"{mapnaam}/{f}"}
        for f in sorted(html_bestanden)
    ]

    # Controleer of er een submap 'bestanden' bestaat
    bestanden_map = os.path.join(mapnaam, 'bestanden')
    if os.path.isdir(bestanden_map):
        docs = [
            f for f in os.listdir(bestanden_map)
            if os.path.isfile(os.path.join(bestanden_map, f))
            and f.lower().endswith(toegelaten_bestanden)
            and not f.lower().endswith('index.json')
        ]

        # Als er documenten zijn, genereer documentatie-index
        if docs:
            doc_data = []
            for f in sorted(docs):
                titel = os.path.splitext(f)[0].replace('_', ' ').capitalize()
                doc_data.append({
                    "titel": titel,
                    "bestand": f"{mapnaam}/bestanden/{f}"
                })

            # Schrijf index.json in de submap 'bestanden'
            with open(os.path.join(bestanden_map, 'index.json'), 'w', encoding='utf-8') as f_docs:
                json.dump(doc_data, f_docs, indent=2, ensure_ascii=False)
            print(f"📘 {mapnaam}/bestanden/index.json aangemaakt ({len(docs)} bestanden)")

    # Alleen .html-lessen in hoofdindex opnemen
    if lessen_data:
        with open(os.path.join(mapnaam, 'index.json'), 'w', encoding='utf-8') as f:
            json.dump(lessen_data, f, indent=2, ensure_ascii=False)
        print(f"✔ {mapnaam}/index.json bijgewerkt ({len(lessen_data)} lessen)")
