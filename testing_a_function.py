import os

def FindTxtFiles():
    for file in os.listdir("C:/Users/dslon/OneDrive/Documents/GitHub/Python_SQL_Assignment"):
        if file.endswith(".txt"):
            TxtFiles = os.path.join("C:/Users/dslon/OneDrive/Documents/GitHub/Python_SQL_Assignment", file)
            print(TxtFiles)


FindTxtFiles()
