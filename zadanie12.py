def znizka(lista, do_zaplaty):
    rabat=0

#Jesli R1 to nie R2
    if len(lista) > 3 and do_zaplaty<500:
        rabat=5
        return rabat

    if do_zaplaty >= 500:
        rabat=10
        return rabat

def wartosc_koszyka (lista):
    suma=0

    for i in lista:
        suma+=i['cena']*i['ilosc']

    bonus=znizka(lista, suma)

    min_cena=min(i['cena'] for i in koszyk)
    print('Wartosc koszyka obnizona o cene najtanszego produktu (-' + str(min_cena) + ")")
    suma-=min_cena

    suma=(1-bonus*0.01)*suma
    print("Znizka wynosi " + str(bonus) + "%")

    return suma

koszyk = [{'nazwa': 'ser', 'cena': 2, 'ilosc': 1},
{'nazwa': 'mleko', 'cena': 3, 'ilosc': 2},
{'nazwa': 'sliwki', 'cena': 2.5, 'ilosc': 600},
{'nazwa': 'maka', 'cena': 2.5, 'ilosc':300}]


print("Wartosc do zaplaty wynosi {:.2f}".format(wartosc_koszyka(koszyk))+"zl")
