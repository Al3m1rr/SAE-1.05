import csv


etudiants = [
{"ID": 1, "Nom": "Schmitt", "Prenom": "Albert", "Note": 9},
{"ID": 2, "Nom": "Al-Hakim", "Prenom": "Yasmine", "Note": 17},
{"ID": 3, "Nom": "Tran", "Prenom": "Sebastien", "Note": 12},
{"ID": 4, "Nom": "Meyer", "Prenom": "Claire", "Note": 16},
{"ID": 5, "Nom": "Kobayashi", "Prenom": "Kaito", "Note": 11}
]

with open('TD2_sae.csv', mode='w',encoding='utf-8',newline='') as file :
    champs = ["ID","Nom","Prenom","Note"]
    fichier = csv.DictWriter(file, fieldnames=champs)
    fichier.writeheader()
    fichier.writerows(etudiants)

with open('resultats.csv', mode='w', encoding='utf-8', newline='') as file:
    champs = ["Nom", "Prenom", "Résultat"]
    fichier = csv.DictWriter(file, fieldnames=champs)
    fichier.writeheader()

    for d in etudiants:
        if d["Note"] >= 10:
            resultat = "Admis"
        else:
            resultat = "Refusé"

        fichier.writerow({
            "Nom": d["Nom"],
            "Prenom": d["Prenom"],
            "Résultat": resultat
        })


