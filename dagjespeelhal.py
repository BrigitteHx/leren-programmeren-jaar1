# dagjespeelhal

x = ticket = float(7.45)
y = VIPveenmin = 0.37 / 5

totaaltickets = int(input('Totaal Aantal Tickets: '))
bedragtickets = totaaltickets * x
print(bedragtickets)

totaaltijdVIP = int(input('Totale Min in VIP-VR-GameSeat: '))
bedragtijdVIP = totaaltijdVIP * y
print(bedragtijdVIP)

totalekosten = bedragtickets + bedragtijdVIP
print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar', {totalekosten} , 'euro!' )