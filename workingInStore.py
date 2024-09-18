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
        "paprika": 70,
        "apple": 15,
        "orange": 20,
        "grapes": 35,
        "watermelon": 45,
        "pineapple": 50,
        "strawberries": 60,
        "blueberries": 70,
        "raspberries": 80,
        "blackberries": 90,
        "kiwi": 25,
        "mango": 30,
        "peach": 35,
        "plum": 40,
        "pear": 45,
        "nectarine": 50,
        "apricot": 55,
        "cherries": 60,
        "fig": 65,
        "pomegranate": 70,
        "avocado": 75,
        "lemon": 20,
        "lime": 25,
        "cucumber": 30,
        "tomato": 35,
        "lettuce": 40,
        "spinach": 45,
        "kale": 50,
        "broccoli": 55,
        "cauliflower": 60,
        "zucchini": 65,
        "eggplant": 70,
        "bell pepper": 75,
        "jalapeno": 80,
        "habanero": 85,
        "potato": 90,
        "sweet potato": 95,
        "onion": 100,
        "garlic": 105,
        "ginger": 110,
        "carrot": 115,
        "celery": 120,
        "radish": 125,
        "beet": 130,
        "turnip": 135,
        "parsnip": 140,
        "rutabaga": 145,
        "butternut squash": 150,
        "acorn squash": 155,
        "spaghetti squash": 160,
        "pumpkin": 165,
        "corn": 30,
        "peas": 25,
        "green beans": 35,
        "asparagus": 40,
        "brussels sprouts": 45,
        "artichoke": 50,
        "mushroom": 55,
        "cabbage": 20,
        "bok choy": 25,
        "collard greens": 30,
        "mustard greens": 35,
        "swiss chard": 40,
        "arugula": 45,
        "endive": 50,
        "radicchio": 55,
        "watercress": 60,
        "alfalfa sprouts": 20,
        "bean sprouts": 25,
        "snow peas": 30,
        "snap peas": 35,
        "okra": 40,
        "egg": 10,
        "cheese": 50,
        "yogurt": 20,
        "butter": 30,
        "cream": 25,
        "sour cream": 30,
        "cottage cheese": 35,
        "cream cheese": 40,
        "milkshake": 45,
        "ice cream": 50,
        "frozen yogurt": 55,
        "gelato": 60,
        "sorbet": 65,
        "popsicle": 10,
        "frozen pizza": 70,
        "frozen vegetables": 30,
        "frozen fruit": 35,
        "frozen dinners": 80,
        "frozen waffles": 25,
        "frozen pancakes": 20,
        "frozen french fries": 30,
        "frozen chicken nuggets": 40,
    }

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

calculatePrice()