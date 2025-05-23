from lib.db.connection import CONN, CURSOR

CURSOR.execute("DELETE FROM authors")
CURSOR.execute("DELETE FROM magazines")
CURSOR.execute("DELETE FROM articles")

CURSOR.execute("INSERT INTO authors (name) VALUES ('Alice')")
CURSOR.execute("INSERT INTO authors (name) VALUES ('Bob')")

CURSOR.execute("INSERT INTO magazines (name, category) VALUES ('Tech Today', 'Technology')")
CURSOR.execute("INSERT INTO magazines (name, category) VALUES ('Health Weekly', 'Health')")

CURSOR.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES ('AI Trends', 'AI is evolving', 1, 1)")
CURSOR.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES ('Healthy Eating', 'Tips and tricks', 2, 2)")

CONN.commit()