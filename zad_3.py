def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0

wynik = czy_parzysta(5)
if wynik == True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")