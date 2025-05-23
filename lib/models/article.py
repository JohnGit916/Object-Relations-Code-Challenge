from lib.db.connection import CURSOR, CONN

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, title, content, author, magazine):
        CURSOR.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (title, content, author.id, magazine.id)
        )
        CONN.commit()
        return cls(CURSOR.lastrowid, title, content, author.id, magazine.id)

    @classmethod
    def find_by_author_id(cls, author_id):
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        from lib.models.magazine import Magazine
        return [cls(*row) for row in CURSOR.fetchall()]

    def magazine(self):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)

    def author(self):
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)