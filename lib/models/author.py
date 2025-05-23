from lib.db.connection import CURSOR, CONN
from lib.models.article import Article

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM authors")
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def articles(self):
        return Article.find_by_author_id(self.id)

    def magazines(self):
        return list(set(article.magazine() for article in self.articles()))

    def write_article(self, title, content, magazine):
        return Article.create(title, content, self, magazine)
