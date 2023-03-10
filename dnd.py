import os
files = os.listdir('.')
files.remove(".git")
files.remove(".gitignore")
files.remove("dnd.py")
print("Hello, welcome to AV D&D tracker: Version 0.2.1")
purpose = input("Would you like to (l)oad an encounter, (a)dd to one, make a (n)ew one, or (c)opy a one: ")
print(f"Current files: {files}")
if purpose.lower() == "l" or purpose.lower() == "load":
    user = input("What is the encounter's name: ")
    with open(user+".py","r") as file:
        script = file.read()
        exec(script)
    for creature in range(amount_of_creatures):
        if creatures[creature][3] == "":
            print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and no side notes.")
        else:
            print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and a side note of: {creatures[creature][3]}.")
    looping_battle = True
    while looping_battle:
        action = int(input("Which creature would you like to interact with (0 for end): "))
        if action == 0:
            print("Goodbye!")
            looping_battle = False
        elif action < 0:
            print("Error, number lower than zero. Please try again.")
        elif action > amount_of_creatures:
            print("There are not that many creatures. Please try again.")
        else:
            modifier = input("What would you like to change about the creature. (d)amage or (n)otes: ")
            if modifier == "d":
                damage = int(input("How much damage would you like to do: "))
                target_creature = creatures[action-1]
                target_creature[1] = target_creature[1] - damage
                print(f"{target_creature[0]} now has {target_creature[1]} health.")
                creatures[action-1] = target_creature
                for creature in range(amount_of_creatures):
                    if creatures[creature][3] == "":
                        print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and no side notes.")
                    else:
                        print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and a side note of: {creatures[creature][3]}.")
                with open(user+".py","w") as file:
                    file.write("creatures = ")
                with open(user+".py","a") as file:
                    file.write(f"{creatures}")
                    file.write("\n")
                    file.write(f"amount_of_creatures = {amount_of_creatures}")
            elif modifier == "n":
                new_notes = input("What would you like the new notes to be: ")
                target_creature = creatures[action-1]
                target_creature[3] = new_notes
                print(f"{target_creature[0]}'s notes are now {target_creature[3]}")
                creatures[action-1] = target_creature
                for creature in range(amount_of_creatures):
                    if creatures[creature][3] == "":
                        print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and no side notes.")
                    else:
                        print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and a side note of: {creatures[creature][3]}.")
                with open(user+".py","w") as file:
                    file.write("creatures = ")
                with open(user+".py","a") as file:
                    file.write(f"{creatures}")
                    file.write("\n")
                    file.write(f"amount_of_creatures = {amount_of_creatures}")

elif purpose.lower() == "n" or purpose.lower() == "new":
    user=input("What is your encounter's name: ")
    with open(user+".py","w") as file:
        contents = file.write("creatures = {")
    with open(user+".py","a") as file:
        amount_of_creatures = int(input("How many creatures will there be in the encounter: "))
        for creature in range(amount_of_creatures):
            print(f"Creature number {creature+1}")
            name = input("What would you like to name this creature: ")
            health = input("How many health points should this creature have: ")
            armour = input("What is the armour class of the creature: ")
            notes = input("Any other information: ")
            if name == "":
                name = f"creature{creature}"
            if health == "":
                health = "0"
            if armour == "":
                armour == "0"
            file.write(f"{creature}:[\"{name}\",{health}, {armour}, \"{notes}\"],\n")
        file.write("}\n")
        file.write(f"amount_of_creatures = {amount_of_creatures}")
elif purpose.lower() == "c" or purpose.lower() == "copy":
    user=input("What is the encounter's name: ")
    new_file_name = input("What would you like to name the new copy: ")
    if f"{new_file_name}.py" in files:
        print("Sorry, you cannot name a file the same name as another. Please try again.")
    else:
        with open(user+".py","r") as file:
            old_file = file.read()
        with open(new_file_name+".py","w") as file:
            file.write(old_file)
        print("File copied!")

elif purpose.lower() == "a" or purpose.lower() == "add":
    user = input("What file would you like to add to: ")
    with open(user+".py","r") as file:
        old_file = file.read()
    exec(old_file)
    amount = int(input("How many creatures would you like to add: "))
    for creature in range(amount):
        print(f"Creature number {creature+1}")
        name = input("What would you like to name this creature: ")
        health = int(input("How many health points should this creature have: "))
        armour = int(input("What is the armour class of the creature: "))
        notes = input("Any other information: ")
        if name == "":
            name = f"creature{creature}"
        if health == "":
            health = "0"
        if armour == "":
            armour == "0"
        creatures[amount_of_creatures] = [name, health, armour, notes]
        amount_of_creatures = len(creatures)
    with open(user+".py","w") as file:
        file.write("creatures = "+ f"{creatures}" +" \namount_of_creatures = "+ f"{amount_of_creatures}")
    print("Goodbye!")



else:
    print("Error: Please enter a valid letter (n, c, or l) or word (new, copy, or load)")