
import sqlite3

con = sqlite3.connect("dersler.db") #You have to write here your database name.
cursor = con.cursor() 


def createuserstable():
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT,sifre TEXT)") #Create your new table to your database.
    con.commit()
         
def usercheck(username,password): #This function checks whether there is such a user registered in the database.
    cursor.execute("SELECT * FROM users WHERE username = ? AND sifre = ? ", (username,password,)) #Database Select function for find user.
    data = cursor.fetchall()
    con.commit()
    
    if data != []  :    #This İF post value to logincheck for the user found.
        return(1)
    else :
        return(0)

def registercheck(username):    #This function operate when unregistered user trying to register and cant registering with already existed username.
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = cursor.fetchall()
    con.commit()
    
    if data != []  : #This İF post value to logincheck for already existed usernames.
        return(1)
    else :
        return(0)
         
def useradd(username,password):  #This is for append new user to database.
    cursor.execute("INSERT INTO users (username,sifre) VALUES (?,?)",(username,password))
    con.commit()
    
