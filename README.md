<!DOCTYPE html>
<html>
<head>
  
</head>
<body>
  <h1>SQLite Database Creation in Python - BookInfo</h1>
  <p>
    This project consists of Python code that uses SQLite3 to create a simple relational database. SQLite is a C library that provides a lightweight disk-based database, which doesn't require a separate server process, and allows accessing the database using a nonstandard variant of the SQL query language. The project focuses on the creation of a database called <code>BookInfo.db</code>, containing two tables: <code>Authors</code> and <code>Books</code>.
  </p>

  <h2>Features</h2>
  <p>
    The main features of this script are:
  </p>
  <ol>
    <li>Database Creation: The script creates an SQLite database named <code>BookInfo.db</code>.</li>
    <li>Table Creation: It creates two tables, <code>Authors</code> and <code>Books</code>.</li>
    <li>Data Insertion: The script populates the tables with sample data related to authors and books.</li>
  </ol>

  <h2>Tables Information</h2>
  <h3>1. Authors:</h3>
  <ul>
    <li><code>Name</code>: The author's name (Primary Key).</li>
    <li><code>Place_of_Birth</code>: The place of birth of the author.</li>
  </ul>

  <h3>2. Books:</h3>
  <ul>
    <li><code>ID</code>: The unique identifier for a book (Primary Key).</li>
    <li><code>Title</code>: The title of the book.</li>
    <li><code>Author</code>: The name of the author who wrote the book.</li>
    <li><code>Data_Published</code>: The year the book was published.</li>
  </ul>

  <h2>Usage</h2>
  <p>
    This Python script can be executed in any Python environment. It connects to an SQLite database, creates tables if they don't already exist, and then populates these tables with data.
  </p>

  <h2>Dataset</h2>
  <p>
    The script uses the following data for the <code>Authors</code> and <code>Books</code> tables:
  </p>
  <h3>Authors:</h3>
  <ul>
    <li>Agatha Christie, Born in Torquay</li>
    <li>J.K. Rowling, Born in Bristol</li>
    <li>Oscar Wilde, Born in Dublin</li>
  </ul>

  <h3>Books:</h3>
  <ul>
    <li>"De Profundis" by Oscar Wilde, published in 1905</li>
    <li>"Harry Potter and the Chamber of Secrets" by J.K. Rowling, published in 1998</li>
    <li>"The Seven Dials Mystery" by Agatha Christie, published in 1929</li>
    <li>"The Picture of Dorian Gray" by Oscar Wilde, published in 1890</li>
    <li>"Murder on the Orient Express" by Agatha Christie, published in 1934</li>
    <li>"Harry Potter and the Prisoner of Azkaban" by J.K. Rowling, published in 1999</li>
  </ul>

  <h2>Note</h2>
  <ul>
    <li>The <code>PRIMARY KEY</code> constraints are being used to ensure that the <code>ID</code> in <code>Books</code> table and <code>Name</code> in <code>Authors</code> table are unique and not null.</li>

  </ul>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>SQLite3 module in Python</li>
  </ul>
</body>
</html>
