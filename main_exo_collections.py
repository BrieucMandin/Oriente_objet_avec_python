#Conisgne :
# Créez 1 utilisateur et un modérateur.

# L’utilisateur crée un fil de discussion (vous pouvez inventer les messages).

# Le modérateur répond dans ce fil.

# L’utilisateur répond dans ce même fil par un message hors sujet❗

# Le modérateur répond que c’est hors sujet, puis supprime le message de l’utilisateur et son dernier message.

# L’utilisateur répond dans le fil en joignant une image.


import exo_heritage_class as e
import exo_heritage_class.User as u
import exo_heritage_class.Moderateur as m
import exo_heritage_class.Feed as f
import exo_heritage_class.Post as p


def main():
    # Création des utilisateurs
    utilisateur = u.User("JohnDoe", "password123")
    moderateur = m.Moderator("ModJane", "securepass")
    
    # Connexion des utilisateurs
    utilisateur.se_connecter("JohnDoe", "password123")
    moderateur.se_connecter("ModJane", "securepass")
    
    # Création d'un fil de discussion
    fil_discussion = utilisateur.creer_un_feed("Discussion Générale")
    
    # L'utilisateur poste un message
    post1 = utilisateur.poster_un_message("Salut1", "Bonjour à tous !", fil_discussion)
    
    
    # Le modérateur répond dans le fil
    post2 = moderateur.poster_un_message("Salut2", "Bienvenue sur le forum !", fil_discussion)
    
    
    # L'utilisateur répond avec un message hors sujet
    post3 = utilisateur.poster_un_message("Salut3", "Savez-vous où acheter un vélo pas cher ?", fil_discussion)
    
    
    # Le modérateur signale que c'est hors sujet et supprime le message
    print("Modérateur : Ce message est hors sujet et sera supprimé.")
    moderateur.supprimer_post(post3)
    
    # L'utilisateur répond en joignant une image
    post4 = utilisateur.poster_un_message("Salut4","Voici une image sympa !", fil_discussion, fichier="image.png")
    
    # Affichage du fil de discussion
    print(fil_discussion)
    
    # Déconnexion des utilisateurs
    utilisateur.se_deconnecter()
    moderateur.se_deconnecter()

main()