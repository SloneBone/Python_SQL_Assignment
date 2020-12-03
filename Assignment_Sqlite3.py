import sqlite3
import os

conn = sqlite3.connect("Sqlite3.db")
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    conn.commit()
conn.close()


def FindTxtFiles():
    for file in os.listdir("C:/Users/dslon/OneDrive/Documents/GitHub/Python_SQL_Assignment"):
        if file.endswith(".txt"):
            TxtFiles = os.path.join("C:/Users/dslon/OneDrive/Documents/GitHub/Python_SQL_Assignment", file)
            print(TxtFiles)


FindTxtFiles()

conn = sqlite3.connect("Sqlite3.db")
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_fileName) \
            VALUES ('Hello.txt')")
    cur.execute("INSERT INTO tbl_files(col_fileName) \
            VALUES ('World.txt')")
    conn.commit()
conn.close()
    
    


            
        
        

