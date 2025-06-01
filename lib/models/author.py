from lib.db.connection import CURSOR, CONN

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM authors")
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def top_author(cls):
        authors = cls.all()
        if not authors:
            return None
        author_counts = {author: len(author.articles()) for author in authors}
        top = max(author_counts, key=author_counts.get)
        return top

    def articles(self):
        from lib.models.article import Article
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        return [Article(*row) for row in CURSOR.fetchall()]

    def magazines(self):
        from lib.models.magazine import Magazine
        CURSOR.execute(
            """
            SELECT DISTINCT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
            """,
            (self.id,)
        )
        rows = CURSOR.fetchall()
        return [Magazine(*row) for row in rows]

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
