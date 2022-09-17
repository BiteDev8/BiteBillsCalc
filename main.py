from colorama import Fore, Back, Style, init
import pyfiglet

T = "BiteBillsCalc"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()

def billet5(chiffre):
    total = chiffre / 5
    return total
    
def billet10(chiffre):
    total = chiffre / 10
    return total
    
def billet20(chiffre):
    total = chiffre / 20
    return total
    
def billet50(chiffre):
    total = chiffre / 50
    return total
    
def billet100(chiffre):
    total = chiffre / 100
    return total
    
def billet200(chiffre):
    total = chiffre / 200
    return total

while True:
    print(Fore.GREEN+"")
    chiffre = int(input("entrer some total d'argent :"))
    b5 = int(billet5(chiffre))
    b10 = int(billet10(chiffre))
    b20 = int(billet20(chiffre))
    b50 = int(billet50(chiffre))
    b100 = int(billet100(chiffre))
    b200 = int(billet200(chiffre))

    print(b5,"billets de 5")
    print(b10,"billets de 10")
    print(b20,"billets de 20")
    print(b50,"billets de 50")
    print(b100,"billets de 100")
    print(b200,"billets de 200")
    print(Fore.RED+"alt+f4 or crtl+c for stop")


