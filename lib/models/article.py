from lib.db.connection import CURSOR, CONN

class Article:
    def __init__(self, id=None, title=None, content=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, title, content, author, magazine):
        # Accepts Author and Magazine objects, not just IDs
        author_id = author.id
        magazine_id = magazine.id

        CURSOR.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (title, content, author_id, magazine_id)
        )
        CONN.commit()
        return cls(CURSOR.lastrowid, title, content, author_id, magazine_id)

    @classmethod
    def find_by_author_id(cls, author_id):
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def magazine(self):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)

    def author(self):
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)
