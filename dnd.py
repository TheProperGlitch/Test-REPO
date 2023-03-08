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
        looping_battle = False
elif purpose == "n":
    with open(user+".py","w") as file:
        contents = file.write("creatures = {\n")
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