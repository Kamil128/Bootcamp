# print(f"Ilosć dni: {1} - ilość minut: {1 * 24 * 60}")
# print(f"Ilosć dni: {2} - ilość minut: {2 * 24 * 60}")
# print(f"Ilosć dni: {13} - ilość minut: {13 * 24 * 60}")

zmienna_testowa = 99.99


def ile_jednostek(dni: int = 1, jednostka: str = 's') -> int:
    """
    Funkcja do obliczenia ilosci jednostek w danej liczbie dni.
    To jest moja pierwsza funkacj
    :param dni: [int] ilość dni
    :param jednostka: [str] 'm' - minuty, 's' - sekundy
    :return: int
    """

    if not isinstance(dni, int):
        print(f"Niepoprawny typ dni: {type(dni)}")
        return 0

    if jednostka == 'm':
        minut = dni * 24 * 60
        print(f"Ilośc dni {dni} = ilość minut: {minut} min")
        return minut
    elif jednostka == 's':
        sekund = dni * 24 * 60 * 60
        print(f"Ilośc dni {dni} = ilość minut: {sekund} sek")
        return sekund
    else:
        print(f"Niepoprawna jednostka")
    return 0


if __name__ == "__main__":
    print(help(ile_jednostek))
    print("#" * 50)

    min10 = ile_jednostek(**{'jednostka': 's', 'dni': 10})
    print(min10)