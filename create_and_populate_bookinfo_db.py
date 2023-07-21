# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:43:32 2022

@author: haet9
"""

import sqlite3

# Creates a Database 
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# Create a Table - Authors
cursor.execute("""Create table IF NOT EXISTS Authors(
    Name text PRIMARY KEY,
    Place_of_Birth text NOT NULL);""")

# Creates a Table - Books
cursor.execute("""Create table IF NOT EXISTS Books(
    ID integer PRIMARY KEY,
    Title text NOT NULL,
    Author text NOT NULL,
    Data_Published timestamp NOT NULL);""")

#Saves the changes done into Database
db.commit()

#Creates list of tuples to insert multiple values into Authors Table
#multiple_columns_authors = [('Agatha Christie','Torquay'),
#                    ('J.K. Rowling','Bristol'),
 #                   ('Oscar Wilde','Dublin')]
#cursor.execute("""Delete from Authors""")
#Inserts data into Authors Table
cursor.execute("""INSERT INTO Authors(Name,Place_of_Birth) VALUES('Agatha Christie','Torquay'),
                   ('J.K. Rowling','Bristol'),
                    ('Oscar Wilde','Dublin');""")

db.commit()
#Creates list of tuples to insert multiple values into Books Table
#multiple_columns_books = [(1,'De Profundis','Oscar Wilde',1905),
 #                   (2,'Harry Potter and the chamber of secrets','J.K. Rowling',1998),
  #                  (3,'The seven dials mystery','Agatha Christie',1929),
   #                 (4,'The picture of Dorian Gray','Oscar Wilde',1890),
    #                (5,'Murder on the Orient Express','Agatha Christie',1934),
     #               (6,'Harry Potter and the prisoner of Azkaban','J.K. Rowling',1999)]
#cursor.execute("""Delete from Books""")
#Inserts data into Authors Table
cursor.execute("""INSERT INTO Books(ID,Title,Author,Data_Published) VALUES(1,'De Profundis','Oscar Wilde',1905),
                    (2,'Harry Potter and the chamber of secrets','J.K. Rowling',1998),
                    (3,'The seven dials mystery','Agatha Christie',1929),
                    (4,'The picture of Dorian Gray','Oscar Wilde',1890),
                    (5,'Murder on the Orient Express','Agatha Christie',1934),
                    (6,'Harry Potter and the prisoner of Azkaban','J.K. Rowling',1999);""")

db.commit()

db.close()
