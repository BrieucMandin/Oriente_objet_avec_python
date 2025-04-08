
class Boite_a_outils :
    def __init__(self, couleur, taille):
        self.couleur = couleur
        self.taille = taille
        self.outils = []
        self.statut_d_Ouverture = False
        pass

    def Ouvrir(self):
        print("Boite à outils est ouverte")
        self.statut_d_Ouverture = True
    
    def Fermer(self):
        print("Boite à outils est fermée")
        self.statut_d_Ouverture = False
    
    def Ajouter_Outil(self, outil):
        if self.statut_d_Ouverture == True:
            self.outils.append(outil)
            print("Outil ajouté")
            print(f"l'outil {outil} a été ajouté à la boite à outils")
            print("Liste des outils : ", self.outils)
            
        else:
            print("Boite à outils est fermée veuillez l'ouvrir avant d'ajouter un outil")

    def Retirer_Outil(self, outil):
        if self.statut_d_Ouverture == True:
            if outil in self.outils:
                self.outils.remove(outil)
                print("Outil retiré")
                print(f"l'outil {outil} a été retiré de la boite à outils")
                print("Liste des outils : ", self.outils)
            else:
                print("L'outil n'est pas dans la boite à outils")
        else:
            print("Boite à outils est fermée veuillez l'ouvrir avant de retirer un outil")

    def Afficher_Outils(self):
        if self.statut_d_Ouverture == True:
            print("Liste des outils : ", self.outils)
        else:
            print("Boite à outils est fermée")