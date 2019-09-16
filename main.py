from flask import Flask, render_template, request, url_for
import domain
app=Flask(__name__)

@app.route("/", methods=['GET', 'POST']) #ovo je index.html, ovo su rute kuda će što ići kao url OVO JE PRIJAVA
def home(): #def -> definiramo funkciju, funkcija se zove home, : ima samo funkcija

    if request.method=='POST':
        email=request.form['email']
        Lozinka=request.form['Lozinka']
        provjera=domain.prijava_korisnika(email, Lozinka)
        if provjera:
            novost=domain.dohvati_novost()
            return render_template('Novosti.html', novosti=novost, korisnik=provjera)
        else:
            print("Prijava nije uspjela")
    return render_template('index.html')

@app.route("/registracija", methods=['GET','POST']) #iovo je registracija.html
def registracija():

    if request.method=='POST': #elif je else if
        Ime=request.form['Ime']
        Prezime=request.form['Prezime']
        email=request.form['email']
        Lozinka=request.form['Lozinka']
        Grad_studiranja=request.form['Grad_studiranja']
        Fakultet=request.form['Fakultet']
        provjera=domain.registracija_korisnika(Ime, Prezime, email, Lozinka, Grad_studiranja, Fakultet)
        if provjera: #ako je provijera TURE onda če mi vratiti ovaj tamplate, index
            return render_template('index.html')
        else:
            print("Registracija nije uspjela")
    return render_template('Registracija.html')


@app.route("/dodaj_novost/<ID>", methods=['GET', 'POST', 'PUT']) #ovo je dodaj_novost.html
def dodaj_novost(ID):
    korisnik=domain.odaberi_korisnika(ID)
    if request.method=='POST':
        Datum=request.form['Datum']
        Naziv=request.form['Naziv']
        Obavjest=request.form['Obavjest']
        provjera=domain.dodaj_novost(Datum, Naziv, Obavjest)
        if provjera: #ako je provijera TURE onda če mi vratiti ovaj tamplate, index
            novost=domain.dohvati_novost()
            return render_template('Novosti.html', novosti=novost, korisnik=korisnik)
        else:
            print("Dodavanje novost nije uspjelo")

    return render_template('Dodaj_novost.html', ID=korisnik[0])

@app.route("/uredi_korisnika/<ID>", methods=['GET', 'POST']) #ovo je uredi_korisnika.html
def uredi_korisnika(ID):
    print('method: ', request.method)
    if request.method=='GET':
        korisnik=domain.odaberi_korisnika(ID)
        return render_template('Uredi_korisnika.html', korisnik=korisnik)
    elif request.method=='POST':
        print('Ovdje')
        Ime=request.form['Ime']
        Prezime=request.form['Prezime']
        Lozinka=request.form['Lozinka']
        Grad_studiranja=request.form['Grad_studiranja']
        Fakultet=request.form['Fakultet']
        domain.uredi_korisnika(Ime, Prezime, Lozinka, Grad_studiranja, Fakultet, ID)
        novost=domain.dohvati_novost()
        korisnik=domain.odaberi_korisnika(ID)
        return render_template('Novosti.html', novosti=novost, korisnik=korisnik)

@app.route("/izbrisi_novost/<ID>", methods=['POST'])
def izbrisi_novost(ID):
    print('Ovdje')
    if request.method=='POST':
        id=request.form["ID"]
        domain.izbrisi_novost(id)
        novost=domain.dohvati_novost()
        korisnik=domain.odaberi_korisnika(ID)
        return render_template('Novosti.html', novosti=novost, korisnik=korisnik)


if __name__ == '__main__':
    app.run(debug = True)
