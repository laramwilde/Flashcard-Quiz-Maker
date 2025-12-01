def menu():
    choice = None
    print("############################")
    print("    A FLASHCARD PROGRAM     ")
    print("############################")
    print("1.Quiz Mode")
    print("2.View Flashcards")
    # viewing flashcards will allow user to delete/edit them
    print("3.View Scores")
    print("4.Quit")
    print("\nOption 2 will allow you to delete/edit flashcards.")

    while True:
        choice = input("Please choose an option by using a number 1-4: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a valid number, 1-4.")
        else:
            if 1 <= choice <= 4:
                if choice == 2:
                    print("View Flashcards Selected")
                    #print("Please select a number between 1-3.")
                    print("###################################")
                    print("1.View Flashcards") # 2a
                    print("2.View Flashcards & edit one.") # 2b
                    print("3.View Flashcards & delete") #2c
                    while True:
                        choice = input("Please choose an option between 1-3.")
                        try:
                            choice = int(choice)
                        except ValueError:
                            print("Please input a valid number, 1-3.")
                        else:
                            if 1 <= choice <= 3:
                                #2a - View flashcards
                                if choice == 1:
                                    choice = "2a"
                                #2b - View & Edit
                                elif choice == 2:
                                    choice = "2b"
                                #2c - View & delete
                                elif choice == 3:
                                    choice = "2c"
                                return choice
                return choice
            else:
                print("Please input a number between 1 and 4.")

def view_flashcards():
    print("Placeholder")

def edit_flashcards():
    print("Placeholder")

def del_flashcards():
    print("placeholder")

def quiz_mode():
    print("Placeholder")

def view_scores():
    print("Placeholder")

while True:
    choice = menu()
    if choice == 1:
        quiz_mode()

    elif choice == "2a":
        view_flashcards()

    elif choice == "2b":
        view_flashcards()
        edit_flashcards()
    
    elif choice == "2c":
        view_flashcards()
        del_flashcards()
    
    elif choice == 3:
        view_scores()

    elif choice == 4:
        break
    