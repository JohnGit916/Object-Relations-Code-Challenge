from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_create_article():
    author = Author.create("Writer")
    mag = Magazine.create("New Mag", "News")
    article = author.write_article("Test", "Content", mag)
    assert article.title == "Test"