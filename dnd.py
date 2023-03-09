print("Hello, welcome to AV DnD tracker, version 0.1.1")
purpose = input("Are you (l)oading an encounter or making a (n)ew one: ")
user=input("What is your encounter name: ")
if purpose == "l":
    with open(user+".py","r") as file:
        script = file.read()
        exec(script)
    for creature in range(amount_of_creatures):
        print(f"{creatures[creature][0].capitalize()} has {creatures[creature][1]} health, an AC of {creatures[creature][2]} and a side note of {creatures[creature][3]}")
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
                with open(user+".py","w") as file:
                    file.write("creatures = ")
                with open(user+".py","a") as file:
                    file.write(f"{creatures}")
                    file.write("\n")
                    file.write(f"amount_of_creatures = {amount_of_creatures}")

elif purpose == "n":
    with open(user+".py","w") as file:
        contents = file.write("creatures = {")
    with open(user+".py","a") as file:
        amount_of_creatures = int(input("How many people will there be in the encounter: "))
        for creature in range(amount_of_creatures):
            print(f"Creature number {creature+1}")
            name = input("What would you like to designate this creature: ")
            health = input("How much hp should this creature have: ")
            armour = input("What is the ac of the creature: ")
            notes = input("Any other information: ")
            file.write(f"{creature}:[\"{name}\",{health}, {armour}, \"{notes}\"],\n")
        file.write("}\n")
        file.write(f"amount_of_creatures = {amount_of_creatures}")