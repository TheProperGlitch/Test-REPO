print("Hello, welcome to AV DnD tracker, version 0.0.1")
purpose = input("Are you (l)oading an encounter or making a (n)ew one: ")
user=input("What is your encounter name:")
if purpose == "l":
    print("Sorry, this feature is under construction.")
if purpose == "n":
    with open (user+".txt","w") as file:
        file.write("testing")