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
print('Totale Kosten: ', totalekosten )