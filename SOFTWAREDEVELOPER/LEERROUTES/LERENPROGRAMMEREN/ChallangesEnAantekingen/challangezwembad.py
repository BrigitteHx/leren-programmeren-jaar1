#challangezwembad

#stap 1:

from functools import total_ordering


lengtezwembad1 = 8 #meter
breedtezwembad1 = 3 #meter
dieptezwembad1 = 1.5 #meter

uitgravenperm3 = 25
afvoerperm3 = 32.50

TotaalGrondAfgevoerdZwembad1 = lengtezwembad1 * breedtezwembad1 * dieptezwembad1
# print(f"{TotaalGrondAfgevoerdZwembad1} m3 grond in totaal. ")

# --- stap 2 

uitgraafkosten = uitgravenperm3 * TotaalGrondAfgevoerdZwembad1
afvoerkosten = afvoerperm3 * TotaalGrondAfgevoerdZwembad1
# totaal = uitgraafkosten + afvoerkosten

# print(f"Offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud: {TotaalGrondAfgevoerdZwembad1} m3)")
# print(f"Uitgraven:          € {uitgraafkosten}")
# print(f"Afvoeren grond:     € {afvoerkosten} ")
# print(f"Totaal:             € {totaal} ")

# --- stap 3

vasteprijsklein = 100
vasteprijsgroot = 250

voorrijkostafstand = int(input("Hoeveel KM moet het worden voor gereden? "))

if voorrijkostafstand < 50 and TotaalGrondAfgevoerdZwembad1 < 20:
    voorijkosten = vasteprijsklein + voorrijkostafstand * 1.25 
elif voorrijkostafstand >= 50 and TotaalGrondAfgevoerdZwembad1 < 20:
    voorijkosten = vasteprijsklein + TotaalGrondAfgevoerdZwembad1 * 1.15
elif voorrijkostafstand < 50 and TotaalGrondAfgevoerdZwembad1 >= 20:
    voorijkosten = vasteprijsgroot * 2.15
elif voorrijkostafstand >= 50 and TotaalGrondAfgevoerdZwembad1 >= 20:
    voorijkosten = vasteprijsgroot * 2.05

totaal = uitgraafkosten + afvoerkosten + voorijkosten

print(f"Offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud: {TotaalGrondAfgevoerdZwembad1} m3)")
print(f"Uitgraven:          € {uitgraafkosten}")
print(f"Afvoeren grond:     € {afvoerkosten} ")
print(f"Voorrijkosten:      € {voorijkosten} ")
print(f"Totaal:             € {totaal} ")



