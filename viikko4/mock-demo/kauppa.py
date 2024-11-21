class Kauppa:
    def __init__(self, pankki, viitegeneraattori):
        self._pankki = pankki
        self._viitegeneraattori = viitegeneraattori
        self._yhteishinta = 0

    def aloita_ostokset(self):
        self._yhteishinta = 0

    def lisaa_ostos(self, hinta):
        self._yhteishinta = self._yhteishinta + hinta

    def maksa(self, tilinumero):
        self._pankki.maksa(
            tilinumero,
            self._yhteishinta,
            self._viitegeneraattori.uusi()
        )
