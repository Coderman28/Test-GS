import fonctions
import objet_tache

#voici le fichier du code principale


# J'ai créer une liste par état pour les afficher plus facilement sur le tableau
ListeDeTâchesTODO = []
ListeDeTâchesDOING = []
ListeDeTâchesDONE = []

colonneTODO = "TODO" + "\n" + "____" + "\n"
colonneDOING = "DOING" + "\n" + "_____" + "\n"
colonneDONE = "DONE" + "\n" + "____" + "\n"



while (True):

    try:

        boucle = 0

        for element in ListeDeTâchesTODO:
            
            colonneTODO += ListeDeTâchesTODO[boucle].titre
            colonneTODO += " : "
            
            colonneTODO += ListeDeTâchesTODO[boucle].catégorie
            colonneTODO += "\n"
            boucle = boucle + 1

        

        boucle = 0 

        

        for element in ListeDeTâchesDOING:
            
            colonneDOING += ListeDeTâchesDOING[boucle].titre
            colonneDOING += " : "
            
            colonneDOING += ListeDeTâchesDOING[boucle].catégorie
            colonneDOING += "\n"
            boucle += 1

        

        boucle = 0

        
        for element in ListeDeTâchesDONE:
            
            colonneDONE += ListeDeTâchesDONE[boucle].titre
            colonneDONE += " : "

            colonneDONE += ListeDeTâchesDONE[boucle].catégorie
            colonneDONE += "\n"
            boucle += 1

        
        print(colonneTODO)
        print(colonneDOING)
        print(colonneDONE)
        


        print("créer/modifier/supprimer/voir/quitter/déplacer")
        demande = input(">>> ")

    except ValueError:

        print("Veuillez écrire un mot")
        

    except KeyboardInterrupt :

        print("N'appuyez pas sur Ctrl + c")
        

    else:

        if demande == "créer":
            NouvelleTâche = fonctions.créer()

            if NouvelleTâche.état == "TODO":
                ListeDeTâchesTODO.append(NouvelleTâche)
            elif NouvelleTâche.état == "DOING":
                ListeDeTâchesDOING.append(NouvelleTâche)
            elif NouvelleTâche.état == "DONE":
                ListeDeTâchesDONE.append(NouvelleTâche)

        elif demande == "supprimer":

            #je n'ai pas mis ce code dans le fonctions.py car il travaille avec les liste

            try:

                tache_à_supprimer = input("Lequel voulez-vous supprimez(entrez son titre) : ")

            except ValueError:

                print("Tapez un titre")
                

            except KeyboardInterrupt:

                print("Pas de Ctrl+C")
                

            else :

                emplacement_actuel = input("Quel est son emplacement actuel : ")

                if emplacement_actuel == "TODO":

                    compteur = 0

                    for element in ListeDeTâchesTODO:
                        if ListeDeTâchesTODO[compteur].titre == tache_à_supprimer:
                            
                            confirmation = input("En êtes vous sur(oui/non) : ")

                            if confirmation == "oui":
                                ListeDeTâchesTODO.remove(ListeDeTâchesTODO[compteur])
                            else:

                                print("La tâche n'a pas été supprimé.")

                        compteur += 1

                
                elif emplacement_actuel == "DOING":

                    compteur = 0

                    for element in ListeDeTâchesDOING:
                        if ListeDeTâchesDOING[compteur].titre == tache_à_supprimer:
                            
                            confirmation = input("En êtes vous sur(oui/non) : ")

                            if confirmation == "oui":
                                ListeDeTâchesDOING.remove(ListeDeTâchesDOING[compteur])
                            else:

                                print("La tâche n'a pas été supprimé.")

                        compteur += 1

                
                elif emplacement_actuel == "DONE":

                    compteur = 0

                    for element in ListeDeTâchesDONE:
                        if ListeDeTâchesDONE[compteur].titre == tache_à_supprimer:
                            
                            confirmation = input("En êtes vous sur(oui/non) : ")

                            if confirmation == "oui":
                                ListeDeTâchesDONE.remove(ListeDeTâchesDONE[compteur])
                            else:

                                print("La tâche n'a pas été supprimé.")

                        compteur += 1



        elif demande == "quitter":

           #je n'ai pas mis ce code au fonctions.py à cause d'un bug
           exit()    

        elif demande == "voir":

            #je n'ai pas mis ce code dans le fonctions.py car il travaille avec la liste

            try:

                tâche_à_voir = input("Lequel voulez-vous voir(écrivrez son titre) : ")

            except ValueError:

                print("Tapez un titre")

            except KeyboardInterrupt:

                print("Pas de Ctrl + c")

            else :

                emplacement_actuel = input("Quel est son emplacement actuel : ")

                if emplacement_actuel == "TODO":

                    compteur = 0

                    for element in ListeDeTâchesTODO:
                        if ListeDeTâchesTODO[compteur].titre == tâche_à_voir:
                            print ("titre : ", ListeDeTâchesTODO[compteur].titre)
                            print("description : ", ListeDeTâchesTODO[compteur].description)
                            print("catégorie : ", ListeDeTâchesTODO[compteur].catégorie)
                            print("état : ", ListeDeTâchesTODO[compteur].état)
                            print("                                   ") # J'ai fais ça pour sauter une ligne.
                    
                        compteur += 1

                elif emplacement_actuel == "DOING":

                    compteur = 0

                    for element in ListeDeTâchesDOING:
                        if ListeDeTâchesDOING[compteur].titre == tâche_à_voir:
                            print ("titre : ", ListeDeTâchesDOING[compteur].titre)
                            print("description : ", ListeDeTâchesDOING[compteur].description)
                            print("catégorie : ", ListeDeTâchesDOING[compteur].catégorie)
                            print("état : ", ListeDeTâchesDOING[compteur].état)
                            print("                                   ") # J'ai fais ça pour sauter une ligne.
                    
                        compteur += 1

                elif emplacement_actuel == "DONE":

                    compteur = 0

                    for element in ListeDeTâchesDONE:
                        if ListeDeTâchesDONE[compteur].titre == tâche_à_voir:
                            print ("titre : ", ListeDeTâchesDONE[compteur].titre)
                            print("description : ", ListeDeTâchesDONE[compteur].description)
                            print("catégorie : ", ListeDeTâchesDONE[compteur].catégorie)
                            print("état : ", ListeDeTâchesDONE[compteur].état)
                            print("                                   ") # J'ai fais ça pour sauter une ligne.
                    
                        compteur += 1

        elif demande == "modifier":

            try:

                tâche_à_modifier = input("Quel tâche veux-tu modifier : ")

            except ValueError:

                print("Tâpe une tâche")

            except KeyboardInterrupt:

                print("Pas de Ctrl + c")

            else:

                emplacement_actuel = input("Quel est son emplacement actuel : ")

                if emplacement_actuel == "TODO":

                    compteur = 0

                    for element in ListeDeTâchesTODO:
                        if ListeDeTâchesTODO[compteur].titre == tâche_à_modifier:
                            nouvelle_description = input("Quel est la nouvel description : ")
                            nouvelle_catégorie = input("Quel est la nouvel catégorie : ")

                            ListeDeTâchesTODO[compteur].description = nouvelle_description
                            ListeDeTâchesTODO[compteur].catégorie = nouvelle_catégorie

                        compteur += 1

                elif emplacement_actuel == "DOING":

                    compteur = 0

                    for element in ListeDeTâchesDOING:
                        if ListeDeTâchesDOING[compteur].titre == tâche_à_modifier:
                            nouvelle_description = input("Quel est la nouvel description : ")
                            nouvelle_catégorie = input("Quel est la nouvel catégorie : ")

                            ListeDeTâchesDOING[compteur].description = nouvelle_description
                            ListeDeTâchesDOING[compteur].catégorie = nouvelle_catégorie

                        compteur += 1

                elif emplacement_actuel == "DONE":

                    compteur = 0

                    for element in ListeDeTâchesDONE:
                        if ListeDeTâchesDONE[compteur].titre == tâche_à_modifier:
                            nouvelle_description = input("Quel est la nouvel description : ")
                            nouvelle_catégorie = input("Quel est la nouvel catégorie : ")

                            ListeDeTâchesDONE[compteur].description = nouvelle_description
                            ListeDeTâchesDONE[compteur].catégorie = nouvelle_catégorie

                        compteur += 1

                else:

                    print("Désolé, vous avez du mal tapé quelque chose.")

        elif demande == "déplacer":

            #Etant donné qu'elle intéragit avec les listes, je n'ai pas pu la mettre au fonctions.py

            try:

                tâche_à_déplacer = input("Laquel voulez-vous déplacer : ")

            except ValueError:

                print("Tapez des caractères")

            except KeyboardInterrupt:

                print ("Pas de Ctrl + c")

            else:

                #Hélas je n'ai trouvé aucune meilleur solution que cette séquence de 100 lignes de code.

                emplacement_actuel = input("Il est actuellement à quel endroit : ")

                if emplacement_actuel == "TODO":

                    compteur = 0

                    for element in ListeDeTâchesTODO:
                        if ListeDeTâchesTODO[compteur].titre == tâche_à_déplacer:
                            lieu_de_déplacement = input("Vers où la déplacer : ")

                            if lieu_de_déplacement == "DOING":
                                
                                objet_à_déplacer = ListeDeTâchesTODO[compteur]
                                ListeDeTâchesTODO.remove(ListeDeTâchesTODO[compteur])
                                ListeDeTâchesDOING.append(objet_à_déplacer)

                            elif lieu_de_déplacement == "DONE":

                                objet_à_déplacer = ListeDeTâchesTODO[compteur]
                                ListeDeTâchesTODO.remove(ListeDeTâchesTODO[compteur])
                                ListeDeTâchesDONE.append(objet_à_déplacer)

                            else:

                                print("Impossible de faire cette action, si vous avez mis TODO ")
                                print("Votre tâche y est déjà.")

                        compteur += 1


                elif emplacement_actuel == "DOING":

                    compteur = 0

                    for element in ListeDeTâchesDOING:
                        if ListeDeTâchesDOING[compteur].titre == tâche_à_déplacer:
                            lieu_de_déplacement = input("Vers où la déplacer : ")

                            if lieu_de_déplacement == "TODO":
                                
                                objet_à_déplacer = ListeDeTâchesDOING[compteur]
                                ListeDeTâchesDOING.remove(ListeDeTâchesDOING[compteur])
                                ListeDeTâchesTODO.append(objet_à_déplacer)

                            elif lieu_de_déplacement == "DONE":

                                objet_à_déplacer = ListeDeTâchesDOING[compteur]
                                ListeDeTâchesDOING.remove(ListeDeTâchesDOING[compteur])
                                ListeDeTâchesDONE.append(objet_à_déplacer)
                                

                            else:

                                print("Impossible de faire cette action, si vous avez mis DOING ")
                                print("Votre tâche y est déjà.")


                        compteur += 1

                elif emplacement_actuel == "DONE":

                    compteur = 0

                    for element in ListeDeTâchesDONE:
                        if ListeDeTâchesDONE[compteur].titre == tâche_à_déplacer:
                            lieu_de_déplacement = input("Vers où la déplacer : ")

                            if lieu_de_déplacement == "TODO":
                                
                                objet_à_déplacer = ListeDeTâchesDONE[compteur]
                                ListeDeTâchesDONE.remove(ListeDeTâchesDONE[compteur])
                                ListeDeTâchesTODO.append(objet_à_déplacer)

                            elif lieu_de_déplacement == "DOING":

                                objet_à_déplacer = ListeDeTâchesDONE[compteur]
                                ListeDeTâchesDONE.remove(ListeDeTâchesDONE[compteur])
                                ListeDeTâchesDOING.append(objet_à_déplacer)
                                

                            else:

                                print("Impossible de faire cette action, si vous avez mis DOING ")
                                print("Votre tâche y est déjà.")


                        compteur += 1

                
                else :

                    print("Impossible de faire l'action.")

