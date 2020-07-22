ten_things = "apples oranges crows telephone light sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff)) # I'm expecting this will turn it into a string, separated by a space
print("#".join(stuff[3:5])) # I'm expecting this will turn the fourth to sixth element of stuff into a string, separated by #
