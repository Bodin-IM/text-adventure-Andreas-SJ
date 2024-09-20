from random import randint
from random import randrange
from shoppingVariables import priceLookup
from shoppingVariables import randomWelcomeMessages
from shoppingVariables import randomCustomer
from time import sleep
from os import system

global clear
clear = system('clear||cls')

def customersCash():
    kroner = randrange(0, 100, 1)
    tiere = randrange(0, 100, 10)
    hundre = randrange(0, 1000, 100)
    money = kroner + tiere + hundre
    return money

def cashCheck(money, price):
    if money <= price:
        print("That does unfortunately not work, that is too little money")
        print("Try Again")
        paymentSuccessful = 1
        
    elif money >= price:
        print("That is too much money, remember to give them the change")
        paymentSuccessful = 2

    elif money == price:
        print("That is just the right amount of money")
        paymentSuccessful = 3
    return paymentSuccessful

def calculatePrice(priceLookup):
    totalPrice = 0
    priceLookupLower = {key.lower(): value for key, value in priceLookup.items()}

    while True:
        product = input("Write the product name (or 'exit' to cancel) > ")

        if product.lower() == "exit":
            print("Purchase cancelled.")
            break
        elif product.lower() == "total":
            print(f"Total Price: {totalPrice}")
            
        elif product.lower() in priceLookupLower:
            totalPrice += priceLookupLower[product.lower()]
            print(f"Added {product.lower()}, price: {priceLookupLower[product.lower()]}")
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

def aNewBeginning(randomWelcomeMessages):
    sleep(3)
    print("Welcome to your frist day here with us! We at Joja Mart can't wait to work with you!")
    sleep(2)
    print("Start by walking into the store")
    sleep(2)
    print("\033[1;32;40m Do you walk into the store? \n")
    decision = input("\033[1;32;40m Yes/No > \n")
    if decision.lower() == "yes":
        print("\033[1;37;40m \n")
        theFirstDay(randomWelcomeMessages)

def theFirstDay(randomWelcomeMessages):
    print(randomWelcomeMessages)
    sleep(2)
    print(f"You get behind the cashier as the first customer {randomCustomer} approaches you")

aNewBeginning(randomWelcomeMessages)