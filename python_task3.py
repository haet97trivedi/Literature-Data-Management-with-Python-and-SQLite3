# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:23:20 2022

@author: haet9
"""

import sqlite3

# Creates a Database 
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    
year = input("Enter the year")

cursor.execute("""Select Title from Books where Data_Published > ? order by Data_Published;""",[year])

print(cursor.fetchall())

db.commit()

db.close()