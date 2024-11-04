import os, time, random

trumps = {}

trumps["Monica"] = {"Intelligence": 178, "Speed": 40, "Guile":50, "Baldness Level": 0}
trumps["Rachel"] = {"Intelligence": 100, "Speed": 40, "Guile":35, "Baldness Level": 0}
trumps["Phoebe"] = {"Intelligence": 150, "Speed": 100, "Guile":60, "Baldness Level": 0}
trumps["Joe"] = {"Intelligence": 50, "Speed": 50, "Guile":150, "Baldness Level": 0}

while True:
    print("Top Trumps")
    print()
    print("Characters")
    print()

    for key in trumps:
        print (key)
    user = input("Pick your Character\n>").title()
    comp = random.choice(list(trumps.keys()))
    
    print("Computer has picked", comp)
    print()
    
    print("Choose your stat: Intelligence, Speed, Guile")
    answer = input("> ").title()
    
    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")
    
    if trumps[user][answer] > trumps[comp][answer]:
        print(user, "wins")
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, "wins")
    else:
        print("Draw")

    time.sleep(2)
    os.system("clear")


