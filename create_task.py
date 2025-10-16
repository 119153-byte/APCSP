#Library Of Alexandria

import random
import time

recommended_books = ["S. ", "Odyssey", "House Of Leaves", "Fall Of The House Of Cabal", "The Devil And Ms. Prym", "Moby Dick", "Don Quixote", "Othello", "Ulysses", "The Giver"]
authors = ["Doug Dorst & JJ Abrams", "Homer", "Mark Z. Danielewski", "Johnathan L. Howard", "Paulo Coelho", "Herman Melville", "Miguel De Cervantes", "Shakespeare", "James Joyce", "Lois Lowry"]
user_recommended = []
books_recommended = 0

print("#####Welcome To The Library######") #Only Asked Once Because Its The Initial Start Of The Program

def m_menu():
        time.sleep(1)
        print("In The Library, You Can Either: \n 1. Receive A Book Recommendation \n 2. Give A Book Recommendation \n 3. Exit") #Menu Screen
        time.sleep(1)
        print("Input Your Choice Of (1) (2) (3) \n")
        while True: #While Loop To Ensure The User's Response Doesnt Break Program With Undesired Response
                user_option = input("Your Choice: ")
                try:
                        if int(user_option) in [1, 2, 3]: #When A User's Input Fulfills The Parameter It Continues The Program
                                break 
                except ValueError:
                        print("Please Enter A Valid Number (1, 2, 3): ")
                else:
                        print("Please Enter A Valid Number (1, 2, 3): ")
        if int(user_option) == 1:
                OPTION1()
        elif int(user_option) == 2:
                OPTION2()
        elif int(user_option) == 3:
                print("Closing Program....Goodbye!")
                time.sleep(1)


def redirect(option): #Asks User Whether To Continue Or Close Program At The End Of Each Menu
        if option == 0:
                print(" Will That Be All? \n Y/N")
                while True:
                        user_option = input("Your Answer: ")
                        try:
                                if user_option.upper() in ["Y", "N"]:
                                        break
                        except ValueError:
                                print("Please Provide A Valid Answer: ")
                        else:
                                print("Please Provide A Valid Answer: ")
                if user_option.upper() == "Y":
                        print("Closing Program....Goodbye!")
                else:
                        print("Redirecting To Main Menu...")
                        print(' \n' * 12) #Clears Screen
                        m_menu()
        else: 
                print("Would You Like To: \n A. Provide A New Recommendation \n B. Exit To Main Menu \n C. Exit Program \n")
                while True:                        
                        user_option = input("Your Answer: ")
                        try:
                                if user_option.lower() in ['a', 'b', 'c']:
                                        break
                        except ValueError:
                                print("Please Provide A Valid Answer: ")
                        else:
                                print("Please Provide A Valid Answer: ")
                if user_option.lower() == 'a':
                        OPTION2()
                elif user_option.lower() == 'b':
                        print("Redirecting To Main Menu...")
                        print(' \n' * 12) #Clears Screen
                        m_menu()
                else:
                        return 0 #Exits Program


def OPTION1():  #User Receives Book Recommendation
        i = random.randint(0, 9)
        print("The Book Of Choice Is...")
        time.sleep(1)
        print(f"{recommended_books[i]} By {authors[i]} \n")
        ri = 0
        redirect(ri) 


def OPTION2(): #User Provides Book Recommendation
        global user_recommended
        global books_recommended
        print("Please Provide A Book Recommendation Below!")
        rec  = input("Your Answer: ")
        user_recommended.append(rec)
        print("\n Thank You For The Recommendation! \n It Has Been Added To The List! \n ")
        books_recommended += 1
        ri = 1 #Redirect Index To Change The Option Screen Of Redirect Function
        redirect(ri)


m_menu()

if books_recommended > 0:
        print("You've Recommended A Total Of [", str(books_recommended), "] Books. \n They Include: ", user_recommended)
print("Program Terminated")

