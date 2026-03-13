import csv

dateiname = "lagerbestand.csv"

print("=== Lagerbestand Analyse ===\n")

anzahl_artikel = 0
anzahl_unter_mindestbestand = 0

with open(dateiname, mode="r", encoding="utf-8") as datei:
    reader = csv.DictReader(datei)

    for zeile in reader:
        anzahl_artikel += 1

        bestand = int(zeile["bestand"])
        mindestbestand = int(zeile["mindestbestand"])

        if bestand < mindestbestand:
            anzahl_unter_mindestbestand += 1
            print(
                f'- {zeile["artikelname"]} '
                f'(Bestand: {bestand}, Mindestbestand: {mindestbestand})'
            )

print("\n=== Zusammenfassung ===")
print(f"Geprüfte Artikel: {anzahl_artikel}")
print(f"Artikel unter Mindestbestand: {anzahl_unter_mindestbestand}")
