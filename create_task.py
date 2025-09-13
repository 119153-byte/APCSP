#library of Alexandria

import random
import time

"""The purpose of this program is to recommend users books from the programmer's current library
        - we begin with two lists, one providing the recommended titles, another providing their authors
        - Then, the program will ask the user to decide whether they want to recieve  a book recommendation or to provide one.
"""
recommended_books = ["S. ", "Odyssey", "House of leaves", "Fall of the house of Cabal", "The Devil and Ms. Prym", "Moby Dick", "Don Quixote", "Othello", "Ulysses", "The Giver"]
authors = ["Doug Dorst & JJ Abrams", "Homer", "Mark Z. Danielewski", "Johnathan L. Howard", "Paulo Coehlo", "Herman Melville", "Miguel De Cervantes", "Shakespeare", "James Joyce", "Lois Lowry"]
user_recommended = []
user_option = None
books_recommended = 0


print("#####WELCOME TO THE LIBRARY######") #only asked once because its the initial start of the program

def m_menu(u_opt):
        time.sleep(1)
        print("In the library, you can either: \n 1. Recieve a Book Recommendation \n 2. Give a Book Recommendation \n 3. Exit")
        time.sleep(1)
        print("Input your choice of (1) (2) (3) \n")
        while True:
                u_opt = input("Your choice: ")
                try:
                        if int(u_opt) in [1, 2, 3]:
                                break
                except ValueError:
                        print("Please enter a valid number (1, 2, 3): ")
                else:
                        print("Please enter a valid number (1, 2, 3): ")
        if int(u_opt) == 1:
                OPTION1(user_option=None)
        elif int(u_opt) == 2:
                OPTION2()
        elif int(u_opt) == 3:
                print("Closing program....Goodbye!")
                time.sleep(3)

def OPTION1(user_option):  #User recieves book recommendation
        i = random.randint(0, 9)
        print("The book of choice is...")
        time.sleep(1)
        print(f"{recommended_books[i]} by {authors[i]} \n Will that be all? \n Y/N")
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
                m_menu(user_option)
def OPTION2():
        print('2')
m_menu(user_option)
print("program ended")