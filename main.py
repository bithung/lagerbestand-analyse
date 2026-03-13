import csv

dateiname = "Lagerbestand.csv"

print("Artikel unter Mindestbestand:\n")

with open(dateiname, mode="r", encoding="utf-8") as datei:
    reader = csv.DictReader(datei)

    for zeile in reader:
        bestand = int(zeile["bestand"])
        mindestbestand = int(zeile["mindestbestand"])

        if bestand < mindestbestand:
            print(
                f'- {zeile["artikelname"]} '
                f'(Bestand: {bestand}, Mindestbestand: {mindestbestand})'
            )