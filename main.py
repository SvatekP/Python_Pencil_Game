import random

pencils = 0
while pencils < 1:
    try:
        pencils = int(input("How many pencils would you like to use: "))
    except ValueError:
        print("The number of pencils should be numeric")

    if pencils < 1:
        print("The number of pencils should be positive")

player = ""
while player != "John" and player != "Jack":
    player = input("Who will be the first (John, Jack): ")
    if player != "John" and player != "Jack":
        print("Choose between 'John' and 'Jack'")

if player == "John":
    bot = "Jack"
else:
    bot = "John"

while pencils != 0:
    print("|" * pencils)

    if player == bot:
        print(player, "'s turn!")
    else:
        print(player, "'s turn:")

    remove = 0
    if player == bot:
        if pencils % 2 == 0 and pencils % 4 == 0:
            remove = 3
        elif pencils % 2 == 0:
            remove = 1
        elif pencils == 1:
            remove = 1
        elif (pencils - 1) % 2 == 0 and (pencils - 1) % 4 == 0:
            remove = random.randint(1, 3)
        else:
            remove = 2
        print(remove)
    else:
        while True:
            try:
                remove = int(input())
            except ValueError:
                print("The number of pencils should be numeric")
            if remove > 3:
                print("Possible values: '1', '2' or '3'")
            elif remove < 1:
                print("Possible values: '1', '2' or '3'")
            elif pencils < remove:
                print("Too many pencils were taken")
            else:
                break

    pencils = pencils - remove

    if player == "John":
        player = "Jack"
    elif player == "Jack":
        player = "John"

    if pencils == 0:
        print(player, "won!")
