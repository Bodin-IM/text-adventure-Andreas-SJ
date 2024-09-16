from os import system
from time import sleep
import workingInStore


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
    global empty
    empty = system('clear||cls')
    empty
    print("You come back to your senses and continue your speech")
    sleep(5)
    print("Suddenly you see a weird glare in the distance and your bodyguard yelling")
    sleep(3)
    print("GET DOWN!")
    toDodgeOrNoToDodge()

def toDodgeOrNoToDodge():
    global empty
    sleep(5)
    print("Do you get down?")
    answer = input("Yes/No > ")

    if answer.lower() in ['no']:
        sleep(2)
        print("You suddenly hear a shot in the distance and it all goes black.")
        sleep(7)
        empty
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
    global empty
    empty
    print("You get crowded by bodyguards using themselves as protection and making sure you get to the ground")
    sleep(7)
    print("the bullet was millimeters away from hitting you")
    input("Press Enter to continue...") 
    empty
    sleep(3)
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
    global empty
    print("WTF man? I know he tried to assassinate you but wouldn't it be more satisfying to let him rot in jail?")
    sleep(8)
    print("1: Nah, he had it coming")
    print("2: Good point")
    input("> ")
    if input == 1:
        karma -= 200
    else:
        print("at least you show some remorse..")
        empty
    secretServiceConversation()
     
def postArrest():
    print("Good call")
    sleep(3)
    print("Now he will at least serve for his crimes")
    input("Press Enter to continue...")
    secretServiceConversation()

def secretServiceConversation():
    sleep(5)
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
    empty
    SsConfrontation()

def YouKeepDoingPolitics():
    global empty
    paranoid = 1
    sleep(4)
    print("*after that stressfull day you decide to go for a walk")
    sleep(4)
    print("You feel a bit paranoid")
    sleep(2)
    print("Do you look behind you?")
    answer = input("Yes/No > ")
    if answer.lower() == 'No':
        paranoid = 2
        print("*you see a silhouette getting out of your view just a second too fast for you to properly identify them")
        sleep(5)
        print("*Your fight or flight kicks in")
    else:
        print("You:")
        print("     Eh, it's probably nothing")
    
    print("*you keep walking ")
    sleep("3")
    print("then you hear a glass bottle rolling down the street")
    if paranoid == 2:
        print("You:")
        print("     A bottle doesn't just start rolling on it's own")
        sleep(3)
        print("     Someone is close, i'm out of here")
        sleep(2)
        print("*you start sprinting away")
        input("Press Enter to continue...")
        empty
        

    else:
        print("You:")
        sleep(2)
        print("     It's probably just a stray cat")
        input("Press Enter to continue...")
        empty
        print("*You hear some footsteps right behind you")
        sleep(1)
        print("*You try to pull a quick manuever when you feel a warm pain in your back")
        sleep(5)
        print("*The footsteps you heard were another assassin")
        sleep(4)
        input("Press Enter to continue...")
        empty
        print("You die a slow death in the middle of the street")
        input("Press Enter to continue...")
        empty
        gameOver()

def GettingAnewJob():
    global name
    global karma
    global empty
    print("After getting your life threatened and quitting your position as the president")
    print("it isn't easy to fake your identity")
    sleep(5)
    print("You are going to need a new name")
    name = input("What is your new name? > ")
    sleep(4)
    print(f"{name} sounds like a great name, no one will be able to recognize you now")
    print("*you walk over to the closest Target to apply for a job")
    sleep(2)
    input("Press Enter to continue...")
    empty 
    sleep(2)
    print("*You walk over to the cashier")
    sleep(5)
    print("You have just started a completely new life, you decide what happens to it")
    sleep (5)
    print("Just keep that in mind")
    sleep ("4")
    print("Do you make a good or bad introduction?")
    choice = input("Good/Bad > ")
    if choice.lower() == 'Bad':
        karma -= 400
        print("You:")
        print("     Yo, give me a job")
        print("Cashier:")
        print("     Excuse you?")



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
    answer = input("Yes/No > ")
    if answer.lower() == 'Yes':
        GettingAnewJob()
    else:
        YouKeepDoingPolitics()
beginning()