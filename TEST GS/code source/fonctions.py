import objet_tache

#Ce fichier sert à regrouper toutes les fonctions afin de rendre plus lisible le code et réustilisable :)
#Je n'ai pas mis certains bout de codes car ils intérragissent avec des élément de code_principale.py

def créer():


    titre = input("Son titre : ")
    description = input("Sa description : ")
    catégorie = input("Sa catégorie : ")
    état = input("Son état (TODO, DOING, DONE) : ")

    #J'ai ajouter un F avant tâche pour le différencier de l'objet
    Ftâche = objet_tache.tâche(titre, description, catégorie, état)

    return Ftâche
    
