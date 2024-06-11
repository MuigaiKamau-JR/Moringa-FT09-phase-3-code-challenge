from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def get_user_input():
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")
    return author_name, magazine_name, magazine_category, article_title, article_content

def insert_sample_data(author_name, magazine_name, magazine_category, article_title, article_content):
    # Create Author
    author = Author(name=author_name)
    author_id = author.id

    # Create Magazine
    magazine = Magazine(name=magazine_name, category=magazine_category)
    magazine_id = magazine.id

    # Create Article
    article = Article(author=author, magazine=magazine, title=article_title, content=article_content)

def main():
    # Initialize the database and create tables
    create_tables()

    # Get user input
    author_name, magazine_name, magazine_category, article_title, article_content = get_user_input()

    # Insert sample data into the database
    insert_sample_data(author_name, magazine_name, magazine_category, article_title, article_content)

    # Display inserted data (optional)
    display_data()

if __name__ == "__main__":
    main()

