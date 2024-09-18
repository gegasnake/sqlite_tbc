# Books & Authors SQLite Database

This project demonstrates how to create and manipulate an SQLite3 database using Python. The database consists of two tables: **Author** and **Book**, where each book is linked to an author. The project uses the `Faker` library to generate random data for authors and books, and various SQL queries are used to retrieve and manipulate this data.

## Table of Contents

1. [Requirements](#requirements)
2. [Database Schema](#database-schema)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Features](#features)
6. [Queries](#queries)
7. [License](#license)

## Requirements

- Python 3.x
- SQLite3
- Faker Library

## Database Schema

### Author Table

| Column        | Type     | Description               |
|---------------|----------|---------------------------|
| `id`          | INTEGER  | Primary key               |
| `first_name`  | TEXT     | First name of the author  |
| `last_name`   | TEXT     | Last name of the author   |
| `birth_date`  | DATE     | Date of birth of the author|
| `birth_place` | TEXT     | Place of birth of the author|

### Book Table

| Column         | Type     | Description               |
|----------------|----------|---------------------------|
| `id`           | INTEGER  | Primary key               |
| `title`        | TEXT     | Title of the book         |
| `category`     | TEXT     | Category of the book      |
| `pages`        | INTEGER  | Number of pages           |
| `publish_date` | DATE     | Date of publication       |
| `author_id`    | INTEGER  | Foreign key from Author table|

## Installation

1. Clone the repository or download the script.

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
3. Run the script to generate the database and insert random data:
   ```bash
   python script.py

## Usage
After running the script, the SQLite database books_authors.db will be created, containing two tables: Author and Book. Randomly generated data for 500 authors and 1000 books will be inserted.

The script will also execute several queries, such as:

  Finding the book with the most pages.
  Calculating the average number of pages in books.
  Finding the youngest author.
  Listing authors who haven't written any books.
  Finding 5 authors who have written more than 3 books.
  
## Features
  Randomly generates 500 authors using Faker.
  Randomly generates 1000 books linked to the authors.
  Provides various SQL queries to analyze the data.








