#Harjoitus 1
from datetime import datetime

#Tarkistetaan nykyinen vuosi
vuosinyt = datetime.now().year

print("Henkilötietotulostaja\n")
print("Syötä henkilötiedot:")
print("------------------------\n")

etunimet = input("Anna etunimet:")
sukunimi = input("Anna sukunimi:")
puhnro = input("Anna puhelinnumerosi:")
email = input("Anna sähköpostiosoitteesi:")
osoite = input("Anna lähiosoitteesi:")
postinumero = input("Anna postinumerosi:")
kaupunki = input("Anna kaupunki:")
maa = input("Anna maa:")
syntymävuosi = int(input("Anna syntymävuosi:"))
print()

print ("KIITOS!\n\n")

print("HENKILÖN TIEDOT")
print("------------------")
print()
print("NIMI:")
print("  "+sukunimi+", "+etunimet)
print("PUH:")
print("  "+puhnro)
print("EMAIL:")
print("  "+email)
print("OSOITE:")
print("  "+osoite)
print("  "+postinumero+" "+kaupunki)
print("  "+maa)
print("IKÄ:")
print("  "+str(vuosinyt-syntymävuosi))








