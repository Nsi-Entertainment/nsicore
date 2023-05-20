import random
import easygui


# liste de mots possibles
mots = ['animal', 'arbuste', 'avion', 'balle', 'banane', 'boisson', 'bouteille', 'brique', 'camion', 'canape', 'carotte', 'carte', 'chaise', 'chat', 'chemise', 'chien', 'ciseaux', 'cle', 'collier', 'crayon', 'cuillere', 'echelle', 'eclair', 'ecran', 'etoile', 'fenetre', 'fleur', 'fourchette', 'gant', 'gateau', 'gomme', 'horloge', 'immeuble', 'insecte', 'jardin', 'jus', 'lampe', 'livre', 'machine', 'maison', 'montagne', 'mouton', 'mur', 'musique', 'oiseau', 'orange', 'ordinateur', 'pain', 'pantalon', 'papier', 'parapluie', 'pelle', 'pinceau', 'pizza', 'plat', 'poisson', 'porte', 'rateau', 'refrigerateur', 'riz', 'robot', 'roche', 'sac', 'salle', 'sapin', 'savon', 'scie', 'serpent', 'table', 'telephone', 'tente', 'tete', 'tomate', 'train', 'trousse', 'valise', 'velo', 'verre', 'vetement', 'voiture', 'yeux']

# choisir un mot au hasard
mot_secret = random.choice(mots)

# initialiser les variables
lettres_trouvees = []
lettres_ratees = []
liste_lettre = [chr(lettre) for lettre in range(97, 123)]

# fonction qui demande une lettre
def demande_lettre():
    erreur = True
    lettre = ""
    while erreur == True:
        lettre_temp = str(easygui.enterbox("Devinez une lettre : "))
        lettre_temp = lettre_temp.lower()
        if lettre_temp in liste_lettre and len(lettre_temp)<=1:
            lettre = lettre_temp
            erreur = False
        else: 
            print("Veuillez saisir un seul caractère valide")
    return lettre

def jouer():


    nb_coups = 0
    mot_affiche = ""


    # boucle principale
    while nb_coups < 8:

        # afficher le mot partiellement complété
        mot_affiche = ""
        for lettre in mot_secret:
            if lettre in lettres_trouvees:
                mot_affiche += lettre
            else:
                mot_affiche += "-"
        print(mot_affiche)

        # demander une lettre au joueur
        
        lettre = demande_lettre()  

        # vérifier si la lettre est dans le mot
        if lettre in mot_secret:
            lettres_trouvees.append(lettre)
            print("Bravo, la lettre est dans le mot !")
        else:
            lettres_ratees.append(lettre)
            nb_coups += 1
            print("Dommage, la lettre n'est pas dans le mot.")

        # vérifier si le joueur a deviné le mot
        if set(mot_secret) == set(lettres_trouvees):
            print("Félicitations, vous avez deviné le mot !")
            break

        # afficher le nombre de coup restant
        print("Nombre de coups restants: " + str(8-nb_coups))

    # afficher le mot complet
    msg_fin = str("Le mot était : " + mot_secret + "\n")
    easygui.msgbox(msg_fin)

# demander au joueur s'il veut jouer
reponse = easygui.ynbox("Voulez-vous lancer une partie de pendu ?",("Jouer ?"))

if reponse == True:
    jouer()
