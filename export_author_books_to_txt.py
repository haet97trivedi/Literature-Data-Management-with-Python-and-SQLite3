# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:34:35 2022

@author: haet9
"""

import sqlite3

# Creates a Database
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()


fileName = 'Booklist.txt'

bookFile = open(fileName, "w")

authorName = input("Enter the Author Name")

bookFile.write(str("This file contents the following record(s):\n\n"))
cursor.execute(
    """Select ID, Title, Author, Data_Published from Books where Author = ?""", [authorName])

for record in cursor.fetchall():

    row = ' - '.join(map(str, record))

    bookFile.write(str(row + "\n\n"))


bookFile.close()
