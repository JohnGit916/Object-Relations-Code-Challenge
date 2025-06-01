import pytest
from lib.db.connection import CURSOR, CONN
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

# Helper to clear tables before each test
def clear_tables():
    CURSOR.execute("DELETE FROM articles")
    CURSOR.execute("DELETE FROM authors")
    CURSOR.execute("DELETE FROM magazines")
    CONN.commit()

# Pytest hook to run before each test
def setup_function():
    clear_tables()

def test_create_and_find_by_id():
    author = Author.create("Test Author")
    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.id == author.id
    assert found.name == "Test Author"

def test_find_by_name():
    author = Author.create("Unique Name")
    found = Author.find_by_name("Unique Name")
    assert found is not None
    assert found.name == "Unique Name"
    assert found.id == author.id

def test_all_returns_list():
    Author.create("Author One")
    Author.create("Author Two")
    authors = Author.all()
    assert isinstance(authors, list)
    assert all(isinstance(a, Author) for a in authors)

def test_articles_method():
    author = Author.create("Article Author")
    mag = Magazine.create("Sample Mag", "Category")
    Article.create("Title1", "Content1", author, mag)
    Article.create("Title2", "Content2", author, mag)

    articles = author.articles()
    assert isinstance(articles, list)
    assert all(article.author_id == author.id for article in articles)

def test_top_author():
    author1 = Author.create("Top One")
    author2 = Author.create("Top Two")
    mag = Magazine.create("Mag For Top", "Category")

    # author1 has 3 articles, author2 has 1
    Article.create("A1", "C", author1, mag)
    Article.create("A2", "C", author1, mag)
    Article.create("A3", "C", author1, mag)
    Article.create("B1", "C", author2, mag)

    top = Author.top_author()
    assert isinstance(top, Author)
    assert top.id == author1.id
    assert top.name == author1.name
