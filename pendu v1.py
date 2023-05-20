import random

# liste de mots possibles
mots = ['animal', 'arbuste', 'avion', 'balle', 'banane', 'boisson', 'bouteille', 'brique', 'camion', 'canapé', 'carotte', 'carte', 'chaise', 'chat', 'chemise', 'chien', 'ciseaux', 'clé', 'collier', 'crayon', 'cuillère', 'échelle', 'éclair', 'écran', 'étoile', 'fenêtre', 'fleur', 'fourchette', 'gant', 'gâteau', 'gomme', 'horloge', 'immeuble', 'insecte', 'jardin', 'jus', 'lampe', 'livre', 'machine', 'maison', 'montagne', 'mouton', 'mur', 'musique', 'oiseau', 'orange', 'ordinateur', 'pain', 'pantalon', 'papier', 'parapluie', 'pelle', 'pinceau', 'pizza', 'plat', 'poisson', 'porte', 'râteau', 'réfrigérateur', 'riz', 'robot', 'roche', 'sac', 'salle', 'sapin', 'savon', 'scie', 'serpent', 'table', 'téléphone', 'tente', 'tête', 'tomate', 'train', 'trousse', 'valise', 'vélo', 'verre', 'vêtement', 'voiture', 'yeux']

# choisir un mot au hasard
mot_secret = random.choice(mots)

# initialiser les variables
lettres_trouvees = []
lettres_ratees = []
nb_coups = 0

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
    lettre = input("Devinez une lettre : ")

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

# afficher le mot complet
print("Le mot était :", mot_secret)
