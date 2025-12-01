def menu():
    print("############################")
    print("    A FLASHCARD PROGRAM     ")
    print("############################")
    print("1.Quiz Mode")
    print("2.View Flashcards")
    # viewing flashcards will allow user to delete/edit them
    print("3.View Scores")
    print("4.Quit")
    print("\n Option 2 will allow you to delete/edit flashcards.")
    choice = input("Please choose an option by using a number 1-4.")
    flag = True
    while flag == True:
        try:
            int(choice)
        except ValueError:
            choice = input("Please input a valid number, 1-4.")
        else:
            flag = False
            return choice

