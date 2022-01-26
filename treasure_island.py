label = ''' Welcome to Treasure Island
 Your mission is to find the treasure '''

game_over = '''
    ..............
   ::::::::::::::::::
  :::::::::::::::
 :::`::::::: :::     :
 :::: ::::: :::::    :
 :`   :::::;     :..~~
 :   ::  :::.     :::.
 :...`:, :::::...:::
::::::.  :::::::::'
 ::::::::|::::::::  !
 :;;;;;;;;;;;;;;;;']}
 ;--.--.--.--.--.-
  \/ \/ \/ \/ \/ \/
     :::       ::::
      :::      ::
     :\:      ::
   /\::    /\:::
 ^.:^:.^^^::`::
 ::::::::.::::
  .:::::::::: 
'''

winner_prizer = ''' 

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print(label)

choice1 = str(input("You are at a crossroad. Where do you want to go [left or right?]: "))
if choice1 == "right" or choice1 != "left":
    print("Fall into a hole, you die. Game Over!!!")
    print(game_over)
else:
    print("the road let you to a lake, there is an island in the middle of the lake")
    choice2 = str(input("[wait] for a boat or [swim] to swim across? What your decision: "))
    if choice2 != "wait":
        print("The river has sharks and they bite you. you die. Game Over")
        print(game_over)
    else:
        print("you arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue.")
        choice3 = str(input("Which door do you choose to open? - [red, yellow or blue]: "))
        if choice3 == "red":
            print("You open gate of hell. Demonic creatures take you inside. you will suffer for all eternity")
            print("Game Over")
            print(game_over)
        elif choice3 == "yellow":
            print("You open the black hole room. You will fall inside another dimension forever.")
            print("Game Over")
            print(game_over)
        elif choice3 == "blue":
            print("You win the game, here your prize")
            print(winner_prizer)
        else:
            print("option not found")
