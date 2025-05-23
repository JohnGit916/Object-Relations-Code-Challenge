from lib.models.author import Author

def test_create_author():
    author = Author.create("Test Author")
    assert author.name == "Test Author"