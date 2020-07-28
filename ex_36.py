from sys import exit

class item:
    def __init__(self):
        self.gold = 0

class player:
    def __init__(self, name):
        # name will be input by player at start
        self.name = name
        # until I figure out how to link an item class to a player, I'm keeping the gold here
        self.gold = False
        # player doesn't start poisoned, nor has a troll companion.
        self.poisoned = False
        self.companion = False
        self.item = item()


    # setting the functions to change whether
    def player_poisoned(self):
        self.poisoned = True

    def has_gold(self):
        self.gold = True

    def has_companion(self):
        self.companion = True
        self.gold = True


def riddle_room():
    print("You enter a room. It is empty, but to your right, there is a door. Next to the door, there appears to be a thin hole in the wall, and an inscription that reads:",
          "'I have a tail, a head, but no legs. I am probably with you even now. What am I?'")

player = player(mike)
player.item.gold = 10

    answer = input("> ").lower().strip()
    if answer == "coin" or answer == "gold":
        print("Congratulations, you solved the riddle. But nothing seems to be happening... what do you do?")

        answer = input("> ").lower().strip()
        if ("slot" in answer or "put coin" in answer or "put gold" in answer) and player.companion = True or player.gold = True:
            print("With a giant crack, the door starts to slowly swing open. The daylight bursting into the room is blinding· You're free.\n Congratulations! You win!")
        elif ("slot" in answer or "put coin" in answer or "put gold" in answer) and player.companion = False and player.gold = False:
            print("You don't have any coins to put in the slot. Would you like to go back?")

            answer = input("> ").lower().strip()
            if answer == "no":
                dead("You have no money to pay the exit fee, and you're too lazy to look. Guess you're staying here forever.")

            else:
                corridor()
        else:
            dead("You can't figure out the mechanism of the door.")

    else:
        dead("That was a hard riddle anyway. I doubt anyone could have solved it.")



def corridor(direction):
    if direction == "troll":
        print("You enter a long corridor, curving slightly to the right. You cautiously walk forward. \nAfter a while, on your left, you see a door. Do you try to open it?")

        answer = input("> ").lower().strip()
        if answer == "yes":
            riddle_room()
        elif answer == "no":
            print("You keep following the corridor. It keeps veering off to the right. You start to suspect you might have covered nearly half of a circle when you see a door, directly in front."
                  "Would you like to go through this door?")
            answer = input(">  ").lower().strip()

            if answer == "yes":
                dragon_room("backwards")
            elif answer == "no"
                answer = input("Would you like to go back to the other door? \n> ")

                if answer == "yes":
                    riddle_room()
                else:
                    dead("You spend your days endlessly wandering this corridor.")
            else:
                dead("You spend your days endlessly wandering this corridor.")
        else:
            dead("You spend your days endlessly wandering this corridor.")

    else:
        print(
            "You enter a long corridor, curving slightly to the left. You cautiously walk forward. \nAfter a while, on your right, you see a door. Do you try to open it?")

        answer = input("> ").lower().strip()
        if answer == "yes":
            riddle_room()
        elif answer == "no":
            print(
                "You keep following the corridor. It keeps veering off to the left. You start to suspect you might have covered nearly half of a circle when you see a door, directly in front."
                "Would you like to go through this door?")
            answer = input(">  ").lower().strip()

            if answer == "yes":
                troll_room("backwards")
            elif answer == "no"
                answer = input("Would you like to go back to the other door? \n> ")

                if answer == "yes":
                    riddle_room()
                else:
                    dead("You spend your days endlessly wandering this corridor.")
            else:
                dead("You spend your days endlessly wandering this corridor.")
        else:
            dead("You spend your days endlessly wandering this corridor.")


def dragon_room(direction):
    if direction == "forwards":
        print("You cautiously enter through the door that the kobolds directed you through, not knowing what's on the other side."
              "You peek round. Right in front of you there's a huge pile of glistening gold, gems, glowing things, and right at the top, an enormous sleeping dragon.")
        answer = input("What do you do? \n> ").lower()

        while fred = True:
            answer = input("What do you do? \n> ").lower()
            if "sneak" in answer:
                print("you tiptoe quietly into the room. You see a door on the other side. The dragon appears not to have woken up.")
            elif "take" in answer:
                fred = False
                kobold_room()

            elif "look" in answer:

            elif "poke" in answer:

            elif "wake" in answer:

            elif "fight" in answer:


def kobold_room():

def troll_room(direction):

def table_room():

def tree_room():

def dead(why):

def start():

