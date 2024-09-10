from os import system
from time import sleep

def gameOver():
    print("Wow yea, you really died")
    input("Press Enter to continue...") 
    system('clear||cls')
    print("Game over")
    decision = input("Do you want to play again? (Yes/No) > ")
    if decision.lower() == 'yes':
        beginning()
    else: 
        quit()

def beginning():
    global karma
    karma = 1000

    system('clear||cls')
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
        system('clear||cls')
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
    system('clear||cls')
    print("You get crowded by bodyguards using themselves as protection and making sure you get to the ground")
    sleep(7)
    print("the bullet was millimeters away from hitting you")
    input("Press Enter to continue...") 
    system('clear||cls')

    print("*you have been escorted to the back of the stage*")
    print("The highest ranking member of the secret services present at the scene tells you that they have a shot on the shooter")
    print("it is your call as to whether they shoot or arrest him")
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
    print("arrest")
    postArrest()

def theShot():
    print("shoot")
    postShot()

def postShot():
    global karma
    print("WTF man? I know he tried to assassinate you but wouldn't it be more satisfying to let him rot in jail?")
    sleep(8)
    print("1: Nah, he had it coming")
    print("2: Good point")
    input("> ")
    if input == 1:
        karma -= 200
    else:
        print("at least you show some remorse..")
    secretServiceConversation()
     
def postArrest():
    print("Good call")
    sleep(3)
    print("Now he will at least serve for his crimes")
    input("Press Enter to continue...")
    secretServiceConversation()

def secretServiceConversation():
    print("*you are back at the white house*")
    print("SS agent Nolan:")
    print("     I have to inform you that after a stunt like the one you just came back from")
    sleep(7)
    print("     We will have to keep you under a constant watch, no matter where you are going or want to go")
    print("     you have to report to us an hour in advance")
    sleep(8)
    print("     and we will have to reinforce your office")
    sleep(5)
    input("Press Enter to continue...")
    SsConfrontation()

def SsConfrontation():
    global karma
    print("You:")
    sleep(3)
    print("     Actually, you know what?")
    sleep(2)
    print("     screw this, i'm done with politics")
    sleep(1)
    print("     i'm out of here")
    sleep(4)
    print("SS agent Nolan:")
    sleep(2)
    print("     i")
    print("     uhh")
    sleep(3)
    print("     are you sure?")
    sleep(3)
    print("Do you really want to quit politics altogether?")
    input("Yes/No > ")
beginning()