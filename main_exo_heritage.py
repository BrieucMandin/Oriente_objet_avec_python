import exo_heritage_class as e
import exo_heritage_class.User as u
import exo_heritage_class.Moderateur as m
import exo_heritage_class.Feed as f
import exo_heritage_class.Post as p

def main():
    

    # Création de deux utilisateurs
    user1 = u.User("Alice", "password123")
    user2 = u.User("Bob", "securepass")

    # Création d'un modérateur
    moderator = m.Moderator("Eve", "adminpass")

    # Connexion des utilisateurs
    user1.se_connecter("Alice", "password123")
    user2.se_connecter("Bob", "securepass")

    # Création de deux feeds
    feed1 = f.Feed("Python News", [])
    feed2 = f.Feed("Tech Updates", [])

    # Création de messages
    post1 = p.Post("Python 3.12 Released", "Check out the new features!", "2025-04-08")
    post2 = p.Post("Django 5.0", "New Django version is out!", "2025-04-08")
    post3 = p.Post("AI Advancements", "New AI models surpass expectations!", "2025-04-08")
    post4 = p.Post("Quantum Computing", "IBM's new quantum breakthrough!", "2025-04-08")
    post5 = p.Post("Cybersecurity Alert", "Major vulnerability found!", "2025-04-08")

    # Ajout des messages aux feeds
    feed1.Posts.extend([post1, post2, post3])
    feed2.Posts.extend([post4, post5])

    print("\n=== Feeds avant suppression de messages ===")
    print(feed1)
    print(feed2)

    # Suppression de messages par le modérateur
    moderator.delete_feed(feed1)

    # Modification d'un message
    moderator.modifier_post(post3, "AI is evolving rapidly!", "2025-04-09")

    print("\n=== Feeds après suppression de messages et modification ===")
    print(feed1)
    print(feed2)





# Call main
main()