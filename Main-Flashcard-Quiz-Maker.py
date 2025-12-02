from datetime import datetime

flashcards = {}

'''
As the flashcards dictionary will be empty when the program first starts - it needs to add what is in the file into the dictionary.
The save flashcard function will overwrite what was in the file incase anything has been deleted or edited.
'''
def save_score(timestamp,score):
    with open("scores.txt", "a") as file:
        file.write(f"{timestamp} | {score}/{len(flashcards)}\n")

def save_flashcards():
        with open("flashcards.txt", "w") as file:
            for term, definition in flashcards.items():
                file.write(f"{term}|{definition}\n")


def load_flashcards():
    try:          #the file name ,  read    , handle
        with open("flashcards.txt", "r") as file:
            for line in file:
                line = line.strip()
                term, definition = line.split("|", 1)
                flashcards[term] = definition
    except FileNotFoundError:
        pass   # does nothing , the save flashcards will create the file if there is not one

def menu():
    choice = None
    print("============================")
    print("    A FLASHCARD PROGRAM     ")
    print("============================")
    print("1.Quiz Mode")
    print("2.View Flashcards")
    print("3.Add Flashcards")
    # viewing flashcards will allow user to delete/edit them
    print("4.View Scores")
    print("5.Quit")
    print("\nOption 2 will allow you to delete/edit flashcards.\n")

    while True:
        choice = input("Please choose an option by using a number 1-5: ")  
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a valid number, 1-5.")
        else:
            if 1 <= choice <= 5:
                if choice == 2:
                    print("\n===================================")
                    print("           View Flashcards           ")
                    print("===================================")
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
                print("Please input a number between 1 and 5: ")

def view_flashcards():
    if not flashcards:
        print("Flashcards are empty!")
    else:
        print("\nCurrent flashcards:")
        for term, definition in flashcards.items():
            print(term, ":", definition)
        print("\n")

def edit_flashcards():
    if not flashcards:
        print("\nTHERE ARE CURRENTLY NO FLASHCARDS. PLEASE ADD FLASHCARDS BEFORE SELECTING THIS OPTION.")
        return
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
    if not flashcards:
        print("\nTHERE ARE CURRENTLY NO FLASHCARDS. PLEASE ADD FLASHCARDS BEFORE SELECTING THIS OPTION.")
        return
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
    if not flashcards:
        print("================")
        print("     WARNING    ")
        print("================")
        print("\nFlashcards are empty - please add some flashcards before selecting quiz mode.\n")
        return
    print("\n")
    print("=======================")
    print("       QUIZ MODE       ")
    print("=======================")
    print("\nPlease select from the following two options:")
    print("1.Program tests if the answer is correct.")
    print("     WARNING (CHOOSING OPTION 1 MEANS THAT YOUR ANSWER HAS TO BE EXACTLY CORRECT, LETTER FOR LETTER.)")
    print("        DO NOT CHOOSE THIS OPTION IF YOU WANT SCORES TO BE 100% ACCURATE OR YOU DO NOT KNOW THE EXACT ANSWERS.\n")
    print("2.User inputs if the answer was correct.")
    while True:
        choice = input("Please choose option 1 or 2:")
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a valid number.")
        else:
            if choice == 1 or choice == 2:
                if choice == 1:
                    print("Reminder - Answers have to be correct letter for letter to be counted as correct.")
                    #makes a list of terms
                    score = 0
                    for term,definition in flashcards.items():
                            clean_correct_answer = definition.lower()
                            print("==================================")
                            print(term)
                            print("==================================")
                            user_answer = input("Input answer:")
                            user_answer = user_answer.strip().lower()
                            clean_correct_answer = clean_correct_answer.strip().lower()
                            if user_answer == clean_correct_answer:
                                print("Correct!")
                                score += 1
                            else:
                                print("Incorrect!")
                                print(f"The correct answer was: \n {definition}")
                    print("\nYou have completed the flashcards quiz.")
                    print(f"Your score was: {score} / {len(flashcards)}")
                    while True:
                        user_choice = input("Would you like to save your score? Y/N")
                        if user_choice.lower() == "y":
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                            save_score(timestamp,score)
                            print("Score has been saved.")
                            break
                        elif user_choice.lower() == "n":
                            print("Score has not been saved.")
                            break
                        else:
                            print("Please enter Y/N.")
                    return
                elif choice == 2:
                    score = 0
                    print("======================================================")
                    print("You have selected option 2.")
                    print("In this mode, input Y if you got it correct, N if not.")
                    print("======================================================\n")
                    for term,definition in flashcards.items():
                        print("========================")
                        print(term)
                        print("========================")
                        user_answer = input("Input an answer:\n")
                        print(f"\nYour answer was: {user_answer}\nThe correct answer is: {definition}\n")
                        correct = input("Is this correct? Y/N")
                        if correct.lower() == "y":
                            score += 1
                    print("\nYou have completed the flashcards quiz.")
                    print(f"Your score was {score} / {len(flashcards)}")
                    user_choice = input("Would you like to save your score? Y/N")
                    if user_choice.lower() == "y":
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                        save_score(timestamp,score)
                        print("Score has been saved.")
                        break
                    elif user_choice.lower() == "n":
                        print("Score has not been saved.")
                        break
                    return
            else:
                print("Please input 1 or 2!")


def view_scores():
    try:
        with open("scores.txt", "r") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("\nNo scores have been saved yet.")
        print("Please save scores in quiz mode before selecting view scores.")
        print("Returning to main menu.\n")

def add_flashcard():
    while True:
        new_flashcard_term = input("Input the term:")
        if new_flashcard_term == "":
            print("Term cannot be empty.")
        elif new_flashcard_term.isspace():
            print("Term cannot be empty!")
        else:
            break
    while True:
        new_flascard_definition = input("Input the definition: ")
        if new_flascard_definition == "":
            print("Definition cannot be empty!")
        elif new_flascard_definition.isspace():
            print("Definition cannot be empty!")
        else:
            break
    flashcards[new_flashcard_term] = new_flascard_definition
    print("You have now added the following flashcard:")
    print(f"{new_flashcard_term} : {new_flascard_definition}")

while True:
    load_flashcards()
    choice = menu()

    # QUIZ MODE
    if choice == 1:
        quiz_mode()

    #VIEW FLASHCARDS
    elif choice == "2a":
        view_flashcards()

    #EDIT FLASHCARDS
    elif choice == "2b":
        view_flashcards() #this function needs to be called as edit flashcards only displays the terms, not definitions 
        edit_flashcards()
        save_flashcards()
    
    #DELETE FLASHCARDS
    elif choice == "2c":
        view_flashcards()
        del_flashcards()
        save_flashcards
    
    #ADD FLASHCARDS
    elif choice == 3:
        add_flashcard()
        save_flashcards()

    #VIEW SCORE
    elif choice == 4:
        view_scores()

    #QUIT
    elif choice == 5:
        break
    