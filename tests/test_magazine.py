from lib.models.magazine import Magazine

def test_create_magazine():
    mag = Magazine.create("Science World", "Science")
    assert mag.name == "Science World"