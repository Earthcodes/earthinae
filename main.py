
#This is a text based adventure game
#
#A SPACE ADVENTURE: BACK HOME
#
#to play the inserted games you have to install pygame()
#
#when typing answers, you can use only the first letter
#
###################################
#the variables are:

yes = {"yes", "y", "ye"}

no = {"no", "n"}

right = {"r", "ri", "rig", "righ", "right"}

left = {"l", "le", "lef", "left"}

drink = {"d", "dr", "dri", "drin", "drink"}

######################
#introduction to the game
#insert your name to start the game

name = input(str("Please enter your name to start the adventure of a lifetime: "))
print("Hello" ,name," ... this is how your adventure begins ...")
print()

#create a while loop for the game to return to this point in case you answer no
panic = 1
while panic == 1:
    print()
    print("You wake up in a foreign place.")
    print("You do not know how you ended up there but start looking around ... ")
    print("it does not take you long to realize you are in a spaceship orbiting an unfamiliar planet.")


    #use while loop which you enter if answer is not valid
    answer="xy"
    while answer not in yes and answer not in no:
        answer = input("You start panicking, do you want to try to calm down? (yes/no)"). lower(). strip()
        if answer in yes:
            panic = 0
            print()
            print("Cool! You decide to go look for the command room in order to fly back home.")
            break
        elif answer in no:
            print()
            print("You continue shouting and end up fainting again, get it together!")
        else:
            print()
            print("Don't mess with our game! Enter yes or no")
            continue

print("As you are looking around the lab you see a glass filled with what seems to be water.")

#while loop for the case on invalid answer --> valid answers lead to games and break the loop
while True:
    answer2 = input("You are quite thirsty. Do you drink it, or do you walk past the glass? (drink/no)"). lower(). strip()
    if answer2 in drink:
        print()
        print("As it turns out this was probably not your best decision.")
        print("As you make your last sip, you notice the liquid in the glass turning fluorescent.")
        print("You turn into a snake")
        print("You notice different pills scattered around the lab.")
        print("You are hoping one of the pills will turn you back into your human form.")
        print("Try to eat as many pills as possible in the hope you find the right one")


        ###########################################################
        while True:
        #   pygame() --> snake --> that gives as a result an input = ? (some number to determine if you exit the loop or stay in the loop and play the minigame again)
            import Snake
            try:
                snake()
            except:
                print("Good job, the last pill you ate was the right one")
                break


        ###########################################################

        break


    elif answer2 in no:
        print()
        print("You aren't that gullible!")
        print("duh, of course you don't drink a random substance in an unfamiliar lab")
        print("It might have killed you!")
        print()
        print("While exploring the complex you encounter a door.")
        print("Unfortunately, there is an alien-looking creature in front of it.")
        print("Try to lead the monster away from the passage by leading it food")
        print("Hopefully, you gain enough time to get past the creature.")

        ###########################################################
        while True:
        #   pygame() --> snake --> that gives as a result an input = ? (some number to determine if you exit the loop or stay in the loop and play the minigame again)
            import Snake
            try:
                snake()
            except:
                print("Good job, the last pill you ate was the right one")
                break
        ###########################################################

        break


    else:
        print()
        print("Don't mess with our game! Enter drink or no")
        continue

print()
print("As you proceed through the spaceship, you enter another room.")
print("ATTENTION! The floor is flooded and water keeps leaking into the room")
print("You find the water valve but are unsure in which direction to turn it to stop the leakage.")

while True:
    answer3 = input("Do you turn in in the left or the right direction? (left/right)"). lower(). strip()
    if answer3 in left:
        print()
        print("OH NO! you turned the valve in the wrong direction, high water pressure breaks the pipes.")
        print("Suddenly the lights go off.")
        print()
        print("Fortunately, you remember seeing a lightning bolt sign on one of the metal panels on ")
        print("the room's ceiling.")
        print("The electric panel is probably there. Try to climb up and repair the wiring.")
        print("But beware ... all that water has made your shoes quite slippery!")

        ###########################################################
        while True:
        #pygame() --> doodle jump game --> that gives as a result an input = ? (some number to determine if you exit the loop or stay in the loop and play the minigame again)
            import Bounce

            try:
                    bounce()
            except:
                    print("Congratulations, you almost slipped, but you managed to complete this dangerous task")
                    print("You proceed on your quest")
                    break

        ###########################################################

        break


    elif answer3 in right:
        print()
        print("You are a real handy man!")
        print("The water has stopped filling up the room,")
        print("you walk towards the door in front of you, only to find it locked.")
        print("You look around for something that might help you unlock the door.")
        print()
        print("After a bit you find what seems to be a small remote controlled robot.")
        print("You decide piloting it through the venting system so that it can unlock the door")
        print("from the other side.")

        ###########################################################
        while True:
        #   pygame() --> doodle jump game --> that gives as a result an input = ? (some number to determine if you exit the loop or stay in the loop and play the minigame again)
            import venv.Game.Bounce
            try:
                bounce()
            except:
                print("Congratulations, you almost slipped, but you managed to complete this dangerous task")
                print("You proceed on your quest")
                break
        ###########################################################

        break


    else:
        print("Don't mess with our game! Enter yes or no")
        continue

print()
print("Finally, you enter the command room and set your destination to earth")
print("Time to fly!!)")
print("...")
print("But beware of the asteroids!")


###########################################################
#pygame() --> rocket
import Rocket
meteorAttack()

#
#
#
###########################################################
#
#can ask a question whether to play the whole game again or to quit the game
#create a function out of the whole game and just insert it, to replay
#
#
#





