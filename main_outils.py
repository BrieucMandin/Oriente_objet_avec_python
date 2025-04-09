import class_ as c
import class_.Boite_a_outils as b
import class_.Marteaux as m
import class_.Tournevis as t

def main():
    # Create an instance of the class Boite_a_outils
    my_Boite_a_outils = b.Boite_a_outils("red", 5)
    my_marteau = m.Martaux("Marteau de forgeron", 25.99, 1.2, 30, "Acier", "Noir")
    my_tournevis_cruciforme = t.Tournevis("Rouge", 16.,"Tournevis cruciforme")
    my_tournevis_plat = t.Tournevis("Rouge", 16.,"Tournevis plat")

    # Open the toolbox
    my_Boite_a_outils.Ouvrir()
    # Add the tools to the toolbox
    my_Boite_a_outils.Ajouter_Outil(my_marteau)
    my_Boite_a_outils.Ajouter_Outil(my_tournevis_cruciforme)

    # Close the toolbox
    my_Boite_a_outils.Fermer()
    # Print the list of tools in the toolbox
    print("Liste des outils dans la boite à outils : ", my_Boite_a_outils.Afficher_Outils)

    # Try to remove a tool from the toolbox
    my_Boite_a_outils.Retirer_Outil(my_marteau)
    # Try to add a tool to the toolbox
    my_Boite_a_outils.Ajouter_Outil(my_tournevis_plat)

    # Open the toolbox
    my_Boite_a_outils.Ouvrir()
    # Add the tool to the toolbox
    my_Boite_a_outils.Ajouter_Outil(my_tournevis_plat)

    # Print the list of tools in the toolbox
    print("Liste des outils dans la boite à outils : ", my_Boite_a_outils.Afficher_Outils)


main()





