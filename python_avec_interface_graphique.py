import random
import easygui

# Liste de mots possibles
mots = ['animal', 'arbuste', 'avion', 'balle', 'bnanane', 'boisson', 'bouteille', 'brique', 'camion', 'canape', 'carotte', 'carte', 'chaise', 'chat', 'chemise', 'chien', 'ciseaux', 'cle', 'collier', 'crayon', 'cuillere', 'echelle', 'eclair', 'ecran', 'etoile', 'fenetre', 'fleur', 'fourchette', 'gant', 'gateau', 'gomme', 'horloge', 'immeuble', 'insecte', 'jardin', 'jus', 'lampe', 'livre', 'machine', 'maison', 'montagne', 'mouton', 'mur', 'musique', 'oiseau', 'orange', 'ordinateur', 'pain', 'pantalon', 'papier', 'parapluie', 'pelle', 'pinceau', 'pizza', 'plat', 'poisson', 'porte', 'rateau', 'refrigerateur', 'riz', 'robot', 'roche', 'sac', 'salle', 'sapin', 'savon', 'scie', 'serpent', 'table', 'telephone', 'tente', 'tete', 'tomate', 'train', 'trousse', 'valise', 'velo', 'verre', 'vetement', 'voiture', 'yeux']

# Choisir un mot au hasard
mot_secret = random.choice(mots)

# Initialiser les variables
lettres_trouvees = []
lettres_ratees = []
liste_lettre = [chr(lettre) for lettre in range(97, 123)]

# Fonction qui demande une lettre et affiche les informations
def demande_lettre():
    mot_affiche = ""
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "- "
    message = f"Mot à deviner : {mot_affiche}\nLettres incorrectes : {', '.join(lettres_ratees)}\nNombre de coups restants : {8 - len(lettres_ratees)}"
    lettre = easygui.enterbox(message, title="Devinez une lettre")
    if lettre is None:
        quitter = easygui.ynbox("Voulez-vous vraiment quitter le jeu ?", title="Confirmation")
        if quitter:
            exit()
        else:
            return demande_lettre()
    elif len(lettre) != 1 or lettre.lower() not in liste_lettre:
        easygui.msgbox("Veuillez saisir une seule lettre valide", title="Erreur")
        return demande_lettre()
    return lettre.lower()

def jouer():
    # Boucle principale
    while len(lettres_ratees) < 8:
        lettre = demande_lettre()
        if lettre in mot_secret:
            lettres_trouvees.append(lettre)
            if set(mot_secret) == set(lettres_trouvees):
                easygui.msgbox(f"Félicitations, vous avez deviné le mot '{mot_secret}' !", title="Victoire")
                break
        else:
            lettres_ratees.append(lettre)
    else:
        easygui.msgbox(f"Vous avez épuisé tous vos coups. Le mot à deviner était '{mot_secret}'.", title="Défaite")

# Demander au joueur s'il veut jouer
reponse = easygui.ynbox("Voulez-vous lancer une partie de pendu ?", title="Jouer ?")

if reponse:
    jouer()
