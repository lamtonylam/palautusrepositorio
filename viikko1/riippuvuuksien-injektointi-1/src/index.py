from konsoli_io import KonsoliIO
from laskin import Laskin


def main():
    io = KonsoliIO()
    laskin = Laskin(io)

    laskin.suorita()


if __name__ == "__main__":
    main()
