# seed.py

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import CONN, CURSOR

# Clear tables
CURSOR.executescript("""
    DELETE FROM articles;
    DELETE FROM authors;
    DELETE FROM magazines;
""")

# Seed Authors
alice = Author.create("Alice")
bob = Author.create("Bob")

# Seed Magazines
tech_today = Magazine.create("Tech Today", "Technology")
health_weekly = Magazine.create("Health Weekly", "Health")

# Seed Articles
Article.create("AI Trends", "AI is evolving fast.", alice, tech_today)
Article.create("Healthy Eating", "Tips and tricks for nutrition.", bob, health_weekly)
Article.create("The Future of AI", "AI is changing everything.", alice, tech_today)
Article.create("Mindfulness", "Stay healthy mentally.", bob, health_weekly)

CONN.commit()
print("✅ Database seeded using model methods.")
