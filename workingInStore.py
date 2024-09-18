from random import randint
from random import randrange
from time import sleep
from os import system

global clear
clear = system('clear||cls')

def customersCash():
    kroner = randrange(0, 100, 1)
    tiere = randrange(0, 100, 10)
    hundre = randrange(0, 1000, 100)
    return kroner, tiere, hundre

def cashCheck(price, kroner, tiere, hundre):
    if kroner + tiere + hundre <= price:
        print("That does unfortunately not work, that is too little money")
        print("Try Again")
        paymentSuccessful = 1
        
    elif kroner + tiere + hundre >= price:
        print("That is too much money, remember to give them the change")
        paymentSuccessful = 2

    elif kroner + tiere + hundre == price:
        print("That is just the right amount of money")
        paymentSuccessful = 3
    return paymentSuccessful

def calculatePrice():
    totalPrice = 0
    priceLookup = {
        "toiletpaper": 40,
        "toothbrush": 40,
        "toothpaste": 40,
        "banana": 28,
        "milk": 23,
        "bread": 50,
        "hot dog": 50,
        "carrot cake": 60,
        "candy": 169,
        "chocolate pancake": 18,
        "chicken drumstick": 17,
        "cigar": 169,
        "fish burger": 300,
    }

    priceLookup_lower = {key.lower(): value for key, value in priceLookup.items()}

    while True:
        product = input("Write the product name (or 'exit' to cancel) > ")

        if product.lower() == "exit":
            print("Purchase cancelled.")
            break
        elif product.lower() == "total":
            print(f"Total Price: {totalPrice}")
            
        elif product.lower() in priceLookup_lower:
            totalPrice += priceLookup_lower[product.lower()]
            print(f"Added {product.lower()}, price: {priceLookup_lower[product.lower()]}")
        else:
            print("Product not found.")

def detVarAlt(price):
    print(price)
    sleep(2)
    answer = input("Are you sure? > ")
    print("Yes/No")
    if answer.lower() == 'Yes':
        print("Fart")
    else:
        print("fis")

calculatePrice()