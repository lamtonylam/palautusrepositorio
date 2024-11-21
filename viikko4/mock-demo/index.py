from pankki import Pankki
from viitegeneraattori import Viitegeneraattori
from kauppa import Kauppa


def main():
    my_net_bank = Pankki()
    viitteet = Viitegeneraattori()
    kumpula_bier_shop = Kauppa(my_net_bank, viitteet)

    kumpula_bier_shop.aloita_ostokset()
    kumpula_bier_shop.lisaa_ostos(10)
    kumpula_bier_shop.lisaa_ostos(7)
    kumpula_bier_shop.maksa("1234-1234")

    kumpula_bier_shop.aloita_ostokset()
    kumpula_bier_shop.lisaa_ostos(1)
    kumpula_bier_shop.lisaa_ostos(1)
    kumpula_bier_shop.lisaa_ostos(2)
    kumpula_bier_shop.lisaa_ostos(2)
    kumpula_bier_shop.maksa("4444-1111")


if __name__ == "__main__":
    main()
