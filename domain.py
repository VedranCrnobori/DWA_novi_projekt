#ovo je za operacije nad bazom
import sqlite3
from uuid import uuid4 #ovo je biblioteka za ID ključeve

def povezivanje():
    try:
        conn=sqlite3.connect("baza_dwa.db")
        return conn
    except Exception as e:
        return None

def registracija_korisnika(Ime, Prezime, email, Lozinka, Grad_studiranja, Fakultet): #spremanje korisnika
    konekcija=povezivanje()
    kursor=konekcija.cursor()
    ID=uuid4().hex
    kursor.execute("INSERT INTO Korisnik VALUES (?, ?, ?, ?, ?, ?, ?)",(ID, Ime, Prezime, email, Lozinka, Grad_studiranja, Fakultet))
    konekcija.commit()
    return True

def prijava_korisnika(email, Lozinka):
    konekcija=povezivanje()
    kursor=konekcija.cursor()
    kursor.execute("SELECT * FROM Korisnik WHERE email = ? AND Lozinka = ?",(email, Lozinka)) # *-> all
    korisnik=kursor.fetchone()
    return korisnik

def odaberi_korisnika(ID):
    konekcija=povezivanje()
    kursor=konekcija.cursor()
    kursor.execute("SELECT * FROM Korisnik WHERE ID=?", (ID,))
    korisnik=kursor.fetchone()
    return korisnik


def uredi_korisnika(Ime, Prezime, Lozinka, Grad_studiranja, Fakultet, ID): #uređenje postojećeg korisnika, PARAMETRI FUNKCIJE
    konekcija=povezivanje()
    kursor=konekcija.cursor()
    kursor.execute("UPDATE Korisnik SET Ime = ?, Prezime = ?, Lozinka = ?, Grad_studiranja = ?, Fakultet = ? WHERE ID = ?",(Ime, Prezime, Lozinka, Grad_studiranja, Fakultet, ID)) #? -> PRIMLJENO KAO PARAMETAR, KOJI SE NALAZI U ZAGRADI DESNO
    konekcija.commit()

def dodaj_novost(Datum, Naziv, Obavjest): #spremanje novih obavjesti
    konekcija=povezivanje()
    kursor=konekcija.cursor()
    ID=uuid4().hex
    kursor.execute("INSERT INTO Novosti VALUES (?, ?, ?, ?)",(ID, Datum, Naziv, Obavjest))
    konekcija.commit()
    return True

def dohvati_novost(): #nije potreban parametar jer će dohvatiti sve što je spremljeno u tablici
    konekcija=povezivanje()
    kursor=konekcija.cursor()
    kursor.execute("SELECT * FROM Novosti") # *-> all
    novosti=kursor.fetchall()
    print (novosti)
    return novosti
