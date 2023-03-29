# Movies & Series Forum


Sovellus pohjautuu kurssimateriaalissa olevaan keskustelusovellukseen. Sovellus on foorumi, jossa voi jakaa ja kysyä katseluvinkkejä elokuviin ja sarjoihin ja yleisesti keskustella elokuvista ja sarjoista. Olisi tarkoitus, että muiden kysymyksiin/ vinkkeihin/ keskustelunaloituksiin voi kommentoida ja tykätä.

## Toimivat ominaisuudet
- Käyttäjä voi luoda käyttäjätilin
- Käyttäjä voi kirjautua sisään
- Käyttäjä voi kirjautua ulos
- Käyttäjä näkee kaikki julkaistut viestit, jos sellaisia on
- Käyttäjä voi kirjoittaa alueella uuden viestin/ ketjun


## Mahdollisia ominaisuuksia
- Käyttäjä voi luoda käyttäjätilin
- Käyttääjä voi kirjautua sisään ja ulos
- Käyttäjä voi kirjoittaa alueelle uuden viestin/ ketjun
- Käyttäjä voi selata kategorioita
- Käyttäjä voi selata ketjujen sisältöjä
- Käyttäjä voi kommentoida jonkun toisen aloittamaan ketjuun/ viestiin
- Käyttäjä voi tykätä toisen vinkistä/ viestistä
- Käyttäjä voi hakea ketjuja/ viestejä hakusanoilla


## Käynnistysohjeet
Sovellus ei ole testattavissa fly.io:ssa.

1. Kloonaa repositorio koneellesi "git clone" ja siirry sen juurikansioon
2. Luo juurikansioon .env-tiedosto ja määritä sen sisällöksi:
```
DATABASE_URL=postgresql:///<user>
SECRET_KEY=<16-merkkinen-salainen-avain>
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
```
psql < schema.sql
```
6. Käynnistä sovellus virtuaaliympäristössä komennolla:
```
flask run
```
