known_users = ["Yaron","Mounika","Kareen","Max","Marco","Helder","Asaf","Ivan"]

print(len(known_users))

while True:
    print("Hi, my name it Travis!")
    name = input("What is your name?: ").strip().capitalize()  # strip function if user enters a space and capitalize for upper and lower case input

    if name in known_users:
        print("Hello {} i know you".format(name))
        remove = input("Would you like to be removed from the system (y/n)??").strip().lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)

    else:
        print("Hello {} i don't recognized you".format(name))
        add_me = input("Would you like to be added to the list (y/n)?:").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("No worries mate, see you around!")
