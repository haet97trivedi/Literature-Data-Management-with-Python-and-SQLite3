SQLite Database Creation in Python - BookInfo
This project consists of Python code that uses SQLite3 to create a simple relational database. SQLite is a C library that provides a lightweight disk-based database, which doesn't require a separate server process, and allows accessing the database using a nonstandard variant of the SQL query language. The project focuses on the creation of a database called BookInfo.db, containing two tables: Authors and Books.

Features
The main features of this script are:

Database Creation: The script creates an SQLite database named BookInfo.db.
Table Creation: It creates two tables, Authors and Books.
Data Insertion: The script populates the tables with sample data related to authors and books.
Tables Information
Authors:

Name: The author's name (Primary Key).
Place_of_Birth: The place of birth of the author.
Books:

ID: The unique identifier for a book (Primary Key).
Title: The title of the book.
Author: The name of the author who wrote the book.
Data_Published: The year the book was published.
Usage
This Python script can be executed in any Python environment. It connects to an SQLite database, creates tables if they don't already exist, and then populates these tables with data.

Sample Data
The script uses the following data for the Authors and Books tables:

Authors:

Agatha Christie, Born in Torquay
J.K. Rowling, Born in Bristol
Oscar Wilde, Born in Dublin
Books:

"De Profundis" by Oscar Wilde, published in 1905
"Harry Potter and the Chamber of Secrets" by J.K. Rowling, published in 1998
"The Seven Dials Mystery" by Agatha Christie, published in 1929
"The Picture of Dorian Gray" by Oscar Wilde, published in 1890
"Murder on the Orient Express" by Agatha Christie, published in 1934
"Harry Potter and the Prisoner of Azkaban" by J.K. Rowling, published in 1999
Note
The PRIMARY KEY constraints are being used to ensure that the ID in Books table and Name in Authors table are unique and not null.
This script doesn't handle exceptions. In a production environment, you should handle potential errors, such as issues with connecting to the database or executing SQL.
This script is an example of how to work with SQLite databases in Python, and its functionality is basic. For more complex scenarios, you would need to modify this script or use more advanced tools or libraries.
Requirements
Python 3.x
SQLite3 module in Python
