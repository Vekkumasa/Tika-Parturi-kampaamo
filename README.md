Kyseessä on tietokantasovellus parturi-kampaamolle (mahdollisesti ketjulle).
Asiakas voi tehdä ajanvarauksen kenelle tahansa kampaajista heidän vapaista ajoista
(mihin vain toimipisteeseen.)
Kampaajilla on eri palveluita esim leikkaus tai värjäys.
Asiakas voi itse tehdä varauksen, tarkistaa oman varauksen ajan, muuttaa varauksen
ajankohtaa tai poistaa eli täysi CRUD toiminnallisuus.
Asiakkaalla voi olla monta varausta ja jokaiseen varaukseen liittyy yksi asiakas.
Kampaajilla on monta varausta ja varaukseen liittyy yksi kampaaja.
Ketjulla on monta kampaajaa ja jokainen kampaaja voi toimia missä vain toimipisteessä.

[Linkki herokuun](https://parturi-kampaamo20.herokuapp.com/)

[Linkki tietokantakaavioon](https://github.com/Vekkumasa/Tika-Parturi-kampaamo/blob/master/documentation/tietokantakaavio.jpg)

[Linkki käyttötapauksiin](https://github.com/Vekkumasa/Tika-Parturi-kampaamo/blob/master/documentation/k%C3%A4ytt%C3%B6tapaukset.md)

Herokussa on tunnukset "Hello world" username: "hello" password "world"

Varauksille täysi crud toiminnallisuus toteutettu MUTTA vaatii paljon viilausta. Täytyy operoida käyttäen pelkästään
tarvittavia id:tä käyttäen.

Varaukset muutetaan ja poistetaan kirjautumalla sisään valikosta omat varaukset -> valitsee varauksen ja joko poistaa
tai muokkaa varausta
