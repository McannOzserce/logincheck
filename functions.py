
import sqlite3

con = sqlite3.connect("dersler.db")
cursor = con.cursor()



def ogrencitablosu():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT,numara INT,ogrencinotu INT)")
    con.commit()

def createuserstable():
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT,sifre TEXT)")
    con.commit()
    
def ogrenciekle(ad,soyad,numara,ogrencinotu):
    cursor.execute("INSERT INTO ogrenciler (ad,soyad,numara,ogrencinotu) VALUES (?,?,?,?)",(ad,soyad,numara,ogrencinotu))
    con.commit()
   
def ogrencibul(ogrencinumarası):
    cursor.execute("SELECT * FROM ogrenciler WHERE numara = ? ", (ogrencinumarası,))
    data = cursor.fetchall()
    con.commit()
    
def kullanicikontrol(kullaniciadi,sifre):
    cursor.execute("SELECT * FROM users WHERE username = ? AND sifre = ? ", (kullaniciadi,sifre,))
    data = cursor.fetchall()
    con.commit()
    
    if data != []  :
        return(1)
    else :
        return(0)

def kayitkontrol(kullaniciadi,sifre):
    cursor.execute("SELECT * FROM users WHERE username = ?", (kullaniciadi,))
    data = cursor.fetchall()
    con.commit()
    
    if data != []  :
        return(1)
    else :
        return(0)
         
def userekle(kullaniciadi,sifre):
    cursor.execute("INSERT INTO users (username,sifre) VALUES (?,?)",(kullaniciadi,sifre))
    con.commit()
    
