from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

alice = Author.create("Alice")
bob = Author.create("Bob")

tt = Magazine.create("Tech Today", "Technology")
hw = Magazine.create("Health Weekly", "Health")

alice.write_article("Quantum AI", "Quantum meets AI", tt)
bob.write_article("Vitamins", "All about vitamins", hw)

print("Alice's magazines:", [m.name for m in alice.magazines()])
print("Contributors to Tech Today:", [a.name for a in tt.contributors()])