def adventure_game():
    print("Welcome to the Jungle Adventure! 🌴🦜")
    print("You find yourself at the edge of a dense jungle. Your goal is to find the hidden treasure.")
    
    while True:
        print("\nYou're at a crossroad. Where do you want to go?")
        print("1. Go left towards the river.")
        print("2. Go right towards the dark cave.")
        print("3. Go straight into the thick jungle.")
        
        choice = input("Enter 1, 2, or 3: ")
        
        if choice == "1":
            print("\nYou approach the river and see a crocodile 🐊 blocking the way!")
            print("What do you do?")
            print("1. Try to swim across.")
            print("2. Look for another way around.")
            
            sub_choice = input("Enter 1 or 2: ")
            if sub_choice == "1":
                print("\nOh no! The crocodile got you. Game Over! 💀")
                break
            else:
                print("\nSmart choice! You find a bridge and cross safely. 🏞️")
        
        elif choice == "2":
            print("\nYou enter the dark cave and hear strange noises. 🦇")
            print("You see a chest in the distance.")
            print("1. Open the chest.")
            print("2. Leave the chest and run.")
            
            sub_choice = input("Enter 1 or 2: ")
            if sub_choice == "1":
                print("\nThe chest was booby-trapped! You triggered an explosion. 💥 Game Over!")
                break
            else:
                print("\nYou escape the cave safely. 🏃‍♂️")
        
        elif choice == "3":
            print("\nYou walk into the jungle and encounter a wise old parrot. 🦜")
            print("It offers you a riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
            
            answer = input("Your answer: ").strip().lower()
            if answer == "echo":
                print("\nCorrect! The parrot reveals the location of the hidden treasure. You win! 🏆💰")
                break
            else:
                print("\nWrong answer! The parrot flies away, leaving you lost in the jungle. Game Over!")
                break
        else:
            print("\nInvalid choice. Please try again.")

adventure_game()