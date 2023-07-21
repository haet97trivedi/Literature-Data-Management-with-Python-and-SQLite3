# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:13:29 2022

@author: haet9
"""

import sqlite3

# Creates a Database 
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("""Select * from Authors;""")

print(cursor.fetchall())

db.commit()

location = input("Enter the location")
cursor.execute("""Select b.Title, b.Data_Published, b.Author from Authors a inner join Books b on a.Name = b.Author where a.Place_of_birth = ?""",[location])

print(cursor.fetchall())
db.commit()

db.close()