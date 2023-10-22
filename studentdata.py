students = ["Joseph D", "Newie V", "Anna N", "Mason N"]
hometown = ["Sterling Heights", "Grand Prairie", "Shelby Township", "Arlington"]
fav_food = ["Beef Bowls", "Noodles", "Shrimp Fried Rice", "Papaya Salad"]

cont = 'y'

while cont == 'y':
    for individual in students:
        print(individual)

    choice = int(input("Welcome! Which student would you like to learn more about? Enter a number between 1-4: "))

    while choice > len(students) or choice < 1:
        choice = int(input("This is an invalid number. Please try again by entering a number between 1-4: "))
    else:
        print(f"Student {choice} is " + students[choice - 1] + ". " + "What would you like to know?")
        choice2 = input("Enter 'hometown' or 'favorite food': ")

        while choice2 != 'hometown' and choice2 != 'favorite food':
            choice2 = input("This is an invalid input. Please enter 'hometown' or 'favorite food: ")

        if choice2 == 'hometown':
            print(students[choice - 1] + "'s" + " hometown is " + hometown[choice - 1])


        elif choice2 == 'favorite food':
            print(students[choice - 1] + "'s" + " favorite food is " + fav_food[choice - 1])

    cont = input("Would you like to learn about another student? Enter 'y' or 'n': ")

else:
    print("Thanks!")




