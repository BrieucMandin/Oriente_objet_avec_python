class Tournevis:

    def __init__(self, couleur,taille,type_tournevis):
        self.couleur = couleur
        self.taille = taille
        self.type_tournevis = type_tournevis

    def __str__(self):
        return f"Tournevis de type {self.type_tournevis}"
    
    def Visser(self):
        print(f"Visser avec le tournevis {self.type_tournevis}")

    def Devisser(self):
        print(f"Dévisser avec le tournevis {self.type_tournevis}")