def calculater():
    print("---calculater---")
    while True:
        try:
            num1 = int(input("Plesae enter your first number: "))
            op = input("Please select your operator! +, -, *, /, ")
            num2 = int(input("Plesae enter your second number: "))
        except ValueError:
            print("That's not number Please Enter Number")
        else:
            if op == "+":
                print(num1 + num2)
            elif op == "/" and num2 == 0:
                print("cannot divided by zero")
            elif op == "/":
                print(num1 / num2)
            elif op == "*":
                print(num1 * num2)
            elif op == "-":
                print(num1 - num2)
            else:
                print("invalid opeator")
            retry = input("Do you want to calculate again (yes/no)")
            if retry == "yes":
                continue
            else:
                break
def guess_game():
    import pyttsx3
    import random
    while True:
        secret_number = random.randint(1, 50)
        guess_count = 0
        guess_limit = 5
        while guess_count < guess_limit:
            try:
                guess = int(input("Welcom to Guess Game Guess a Number Between 1 to 50: "))
            except ValueError:
                print("That's not number please enter number")
                pyttsx3.speak("That's not number please enter number")
            else:
                guess_count += 1
                if guess == secret_number:
                    print(f"you guess correct! the secret number was {secret_number}")
                    pyttsx3.speak(f"you guess correct! the secret number was {secret_number}")
                    break
                elif guess > secret_number:
                    print(f"It's too high \n ({guess_limit - guess_count}) guess left")
                    pyttsx3.speak(f"It's too high \n ({guess_limit - guess_count}) guess left")
                else:
                    print(f"It's too low \n ({guess_limit - guess_count}) guess left")
                    pyttsx3.speak(f"It's too low \n ({guess_limit - guess_count}) guess left")
                if guess != secret_number and guess_count == guess_limit:
                    print(f"you out off guess \n Secret number was ({secret_number})")
                    pyttsx3.speak(f"you out off guess \n Secret number was ({secret_number})")
        retry = input("Will you like to guess again (yes/no)")
        if retry == "yes":
            continue
        else:
            break
def Superhero_dectonary():
    while True:
        import pyttsx3
        Superheros = {
            "Spider Man": "Peter Parker",
            "Batman": "Bruce Wayne",
            "Superman": "Clark Kent",
            "Iron Man": "Tony Stark",
            "Captain America": "Steve Rogers",
            "Hulk": "Bruce Banner",
            "Thor": "Thor Odinson",
            "Wonder Woman": "Diana Prince",
            "Black Panther": "T'Challa",
            "Flash": "Barry Allen",
            "Doctor Strange": "Stephen Strange",
            "Aquaman": "Arthur Curry",
            "Green Lantern": "Hal Jordan",
            "Wolverine": "Logan / James Howlett",
            "Deadpool": "Wade Wilson",
            "Black Widow": "Natasha Romanoff",
            "Scarlet Witch": "Wanda Maximoff",
            "Green Arrow": "Oliver Queen",
            "Ant Man": "Scott Lang",
            "Shazam": "Billy Batson"}
        pyttsx3.speak ("Enter Superhero name if you want to know there true identity! ")
        identity = input("Enter Superhero name if you want to know there true identity! ")
        if identity in Superheros:
            pyttsx3.speak(Superheros[identity])
            print(Superheros[identity])
        else:
            pyttsx3.speak("identity not found\nSearch other name ")
            print("identity not found\nSearch other name ")
        retry = input("while you like to search again!,(yes/no)").strip().lower()
        if retry == "yes":
            continue
        else:
            break
while True:
    import pyttsx3
    print("="*40)
    print("---Main Manu---")
    print("(1) calculater")
    print("(2) guess_game")
    print("(3) Superhero_dectonary")
    print("(4) Exist")
    print("="*40)
    try:
        pyttsx3.speak("Please enter your choose to open program \n (1)(2)(3)(4)\n")
        choose = input("Please enter your choose to open program \n (1)(2)(3)(4)\n")
    except ValueError:
        print("invalid choice")
    else:
        if choose == "1":
            calculater()
        elif choose == "2":
            guess_game()
        elif choose == "3":
            Superhero_dectonary()
        elif choose == "4":
            break
        else:
            print("invalid choice")