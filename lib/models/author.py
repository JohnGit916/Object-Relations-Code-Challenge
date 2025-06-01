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

    # Added fix for missing find_by_name method
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM authors")
        return [cls(*row) for row in CURSOR.fetchall()]

    # Added fix for missing top_author method
    @classmethod
    def top_author(cls):
        from lib.models.article import Article
        authors = cls.all()
        if not authors:
            return None
        # create dict with author as key and count of articles as value
        author_counts = {author: len(author.articles()) for author in authors}
        top = max(author_counts, key=author_counts.get)
        return top

    def articles(self):
        from lib.models.article import Article
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        return [Article(*row) for row in CURSOR.fetchall()]

    # Added equality and hash for dictionary keys (used in top_author)
    def __eq__(self, other):
        if isinstance(other, Author):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
