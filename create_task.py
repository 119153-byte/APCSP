#library of Alexandria

import random
import time

recommended_books = ["S. ", "Odyssey", "House of leaves", "Fall of the house of Cabal", "The Devil and Ms. Prym", "Moby Dick", "Don Quixote", "Othello", "Ulysses", "The Giver"]
authors = ["Doug Dorst & JJ Abrams", "Homer", "Mark Z. Danielewski", "Johnathan L. Howard", "Paulo Coehlo", "Herman Melville", "Miguel De Cervantes", "Shakespeare", "James Joyce", "Lois Lowry"]
user_recommended = []
books_recommended = 0

print("#####WELCOME TO THE LIBRARY######") #only asked once because its the initial start of the program

def m_menu():
        time.sleep(1)
        print("In the library, you can either: \n 1. Recieve a Book Recommendation \n 2. Give a Book Recommendation \n 3. Exit") #menu screen
        time.sleep(1)
        print("Input your choice of (1) (2) (3) \n")
        while True: #while loop to ensure the user's response doesnt break program with undesired response
                user_option = input("Your choice: ")
                try:
                        if int(user_option) in [1, 2, 3]: #when a user's input fulfills the parameter it continues the program
                                break 
                except ValueError:
                        print("Please enter a valid number (1, 2, 3): ")
                else:
                        print("Please enter a valid number (1, 2, 3): ")
        if int(user_option) == 1:
                OPTION1()
        elif int(user_option) == 2:
                OPTION2()
        elif int(user_option) == 3:
                print("Closing program....Goodbye!")
                time.sleep(1)


def redirect(option): #asks user whether to continue or close program at the end of each menu
        if option == 0:
                print(" Will that be all? \n Y/N")
                while True:
                        user_option = input("Your Answer: ")
                        try:
                                if user_option.upper() in ["Y", "N"]:
                                        break
                        except ValueError:
                                print("Please provide a valid answer: ")
                        else:
                                print("Please provide a valid answer: ")
                if user_option.upper() == "Y":
                        print("Closing Program....Goodbye!")
                else:
                        print("Redirecting to Main Menu...")
                        print(' \n' * 12) #clears screen
                        m_menu()
        else: 
                print("Would You likke to: \n a. Provide a New Recommendation \n b. Exit to Main Menu \n c. Exit Program \n")
                while True:                        
                        user_option = input("Your Answer: ")
                        try:
                                if user_option.lower() in ['a', 'b', 'c']:
                                        break
                        except ValueError:
                                print("Please provide a valid answer: ")
                        else:
                                print("Please provide a valid answer: ")
                if user_option.lower() == 'a':
                        OPTION2()
                elif user_option.lower() == 'b':
                        print("Redirecting to Main Menu...")
                        print(' \n' * 12) #clears screen
                        m_menu()
                else:
                        return 0 #exits program


def OPTION1():  #User receives book recommendation
        i = random.randint(0, 9)
        print("The book of choice is...")
        time.sleep(1)
        print(f"{recommended_books[i]} by {authors[i]} \n")
        ri = 0
        redirect(ri) 


def OPTION2(): #User provides book recommendation
        global user_recommended
        global books_recommended
        print("Please provide a book recomendation below!")
        rec  = input("Your Answer: ")
        user_recommended.append(rec)
        print("\n Thank you for the recommendation! \n It has been added to the list! \n ")
        books_recommended += 1
        ri = 1 #redirect index to change the option screen of rediect function
        redirect(ri)


m_menu()

if books_recommended > 0:
        print("You've recommended a total of [", str(books_recommended), "] books. \n they include: ", user_recommended)
print("Program Terminated")
