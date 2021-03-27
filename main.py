# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyttsx3
import CharClasses
import WeaponsClasses
def game_start():
    print('Hello, welcome to the AdventureGame. Please enter your name')
    pyttsx3.speak('Hello, welcome to the AdventureGame. Please enter your name')
    name = input('Enter Name : ')
    return name


def player_assign(s):
    if s == 1:
        player_char = CharClasses.Knight(5, 5, 1, 1, 50)
    if s == 2:
        player_char = CharClasses.Barbarian(6, 3, 1, 2, 50)
    if s == 3:
        player_char = CharClasses.Wizard(5, 2, 3, 2, 50)
    if s == 4:
        player_char = CharClasses.Rogue(5, 3, 3, 5, 50)
    return player_char

def char_select(char):

    print("Please select your character.")
    pyttsx3.speak('Please select your character')

    print("1 -- Knight")
    print("2 -- Barbarian")
    print("3 -- Wizard")
    print("4 -- Rogue")
    selection = int(input("Please enter 1 , 2 , 3 or 4 to select your character " + char + ": "))
    while selection not in [1, 2, 3, 4]:
        print("Not a valid selection, please try again")
        selection = int(input("Please enter 1 , 2 , 3 or 4 to select your character " + char + ": "))
    player_assign(selection)
    print("you have selected " + str(selection) + " do you want to see their stats?")
    pyttsx3.speak("you have selected " + str(selection) + " do you want to see their stats?")
    y_or_n = input("enter Y to see stats or N if you just wish to continue ")
    if y_or_n == "y":

        print('Show Stats for your class')
        char_stats(selection)
        print('do you want to select this character?')
        game_start = input('please enter y to start game or press anything else to reselect')
        if game_start == 'y':
            start_game()
            player_assign(selection)

        elif game_start != 'y':
            char_select(char)
    elif y_or_n == "n":

        print("Continue to game")
        player_assign(selection)
        start_game()
    else:
        print("Not a valid selection, please try again")
        char_select(char)


def char_stats(char):
    print("Your stats are as follows: ")
    if char == 1:
        print('Knight --')
        print('Attack    --  5')
        print('Defence   --  5')
        print('Magic     --  1')
        print('Dexterity --  1')

    if char == 2:
        print('Barbarian --')
        print('Attack    -- 6')
        print('Defence   -- 3')
        print('Magic     -- 1')
        print('Dexterity -- 2')

    if char == 3:
        print('Wizard --')
        print('Attack    --  5')
        print('Defence   --  2')
        print('Magic     -- 3')
        print('Dexterity -- 2')

    if char == 4:
        print('Rogue --')
        print('Attack    -- 5')
        print('Defence   -- 3')
        print('Magic     -- 3')
        print('Dexterity -- 5')


def help_screen():

    print('Look around the rooms by typing LOOK LEFT , LOOK RIGHT , LOOK FORWARD , LOOK DOWN. To'
          'Inspect an item type INSPECT followed by the name of the item. To view your inventory'
          'type INVENTORY. To use an item in your inventory type USE YOURITEM on OTHERITEM for '
          'example USE KEY on DOOR to read these messages again type HELP')

def user_input(input):


    if input == "LOOK LEFT":
        print("You look left")
    if input == "LOOK RIGHT":
        print("You look right")
    if input == "LOOK FORWARD":
        print("You look left")
    if input == "LOOK DOWN":
        print("You look down")
    if input == "HELP":
        help_screen()

    #DO SOMETHING ABOUT ERROR HANDLING



def start_game():

    print('Welcome to the AdventureGame!')
    pyttsx3.speak('Welcome to the AdventureGame!')
    help_screen()



    knight_sword = WeaponsClasses.Sword(10).sword_damage(5)


def r1():
    doorisclosed = True
    print('You wake up in a small, dark room. Rats running beneath your feet. In the background you can hear'
          'sounds of metal doors slamming and distant screams. You have to get out of here... but how?')
    pyttsx3.speak('You wake up in a small, dark room. Rats running beneath your feet. In the background you can hear'
          'sounds of metal doors slamming and distant screams. You have to get out of here... but how?')
    while doorisclosed:
        userinput = input('What would you like to do : ')
        user_input(userinput)
        if userinput == "LOOK LEFT":
            #GO TO FUNCTION FOR LOOKING LEFT
            r1lookleft()
        elif userinput == "LOOK RIGHT":
            #GO TO FUNCTION FOR LOOKING RIGHT
            r1lookright()
        elif userinput == "LOOK FORWARD":
            #GO TO FUNCTION FOR LOOKING FORWARD
            r1lookforward()
        elif userinput == "LOOK DOWN":
            #GO TO FUNCTION FOR LOOKING DOWN
            r1lookdown()
        else:
            print('Not a valid input. type help to look at options')





def r1lookleft():
    print('Looking left from the bed you are sat on you can see in the darkness a stone wall covered in damp'
          'there is a small black iron bar window going into the cell next door.')
    pyttsx3.speak('Looking left from the bed you are sat on you can see in the darkness a stone wall covered in damp'
          'there is a small black iron bar window going into the cell next door.')
    looking_left = True
    stonewall_inspected = False
    while looking_left:
            uinput = input('What would you like to do : ')
            if uinput == "LOOK AWAY":
                print('You look away')
                looking_left = False
            #if uinput == "INSPECT STONE WALL" & stonewall_inspected == False:


             #   print('Looking at the stone wall closer, you notice one of the stones is loose.Pulling at the old stone'
             #         'it breaks out. Looking in the hole there is a rusty spanner. you put this in your pocket')
                #PUT SPANNER IN INVENTORY
             #   inventory.append('Spanner')
             #   stonewall_inspected = True
             #   print(inventory)
            if uinput == "INSPECT STONE WALL" & stonewall_inspected == True:
                print('There is nothing new about this wall.')

            if uinput == "INSPECT WINDOW":
                print('Inspect Window')





def r1lookright():
    print('Looking right you see a small wash basin and a copper pipe that goes to the floor. it is bolted to the ground'
          ' with 4 large bolts')

def r1lookforward():
    print('In front of you is a large barred prison cell door. there is a rusted padlock with a hole for a key.')


def r1lookdown():
    print('looking down onto the bed you are sitting on there is a thin mattress and a pillow full of straw.')

if __name__ == "__main__":
    char_name = game_start()
    char_select(char_name)
    inventory = []
    r1()


