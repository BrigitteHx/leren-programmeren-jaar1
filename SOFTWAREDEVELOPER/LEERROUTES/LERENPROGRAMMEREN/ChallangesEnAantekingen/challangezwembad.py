#challangezwembad

#stap 1:

lengtezwembad1 = 8 #meter
breedtezwembad1 = 3 #meter
dieptezwembad1 = 1.5 #meter

uitgravenperm3 = 25
afvoerperm3 = 32.50

TotaalGrondAfgevoerdZwembad1 = lengtezwembad1 * breedtezwembad1 * dieptezwembad1
# print(f"{TotaalGrondAfgevoerdZwembad1} m3 grond in totaal. ")

uitgraafkosten = uitgravenperm3 * TotaalGrondAfgevoerdZwembad1
afvoerkosten = afvoerperm3 * TotaalGrondAfgevoerdZwembad1
totaal = uitgraafkosten + afvoerkosten

print(f"Offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud: {TotaalGrondAfgevoerdZwembad1} m3)")
print(f"Uitgraven:          € {uitgraafkosten}")
print(f"Afvoeren grond:     € {afvoerkosten} ")
print(f"Totaal:             € {totaal} ")

