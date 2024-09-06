import os
from time import sleep

def gameOver():
    print("Wow yea, you really died")
    input("Press Enter to continue...") 
    os.system('clear||cls')
    print("Game over")
    decision = input("Do you want to play again? (Yes/No) > ")
    if decision.lower() == 'yes':
        beginning()
    else: 
        quit()

def beginning():
    global karma
    karma = 1000

    os.system('clear||cls')
    print("You come back to your senses and continue your speech")
    sleep(5)
    print("Suddenly you see a weird glare in the distance and your bodyguard yelling")
    sleep(3)
    print("GET DOWN!")
    toDodgeOrNoToDodge()

def toDodgeOrNoToDodge():
    sleep(5)
    print("Do you get down?")
    answer = input("Yes/No > ")

    if answer.lower() in ['no']:
        sleep(2)
        print("You suddenly hear a shot in the distance and it all goes black.")
        sleep(7)
        os.system('clear||cls')
        gameOver()
        
    else:
        sleep(2)
        print("You dodged the bullet")
        sleep(2)
        print("but barely")
        sleep(5)
        input("Press Enter to continue...") 
        theAftermath()

def theAftermath():
    global karma  
    os.system('clear||cls')
    print("You get crowded by bodyguards using themselves as protection and making sure you get to the ground")
    sleep(7)
    print("the bullet was millimeters away from hitting you")
    input("Press Enter to continue...") 
    os.system('clear||cls')

    print("The highest ranking member of the secret services present at the scene")
    print("tells you that they have a shot on the shooter, it is your call as to whether they shoot or arrest him")
    sleep(14)
    print("i want you to ---- him")
    answer = input("Cuff/Shoot > ")
    if answer.lower() == 'shoot':
        karma -= 100
        theShot()
    else:
        karma += 35
        theArrest() 

def theArrest():
    global karma 
    print("arrest")
    print(karma)

def theShot():
    global karma  
    print("shoot")
    print(karma)

beginning()