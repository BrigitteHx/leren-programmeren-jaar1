# feestlunch

croissant = float(0.39)
stokbrood = float(2.78)
korting = float(0.50)


totaalcroissant = int(input('Hoeveel croissants wilt u? '))
bedragcroissants = totaalcroissant * croissant

totaalstokbrood = int(input('Hoeveel stokbroden wilt u? '))
bedragstokbrood = totaalstokbrood * stokbrood

totaal = bedragcroissants + bedragstokbrood 

totaalkorting = int(input('Had u nog een kortingsbon?'))
bedragkorting = totaalkorting * korting

eindbedrag = totaal - bedragkorting 

print('De feestlunch kost je bij de bakker', float(eindbedrag),'euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')

