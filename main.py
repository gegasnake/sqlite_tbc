import sqlite3
from faker import Faker
import random

fake = Faker()
conn = sqlite3.connect('books_authors.db')
cursor = conn.cursor()

# I created an Author table which consists of: id, first_name, last_name, birth_date, birth_place
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Author (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        birth_date DATE,
        birth_place TEXT
    )
''')

# Created a Book table which is connected to Author table with author_id.
# it contains: id, title, category, pages, publish_date, author_id.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT,
        pages INTEGER,
        publish_date DATE,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES Author(id)
    )
''')

# here I save the changes so that in the future my code works
conn.commit()


def generate_random_authors(n):
    """Function where I generate random authors with a help of 'fake' package and save the changes
    when I write in the database"""
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=20, maximum_age=80).strftime('%Y-%m-%d')
        birth_place = fake.city()
        cursor.execute('''
            INSERT INTO Author (first_name, last_name, birth_date, birth_place)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, birth_date, birth_place))
    conn.commit()


generate_random_authors(500)


def generate_random_books(n):
    """Function where I generate random books with a help of 'fake' package and save the changes"""
    cursor.execute('SELECT id FROM Author')
    author_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        title = fake.sentence(nb_words=3)
        category = random.choice(['Fiction', 'Science', 'Technology', 'History', 'Fantasy'])
        pages = random.randint(100, 1000)
        publish_date = fake.date_between(start_date='-50y', end_date='today').strftime('%Y-%m-%d')
        author_id = random.choice(author_ids)
        cursor.execute('''
            INSERT INTO Book (title, category, pages, publish_date, author_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, category, pages, publish_date, author_id))
    conn.commit()


generate_random_books(1000)

# Here I find a book with the most pages in the database
cursor.execute('''
    SELECT * FROM Book
    ORDER BY pages DESC
    LIMIT 1
''')
max_pages_book = cursor.fetchone()
print("Book with most pages:", max_pages_book)

# Here I calculate the average of book pages in the whole database
cursor.execute('''
    SELECT AVG(pages) FROM Book
''')
avg_pages = cursor.fetchone()[0]
print("Average number of pages in books:", avg_pages)

# Here I find the youngest author there is in database
cursor.execute('''
    SELECT * FROM Author
    ORDER BY birth_date DESC
    LIMIT 1
''')
youngest_author = cursor.fetchone()
print("Youngest author:", youngest_author)

# Here I write the authors who don't have any books
cursor.execute('''
    SELECT * FROM Author
    WHERE id NOT IN (SELECT DISTINCT author_id FROM Book)
''')
authors_without_books = cursor.fetchall()
print("Authors without books:", authors_without_books)

# Bonus exercise:
# in this problem I found top 5 authors which have more than 3 books.
cursor.execute('''
    SELECT author_id, COUNT(*) as book_count 
    FROM Book 
    GROUP BY author_id 
    HAVING book_count > 3
    LIMIT 5
''')
authors_with_more_than_3_books = cursor.fetchall()
print("Authors with more than 3 books:", authors_with_more_than_3_books)

# Here I close the connection to database.
conn.close()
