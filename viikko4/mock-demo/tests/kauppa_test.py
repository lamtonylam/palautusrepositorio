import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori


class TestKauppa(unittest.TestCase):
    def setUp(self):
        pass

    def test_kutsutaan_pankki(self):
        pankki_mock = Mock()
        # laitetaan Mock-olio toteuttamaan Viitegeneraattori-luokan metodit
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(5)
        kauppa.lisaa_ostos(5)
        kauppa.maksa("1111")

        pankki_mock.maksa.assert_called()

    def test_kutsutaan_pankkia_oikealla_tilinumerolla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(5)
        kauppa.lisaa_ostos(5)
        kauppa.maksa("1111")

        # katsotaan, että ensimmäisen parametrin arvo on oikea
        pankki_mock.maksa.assert_called_with("1111", ANY, ANY)

    def test_kutsutaan_pankkia_oikealla_tilinumerolla_ja_summalla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(5)
        kauppa.lisaa_ostos(5)
        kauppa.maksa("1111")

        # katsotaan, että ensimmäisen ja toisen parametrin arvo on oikea
        pankki_mock.maksa.assert_called_with("1111", 10, ANY)

    def test_kaytetaan_maksussa_palautettua_viitetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 55
        viitegeneraattori_mock.uusi.return_value = 55

        kauppa = Kauppa(pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(5)
        kauppa.lisaa_ostos(5)
        kauppa.maksa("1111")

        # katsotaan, että kolmannen parametrin arvo on oikea
        pankki_mock.maksa.assert_called_with(ANY, ANY, 55)

    def test_pyydetaan_uusi_viite_jokaiseen_maksuun(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(5)
        kauppa.maksa("1111")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kerran
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(1)
        kauppa.maksa("1234")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kaksi kertaa
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(3)
        kauppa.maksa("4444")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kolme kertaa
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 3)

    def test_kaytetaan_perakkaisten_viitekutsujen_arvoja(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # määritellään että metodi palauttaa ensimmäisellä kutsulla 1, toisella 2 ja kolmannella 3
        viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        kauppa = Kauppa(pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(5)
        kauppa.maksa("1111")

        # varmistetaan, että nyt käytössä ensimmäinen viite
        pankki_mock.maksa.assert_called_with(ANY, ANY, 1)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(1)
        kauppa.maksa("1222")

        # ...toinen viite
        pankki_mock.maksa.assert_called_with(ANY, ANY, 2)

        kauppa.aloita_ostokset()
        kauppa.lisaa_ostos(1)
        kauppa.maksa("4321")

        # ...ja kolmas viite
        pankki_mock.maksa.assert_called_with(ANY, ANY, 3)
