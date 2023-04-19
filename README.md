# Movies & Series Forum


Sovellus pohjautuu kurssimateriaalissa olevaan keskustelusovellukseen. Sovellus on foorumi, jossa voi jakaa ja kysyä katseluvinkkejä elokuviin ja sarjoihin ja yleisesti keskustella elokuvista ja sarjoista. Olisi tarkoitus, että muiden kysymyksiin/ vinkkeihin/ keskustelunaloituksiin voi kommentoida ja tykätä.

## Toimivat ominaisuudet
- Käyttäjä voi luoda käyttäjätilin
- Käyttäjä voi kirjautua sisään
- Käyttäjä voi kirjautua ulos
- Käyttäjä voi kirjoittaa alueella uuden viestin/ ketjun
- Käyttäjä voi selata eri kategorioita ja niiden viestejä
- Käyttäjä voi katsoa ketjun sisältöä
- Käyttäjä voi kommentoida aloitettuun ketjuun/ viestiin
- Käyttäjä voi tykätä toisen ketjun aloituksesta


## Ei toimi vielä/ keskeneräisiä
- Käyttäjä voi tykätä viestistä, mutta tykkäysten määrä ei näy oikein (näkyy kyllä tietokannassa, mutta ei sivulla) (keskeneräinen)
- Käyttäjä voi hakea ketjuja/ viestejä hakusanoilla (ominaisuus ei vielä olemassa)
- Ulkoasu miellyttävämmäksi viimeiseen palautukseen


## Ideoita jatkokehitykseen
- Käyttäjä voi tykätä viestien kommenteista
- Käyttäjä voi vastata suoraan kommenttiin



## Käynnistysohjeet
Sovellus ei ole testattavissa fly.io:ssa.

1. Kloonaa repositorio koneellesi "git clone" ja siirry sen juurikansioon
2. Luo juurikansioon .env-tiedosto ja määritä sen sisällöksi:
```
DATABASE_URL=postgresql:///<user>
SECRET_KEY=<16-merkkinen-salainen-avain>
```
- user = tietokannan nimi, tässä tapauksessa hyvin todennäköisesti käyttäjän tunnus
- Luo salainen avain esimerkiksi komentorivillä näin:
```
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```

3. Aktivoi virtuaaliympäristö komennoilla:
```
python3 -m venv venv
source venv/bin/activate
```
4. Asenna riippuvuudet komennolla:
```
pip install -r requirements.txt
```
5. Määritä tietokannan skeema komennolla:

(jos sovellus ei käynnisty ja tulee virhe tietokannan kanssa, suorita komento uudelleen ja sovelluksen pitäisi toimia oikein)
- Muista avata tietokantayhteys ja pitää se auki sovellusta suoritettaessa
```
psql < schema.sql
```

6. Käynnistä sovellus virtuaaliympäristössä komennolla:
```
flask run
```
