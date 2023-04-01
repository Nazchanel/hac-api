def userInput():
    minutes_per_check = None
    try:
        minutes_per_check = float(input("Per how many minutes should the program check your grades >>> "))
    except ValueError:
        print("Enter a number without any spaces or letters!")
        exit(0)

    print()

    username = input("Enter your Student ID >>> ")
    password = input("Enter your password >>> ")
    spacing = ""

    for i in range(30):
        spacing += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print(spacing)

    return username, password, minutes_per_check