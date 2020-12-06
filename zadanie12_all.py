def znizka_R1_R2(lista, do_zaplaty, wariant):
    rabat=0

    if wariant==1:
        if len(lista) > 3:
            rabat=5
            return rabat

        if do_zaplaty >= 500:
            rabat=10
            return rabat

    elif wariant == 2:
        if len(lista) > 3 and do_zaplaty<500:
            rabat=5
            return rabat

        if do_zaplaty >= 500:
            rabat=10
            return rabat

    else: return rabat


def znizka_R3(lista, wariant):
    min_cena=0

    if wariant ==3:
        min_cena=min(i['cena'] for i in lista)
    return min_cena


def znizka_R4(lista,wariant):
    lista_posortowana = sorted(lista, key=lambda k: k['cena'])
    ilosc_sztuk=0
    rabat =0
    j_rabat
    for i in lista_posortowana:
            ilosc_sztuk+=i['ilosc']
            if ilosc_sztuk > 2:
                j_rabat = i['ilosc']//3
                rabat+=i['cena']*j_rabat
                print("Rabat wynosi " + str(rabat))
                ilosc_sztuk=i['ilosc']%3
    return 0


def wartosc_koszyka (lista, wariant):
    suma=0
    licznik=1
    rabat3=0

    for i in lista:
        print(" Nalicz 100% za Produkt: "+str(i['nazwa'])+ ", Wartosc pozycji: " +str(i['cena']*i['ilosc']))
        if licznik%3!=0 or wariant!=4:
            suma+=i['cena']*i['ilosc']
        else:
            print("  Rabat 100% za Produkt: "+str(i['nazwa'])+ ", Wartosc pozycji: -" +str(i['cena']*i['ilosc']))
            rabat3+=i['cena']*i['ilosc']
        licznik+=1

    bonus_proc=znizka_R1_R2(lista, suma,wariant)
    bonus_zl=znizka_R3(lista,wariant)

    print("Wartosc koszyka: " + str(suma))
    suma=(1-bonus_proc*0.01)*suma-bonus_zl
    print(" Znizka: -" + str(bonus_proc) + "%")
    print(" Znizka (1 x najtanszy produkt): -" + str(bonus_zl) + "zl")
    return suma

if __name__ == "__main__":
    koszyk = [{'nazwa': 'ser', 'cena': 2, 'ilosc': 3},
    {'nazwa': 'mleko', 'cena': 3, 'ilosc': 2},
    {'nazwa': 'sliwki', 'cena': 2.5, 'ilosc': 600},
    {'nazwa': 'maka', 'cena': 2.5, 'ilosc':300},
        {'nazwa': 'salata', 'cena': 5, 'ilosc': 3},
        {'nazwa': 'jablka', 'cena': 2.4, 'ilosc': 2},
        {'nazwa': 'sokowirowka', 'cena': 1500, 'ilosc':2}]
    opcja=3

    #Opcja=1 Rabat za > 3 produkty niezaleznie od wartosci koszyka; R1 wazniejsze od R2
    #Opcja=2 Rabat za >3 produkty lub za wartosc koszyka; R2 wazniejsze od R1
    #opcja=3 Rabat na 1 najtanszy produkt
    #opcja=4 Rabat na co 3 produkt

    znizka_R4(koszyk,opcja)
    print("Wyznaczam wartosc koszyka wedug wariantu " + str(opcja))

    print("Wartosc do zaplaty: {:.2f}".format(wartosc_koszyka(koszyk,opcja))+"zl")
