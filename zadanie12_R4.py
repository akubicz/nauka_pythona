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
    licznik=1

    for i in lista:
        if licznik%3!=0:
            suma+=i['cena']*i['ilosc']
            print("Produkt: "+str(i['nazwa'])+ ", Wartosc: " +str(i['cena']*i['ilosc']))
        licznik+=1

    bonus=znizka(lista, suma)

    print("Wartosc koszyka: " + str(suma))
    suma=(1-bonus*0.01)*suma
    print("Znizka: -" + str(bonus) + "%")

    return suma

koszyk = [{'nazwa': 'ser', 'cena': 2, 'ilosc': 1},
{'nazwa': 'mleko', 'cena': 3, 'ilosc': 2},
{'nazwa': 'sliwki', 'cena': 2.5, 'ilosc': 600},
{'nazwa': 'maka', 'cena': 2.5, 'ilosc':300}]


print("Wartosc do zaplaty: {:.2f}".format(wartosc_koszyka(koszyk))+"zl")
