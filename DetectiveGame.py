import time

gameOver = False

intelligence = 0
inventory = ["Revolver","Lighter", "Cigarettes"]

playerName = input("What is your name detective? ")
print("The year is 1966, East London")
time.sleep(2)
print("Detective " + playerName, ", your partner has been missing for the past two days.")
time.sleep(1)
print("His last known whereabouts follow the steps of Pacho Rerra at the port, gang leader for the Red Barrels.")
print("We believe his location was comprimised and Red Barrels kidnapped him.")
time.sleep(1)
print("We cannot afford to lose another agent Detective.")
print("Take this with you, you might need it.")
print("Revolver has been added to inventory!")
print(inventory)
time.sleep(2)

print("5 Days Later | Somewhere in the Atlantic Ocean")
time.sleep(2)

print("You have woken in a boat cabin strapped to a chair. Your hands and feet are tied on the chair with a rope and the only thing visible outside is the ocean.")
time.sleep(1)
print("You don't even remember what happened.")
time.sleep(1)
print("You hear growling from the room across. Could that be your partner? What do you do? What is your plan?")

def roomSearch():
    print("You start looking around the room for any clues. You see a stack newspapers together with some duct tape")

def chairEscape():
    print("You try struggle but its effortless. There must be another way around this. Maybe a way to get rid of the rope?")

def scream():
    print("ya dead")

def scream2():
    print("The door opens and two men walk through.")

while not gameOver:
    usrinpt = input("Look for items, escape the chair or scream for help?").lower()
    if usrinpt in ["look for items", "search room", "search"]:
        roomSearch()
    elif usrinpt in ["escape"]:
        chairEscape()
    elif usrinpt in ["scream"]:
        if "rope" in inventory:
            scream2()
        else:
            scream()
    else:
        print("That was not an option, pick again")


    if "inv" in input():
        print(inventory)
