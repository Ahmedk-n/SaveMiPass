import os
from db import *
from masterpass import *
import time


know_pass = input("Enter the master password : ")
if know_pass == master_password :

    def menu():
        print("[1] Create a new passwod ")
        print("[2] Retrieve a password ")
        print("[3] Find all passwords connected to an e-mail. ")
        print("[4] See User name connected to a website.")
        print("[5] Delete a record ")
        print("[6] Help file")
        print("[0] Exit")

    menu()

    option = input("What is your option?")

    while option.lower() != 'exit' :
        if option == '1' :
            add_new()
        elif option == "2" :
            get_password()
        elif option == "3":
            get_websiteMail()
        elif option == "4":
            get_userName()
        elif option == "5":
            delete_item()
        elif option == "6":
            os.startfile(os.listdir()[3])
        else:
            print("Invalid input")
        break
        
    print("Thanks for using our app")
    print("Use again?")
    again = input(">")
    if again.lower() == "yes":
        menu()
    else:
        print("We would love to get you your feedback on discord (Ahmedk.n#9375)")
    
else :
    print("No Hope")



time.sleep(5)