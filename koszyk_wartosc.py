def koszyk_wartosc(koszyk, rodzaj_operacji):
    netto=0
    brutto=0

    if rodzaj_operacji == 'netto':
        for i in koszyk:
            netto+=i['cena']*i['ilosc']
        return netto

    if rodzaj_operacji == 'brutto':
        return 1.23*koszyk_wartosc(koszyk,"netto")
