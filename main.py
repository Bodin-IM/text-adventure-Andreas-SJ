import random
from shoppingVariables import priceLookup, customerList, inventory, welcomeMessages

points = 0
restock_items = []
special_items = {"bonus_card": False, "manager_approval": False}

def print_commands(commands):
    print("\nCommands:")
    for command in commands:
        print(f"- {command}")

def get_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print("Invalid input, please try again.")

def interact_with_customer(customer):
    print(f"\nA customer named {customer} approaches the cashier.")
    
    print(f"{customer}: 'Hi, how's your day going?'")
    
    print_commands(["good", "bad", "small talk", "stay silent"])
    response = get_input("How would you like to respond? ", ["good", "bad", "small talk", "stay silent"])

    if response == "good":
        print(f"You: 'It's going well! How about yours?'")
        print(f"{customer}: 'Glad to hear! I'm just doing some quick shopping.'")
    elif response == "bad":
        print(f"You: 'Not the best day, but it is what it is.'")
        print(f"{customer}: 'Sorry to hear that, hope it gets better.'")
    elif response == "small talk":
        print(f"You: 'Busy day, huh?'")
        print(f"{customer}: 'Yeah, this store is always packed around this time.'")
    elif response == "stay silent":
        print(f"You stay silent, and {customer} awkwardly proceeds to unload their cart.")

    print(f"{customer} starts unloading their cart for you to scan.")
    return True

def scan_customer():
    global points
    customer = random.choice(customerList)
    
    if interact_with_customer(customer):
        cart = random.sample(list(priceLookup.keys()), random.randint(1, 4))
        total = 0
        restock_needed = False

        print(f"{customer} has the following items in their cart:")
        for item in cart:
            if inventory[item] > 0:
                inventory[item] -= 1
                price = priceLookup[item]
                total += price
                print(f"- {item.capitalize()} (${price})")
            else:
                print(f"- {item.capitalize()} (Out of stock)")
                restock_needed = True

        if restock_needed:
            print("Some items are out of stock! Would you like to restock first?")
            choice = get_input("Type 'yes' to restock or 'no' to continue: ", ["yes", "no"])
            if choice == "yes":
                restock()

        print(f"Total for {customer}: ${total:.2f}")
        points += total

def restock():
    global restock_items
    print("\nTime to restock!")
    available_items = list(priceLookup.keys())
    
    print(f"Your current restock inventory: {restock_items}")
    print("Available items to restock:")
    for i, item in enumerate(available_items, 1):
        print(f"{i}. {item.capitalize()}")

    choice = get_input("Choose an item to restock (enter number): ", [str(i) for i in range(1, len(available_items) + 1)])
    restocked_item = available_items[int(choice) - 1]
    inventory[restocked_item] += 5
    restock_items.append(restocked_item)
    print(f"Restocked 5 units of {restocked_item.capitalize()}!")

def break_room():
    global special_items
    print("\nYou enter the break room. You can relax or take a bonus card.")
    print_commands(["relax", "take bonus card", "leave"])
    choice = get_input("What would you like to do? ", ["relax", "take bonus card", "leave"])

    if choice == "relax":
        print("You take a moment to relax and regain your energy!")
    elif choice == "take bonus card":
        special_items["bonus_card"] = True
        print("You have taken the bonus card. It will boost your points on your next sale!")
    elif choice == "leave":
        print("Leaving the break room.")

def stockroom():
    print("\nYou enter the stockroom. Time to restock items!")
    restock()

def play_day():
    print(welcomeMessages)
    day_done = False
    while not day_done:
        print_commands(["scan", "restock", "inventory", "break room", "end day"])
        action = get_input("What would you like to do? ", ["scan", "restock", "inventory", "break room", "end day"])

        if action == "scan":
            scan_customer()
        elif action == "restock":
            stockroom()
        elif action == "inventory":
            print("\nCurrent inventory:")
            for item, qty in inventory.items():
                print(f"{item.capitalize()}: {qty}")
        elif action == "break room":
            break_room()
        elif action == "end day":
            print(f"Ending the day. You earned {points:.2f} points today!")
            day_done = True

def play_store():
    print("\nWelcome to the Grocery Store!")
    day = 1
    max_days = 7

    while day <= max_days:
        print(f"\n--- Day {day} ---")
        play_day()

        if day != max_days:
            print(f"\nEnd of Day {day}. Get ready for Day {day + 1}!")
        else:
            print(f"\nYou finished 7 days at the grocery store. Total points earned: {points:.2f}")

        day += 1

play_store()