from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    print("All Authors:")
    authors = Author.all()
    for author in authors:
        print(f"{author.id} {author.name}")

    print("\nFind Author by Name:")
    author = Author.find_by_name("Alice")  # Replace with actual seeded name
    if author:
        print(f"Found: {author.id} {author.name}")
    else:
        print("Author not found.")

    print("\nTop Author:")
    top_author = Author.top_author()
    if top_author:
        print(f"{top_author.name} with {len(top_author.articles())} articles")
    else:
        print("No top author found.")

    print("\nAll Magazines:")
    magazines = Magazine.all()
    for mag in magazines:
        print(f"{mag.id} {mag.name} - {mag.category}")

    print("\nMagazine Contributors for first magazine:")
    if magazines:
        contributors = magazines[0].contributors
        for c in contributors:
            print(f"{c.name}")

    print("\nArticles by first author:")
    if authors:
        articles = authors[0].articles()
        for art in articles:
            print(f"{art.title}")

if __name__ == "__main__":
    main()
