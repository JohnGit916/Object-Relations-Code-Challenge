import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import CONN, CURSOR

# Setup and teardown for tests to keep DB clean
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Clear tables before each test
    CURSOR.execute("DELETE FROM articles")
    CURSOR.execute("DELETE FROM authors")
    CURSOR.execute("DELETE FROM magazines")
    CONN.commit()
    yield
    # Clear tables after each test
    CURSOR.execute("DELETE FROM articles")
    CURSOR.execute("DELETE FROM authors")
    CURSOR.execute("DELETE FROM magazines")
    CONN.commit()

def test_create_article():
    author = Author.create("Test Author")
    magazine = Magazine.create("Test Magazine", "Tech")
    article = Article.create("Test Title", "Test Content", author, magazine)

    assert article.id is not None
    assert article.title == "Test Title"
    assert article.content == "Test Content"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id

def test_find_by_author_id():
    author1 = Author.create("Author One")
    author2 = Author.create("Author Two")
    magazine = Magazine.create("Magazine One", "Lifestyle")

    a1 = Article.create("Title1", "Content1", author1, magazine)
    a2 = Article.create("Title2", "Content2", author1, magazine)
    a3 = Article.create("Title3", "Content3", author2, magazine)

    articles_author1 = Article.find_by_author_id(author1.id)
    articles_author2 = Article.find_by_author_id(author2.id)

    assert len(articles_author1) == 2
    assert all(article.author_id == author1.id for article in articles_author1)

    assert len(articles_author2) == 1
    assert articles_author2[0].author_id == author2.id

def test_find_by_title():
    author = Author.create("Jane Doe")
    magazine = Magazine.create("Tech Mag", "Tech")
    article = Article.create("Unique Title", "Some content", author, magazine)

    found = Article.find_by_title("Unique Title")
    not_found = Article.find_by_title("Nonexistent Title")

    assert found is not None
    assert found.title == "Unique Title"
    assert found.id == article.id

    assert not_found is None

def test_article_relationships():
    author = Author.create("Rel Author")
    magazine = Magazine.create("Rel Magazine", "Science")
    article = Article.create("Rel Title", "Rel Content", author, magazine)

    assert article.author().id == author.id
    assert article.magazine().id == magazine.id