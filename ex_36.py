from sys import exit

class player:
    def __init__(self, name):
        # name will be input by player at start
        self.name = name
        # until I figure out how to link an item class to a player, I'm keeping the gold here
        self.gold = False
        # player doesn't start poisoned, nor has a troll companion.
        self.poisoned = False
        self.companion = False

    def player_poisoned(self):
        self.poisoned = True

    def has_gold(self):
        self.gold = True

    def has_companion(self):
        self.companion = True

def riddle_room():
    print("You enter a room. It is empty, but to your right, there is a door. Next to the door, there appears to be a thin hole in the wall, and an inscription that reads:",
          "'I have a tail, a head, but no legs. I am probably with you even now. What am I?'")

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



def corridor():

def dragon_room():

def kobold_room():

def troll_room():

def table_room():

def tree_room():

def dead(why):

def start():

