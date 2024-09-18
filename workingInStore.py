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
        "toiletPaper": 40,
        "toothBrush": 40,
        "toothPaste": 40,
        "banana": 28,
        "milk": 23,
        "bread": 50,
        "hotDog": 50,
        "carrotCake": 60,
        "candy": 169,
        "pancakeWithChocolate": 18,
        "chickenDrumstick": 17,
        "cigar": 169,
        "fishBurger": 300,
    }

    while True:
        product = input("Write the product name (or 'exit' to cancel) > ")

        if product == "exit":
            print("Purchase cancelled.")
            break
        elif product == "calculate":
            print(f"Total Price: {totalPrice}")
            break
        elif product in priceLookup:
            totalPrice += priceLookup[product]
            print(f"Added {product}, price: {priceLookup[product]}")
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