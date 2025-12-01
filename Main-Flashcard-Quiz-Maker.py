def menu():
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
                    print("1.View Flashcards")
                    print("2.View Flashcards & edit one.")
                    print("3.View Flashcards & delete")
                    while True:
                        choice = input("Please choose an option between 1-3.")
                        try:
                            choice = int(choice)
                        except ValueError:
                            print("Please input a valid number, 1-3.")
                        else:
                            if 1 <= choice <= 3:
                                return choice
                return choice
            else:
                print("Please input a number between 1 and 4.")

#def view_flashcards():

print(menu())