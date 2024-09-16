from random import randint
from random import randrange
from time import sleep

count = 0

def customersCash():
    kroner = randrange(0, 100, 1)
    tiere = randrange(0, 100, 10)
    hundre = randrange(0, 1000, 100)
    return kroner, tiere, hundre

def cashCheck(price, kroner, tiere, hundre):
    if kroner + tiere + hundre <= price:
        print("Det går nok ikke, det er for lite penger")
        print("Prøv igjen")
        paymentSuccessful = 1
        
    elif kroner + tiere + hundre >= price:
        print("Det er for mange penger, husk å gi tilbake overskuddet")
        paymentSuccessful = 2

    elif kroner + tiere + hundre == price:
        print("Det er en perfekt mengde penger")
        paymentSuccessful = 3
    return paymentSuccessful

def products():
    product = input("Hvilke produkt ønsker kunden å kjøpe? > ")
    
    while True:
        price = 0
        if product.lower() == 'dopapir':
            price += 40
            print(price)
        elif product.lower() == 'tannbørste':
            price += 40
        elif product.lower() == 'tannkrem':
            price += 40
        elif product.lower() == 'banan':
            price += 28
        elif product.lower() == 'melk':
            price += 23
        elif product.lower() == 'brød':
            price += 50
        elif product.lower() == 'grillpølse':
            price += 50
        elif product.lower() == 'gulrotkake':
            price += 60
        elif product.lower() == 'det var alt':
            detVarAlt()
        else:
            print("Error, prøv igjen. Stavet du det riktig?")
    return price

def detVarAlt(price):
    print(price)
    sleep(2)
    answer = input("Are you sure? > ")
    print("Yes/No")
    if answer.lower() == 'Yes':
        print("Fart")
    else:
        print("fis")

products()