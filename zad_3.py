print("\nc zadanie")


def liczby_parzyste(liczby):
    for liczb in liczby:
        if liczb % 2 == 0:
            print(liczb)


parzyste_lista = list(range(10))
liczby_parzyste(parzyste_lista)
