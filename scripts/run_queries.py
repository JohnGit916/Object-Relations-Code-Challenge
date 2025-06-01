from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    alice = Author.create("Alice")
    bob = Author.create("Bob")

    tech_today = Magazine.create("Tech Today", "Technology")
    health_weekly = Magazine.create("Health Weekly", "Health")

    # Pass full objects, not IDs
    Article.create("Quantum AI", "Quantum meets AI", alice, tech_today)
    Article.create("Vitamins", "All about vitamins", bob, health_weekly)

    print("Alice's magazines:", [m.name for m in alice.magazines()])
    print("Contributors to Tech Today:", [a.name for a in tech_today.contributors])

if __name__ == "__main__":
    main()
