import pytest
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

def test_find_by_category():
    mag1 = Magazine.create("Tech Today", "Technology")
    mag2 = Magazine.create("Health Weekly", "Health")

    tech_mags = Magazine.find_by_category("Technology")
    assert any(mag.name == "Tech Today" for mag in tech_mags)
    assert all(mag.category == "Technology" for mag in tech_mags)

def test_article_titles_and_contributors():
    author = Author.create("John Doe")
    mag = Magazine.create("Sample Mag", "Sample")

    art1 = Article.create("Title 1", "Content 1", author, mag)
    art2 = Article.create("Title 2", "Content 2", author, mag)

    titles = mag.article_titles
    assert "Title 1" in titles
    assert "Title 2" in titles

    contributors = mag.contributors
    assert any(c.id == author.id for c in contributors)

def test_contributing_authors_property():
    author1 = Author.create("Author 1")
    author2 = Author.create("Author 2")
    mag = Magazine.create("Contrib Mag", "Misc")

    # author1 writes 3 articles, author2 writes 1 article
    Article.create("Art1", "C", author1, mag)
    Article.create("Art2", "C", author1, mag)
    Article.create("Art3", "C", author1, mag)
    Article.create("Art4", "C", author2, mag)

    contrib_authors = mag.contributing_authors
    assert len(contrib_authors) == 1
    assert contrib_authors[0].id == author1.id

def test_with_multiple_authors():
    author1 = Author.create("Author A")
    author2 = Author.create("Author B")
    mag1 = Magazine.create("MultiAuthor Mag", "General")
    mag2 = Magazine.create("SingleAuthor Mag", "General")

    # mag1 has two authors
    Article.create("Art1", "C", author1, mag1)
    Article.create("Art2", "C", author2, mag1)

    # mag2 has only one author
    Article.create("Art3", "C", author1, mag2)

    mags = Magazine.with_multiple_authors()
    assert any(mag.id == mag1.id for mag in mags)
    assert all(mag.id != mag2.id for mag in mags)

def test_article_counts():
    mag1 = Magazine.create("Count Mag1", "Cat")
    mag2 = Magazine.create("Count Mag2", "Cat")

    author = Author.create("Author Count")

    Article.create("A1", "Content", author, mag1)
    Article.create("A2", "Content", author, mag1)
    Article.create("A3", "Content", author, mag2)

    counts = Magazine.article_counts()
    counts_dict = {mag.name: count for mag, count in counts}

    assert counts_dict.get("Count Mag1") == 2
    assert counts_dict.get("Count Mag2") == 1

def test_magazine_create_and_all():
    mag1 = Magazine.create("Mag A", "Tech")
    mag2 = Magazine.create("Mag B", "Health")

    all_mags = Magazine.all()
    assert len(all_mags) >= 2
    assert any(mag.name == "Mag A" for mag in all_mags)
    assert any(mag.name == "Mag B" for mag in all_mags)