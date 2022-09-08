# feestlunch

croissant = 39
stokbrood = 278
korting = 50

totaalcroissant = int(input('Hoeveel croissants wilt u? '))
bedragcroissants = totaalcroissant * croissant

totaalstokbrood = int(input('Hoeveel stokbroden wilt u? '))
bedragstokbrood = totaalstokbrood * stokbrood

totaal = bedragcroissants + bedragstokbrood 

totaalkorting = int(input('Hoeveel kortingsbonnen heeft u?'))
bedragkorting = totaalkorting * korting

eindbedrag = totaal - bedragkorting 

print('De feestlunch kost je bij de bakker', eindbedrag,'cent voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')

