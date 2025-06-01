from lib.db.connection import CURSOR, CONN

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        CURSOR.execute(
            "INSERT INTO magazines (name, category) VALUES (?, ?)",
            (name, category)
        )
        CONN.commit()
        return cls(CURSOR.lastrowid, name, category)

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    # Added find_by_category classmethod
    @classmethod
    def find_by_category(cls, category):
        CURSOR.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM magazines")
        return [cls(*row) for row in CURSOR.fetchall()]

    def articles(self):
        from lib.models.article import Article
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return [Article(*row) for row in CURSOR.fetchall()]

    # Added property article_titles
    @property
    def article_titles(self):
        return [article.title for article in self.articles()]

    # Added property contributors
    @property
    def contributors(self):
        from lib.models.author import Author
        CURSOR.execute(
            """
            SELECT DISTINCT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            """,
            (self.id,)
        )
        return [Author(*row) for row in CURSOR.fetchall()]

    # Added property contributing_authors
    @property
    def contributing_authors(self):
        from lib.models.author import Author
        CURSOR.execute(
            """
            SELECT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(articles.id) > 2
            """,
            (self.id,)
        )
        return [Author(*row) for row in CURSOR.fetchall()]

    # Added with_multiple_authors classmethod
    @classmethod
    def with_multiple_authors(cls):
        CURSOR.execute(
            """
            SELECT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            GROUP BY magazines.id
            HAVING COUNT(DISTINCT articles.author_id) > 1
            """
        )
        return [cls(*row) for row in CURSOR.fetchall()]

    # Added article_counts classmethod
    @classmethod
    def article_counts(cls):
        CURSOR.execute(
            """
            SELECT magazines.id, magazines.name, magazines.category, COUNT(articles.id) as article_count
            FROM magazines
            LEFT JOIN articles ON magazines.id = articles.magazine_id
            GROUP BY magazines.id
            """
        )
        return [(cls(row[0], row[1], row[2]), row[3]) for row in CURSOR.fetchall()]
