from lib.db.connection import CURSOR, CONN

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        CURSOR.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, category)

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM magazines")
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def articles(self):
        from lib.models.article import Article
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return [Article(*row) for row in CURSOR.fetchall()]

    def contributors(self):
        return list(set(article.author() for article in self.articles()))