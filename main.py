import sys

liste = []

menu = ("Choissisez parmis les 5 options suivantes :"
      "\n 1: Ajoutez un élément dans la liste"
      "\n 2: Retirez un élément dans la liste"
      "\n 3: Afficher la liste"
      "\n 4: Vider la liste"
      "\n 5: Quitter"
      "\n Votre choix : ")

selection = ["1", "2", "3", "4", "5"]

while True:

    reponse = input(menu)

    if reponse not in selection:
        print("Veuillez choisir une option valide")
        continue

    if reponse == "1":
        element = input("Quel élément souhaitez-vous ajouter à la liste : ")
        liste.append(element)
        print(f"L'élément {element} a été ajouté à la liste")
    elif reponse == "2":
        element = input("Quel élément souhaitez-vous retirer de la liste : ")
        if element not in liste:
            print(f"L'élément {element} ne se trouve pas dans la liste")
        else:
            liste.remove(element)
            print(f"L'élément {element} a été retiré à la liste")
    elif reponse == "3":
        if liste:
            print(f"Voici le contenu de votre liste :")
            for i, element in enumerate(liste):
                print(i, element)
        else:
            print("Votre liste ne contient aucun élément.")
    elif reponse == "4":
        liste.clear()
        print("La liste a été vidée de son contenu")
    elif reponse == "5":
        print("A bientôt !")
        sys.exit()

    print("-" * 50)