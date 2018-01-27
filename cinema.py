films = {
    "Finding Dori": [3,5],
    "Bourne": [18,5],
    "Taraza": [15,5],
    "Ghost Busters": [12,5]
}

while True:
    choise = input("What movie would you like to watch?:").strip().title()
    if choise in films:
        age = int(input("Are old are you?:").strip())
        if age >= films[choise][0]:
            if films[choise][1] > 0:
                print("enjoy the film")
                films[choise][1] = films[choise][1] - 1
            else:
                print("There are no seats available!")
        else:
            print("You are too young to see that film")
    else:
        print("We dont have this film.")