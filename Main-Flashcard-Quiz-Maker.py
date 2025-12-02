flashcards = {"CPU": "Central Processing Unit", "GPU": "Graphics Processing Unit"}

def save_flashcards():
    print("Placeholder")

def load_flashcards():
    print("placeholder")

    
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
    print("\nOption 2 will allow you to delete/edit flashcards.\n")

    while True:
        choice = input("Please choose an option by using a number 1-4: ")  
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a valid number, 1-4.")
        else:
            if 1 <= choice <= 4:
                if choice == 2:
                    print("\n###################################")
                    print("           View Flashcards           ")
                    print("###################################")
                    print("1.View Flashcards") # 2a
                    print("2.View Flashcards & edit one.") # 2b
                    print("3.View Flashcards & delete") #2c
                    while True:
                        choice = input("Please choose an option between 1-3: ")
                        try:
                            choice = int(choice)
                        except ValueError:
                            print("Please input a valid number, 1-3: ")
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
                print("Please input a number between 1 and 4: ")

def view_flashcards():
    if not flashcards:
        print("Flashcards are empty!")
    else:
        print("\nCurrent flashcards:")
        for term, definition in flashcards.items():
            print(term, ":", definition)
        print("\n")

def edit_flashcards():
    #makes a list of terms 
    terms = list(flashcards.keys())
    for i in range(len(terms)):
        print(f"{i + 1}. {terms[i]}") # prints (Number. Term)

    len_list = len(terms)
    while True:
        user_choice = input(f"Choose a number 1-{len_list}.")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Please input a valid number.")
        else:
            if 1 <= user_choice <= len_list:
                selected_index = user_choice - 1
                selected_term = terms[selected_index]
                break
    new_definition = input(f"Please enter the new definition for {selected_term}:")
    flashcards[selected_term] = new_definition
    print(f"The updated flashcard is now: \n{selected_term} : {flashcards[selected_term]}")


def del_flashcards():
    #prints each flashcard with a number
    terms = list(flashcards.keys())
    for i in range(len(terms)):
        print(f"{i + 1}. {terms[i]}") # prints (Number. Term)
    len_list = len(terms)
    print("Which flashcard would you like to delete?")
    while True:
        user_choice = input(f"Choose a number 1-{len_list}")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Please input a valid number.")
        else:
            if 1 <= user_choice <= len_list:
                selected_index = user_choice - 1
                selected_term = terms[selected_index]
                del flashcards[selected_term]
                print(f"Succesfully deleted {selected_term}")
                break


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
        view_flashcards() #this function needs to be called as edit flashcards only displays the terms, not definitions 
        edit_flashcards()
    
    elif choice == "2c":
        view_flashcards()
        del_flashcards()
    
    elif choice == 3:
        view_scores()

    elif choice == 4:
        break
    