#Harjoitus 2

print(f"{"* "*18}")
print(f"{"*":10}Valuuttamuunnin{"*":>10}")
print(f"{"* "*18}")

dollarinkurssi = float(input("Anna dollarin kurssi euroina: "))
rahanmääräeur = float(input("Anna rahanmäärä euroina: "))
rahanarvodollareina = rahanmääräeur / dollarinkurssi
print(f"Rahan arvo dollareina on: {rahanarvodollareina:.2f}")
print(f"{"* "*18}")
