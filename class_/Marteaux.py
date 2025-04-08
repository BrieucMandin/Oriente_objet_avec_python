class Martaux :
    def __init__(self, nom, prix, poids, taille, materiaux, couleur):
        self.nom = nom
        self.prix = prix
        self.poids = poids
        self.taille = taille
        self.materiaux = materiaux
        self.couleur = couleur

    def __str__(self):
        return f"Martaux: {self.nom}, Prix: {self.prix}, Poids: {self.poids}, Taille: {self.taille}"
    
    def Planter_clou(self):
        print(f"Un clou a été planter avec le marteau {self.nom}")

    def Casser_objet(self):
        print(f"Un objet a été casser avec le marteau {self.nom}")
    
    def Retirer_clou(self):
        print(f"Un clou a été retirer avec le marteau {self.nom}")

    def Peindre(self, couleur):
        self.couleur = couleur
        print(f"Le marteau {self.nom} a été peint de couleur {couleur}")