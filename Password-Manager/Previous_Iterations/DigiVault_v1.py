

# - - - DigiVault.py
# - - - Giuseppe Raciti (S3113490)
# - - - Development Started 11_Oct_2022

import os
import time
import csv


# Clearing the terminal
os.system('cls')



# Creating a dictionary to store retrievable information
credentials = {"Username":[], "Password":[],"Site":[]}

csv_filename = 'credentials.csv'
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# - - Add a new user's credentials
def adduser():
    try:
        while(True):
            site = input("\nWebsite or URL: ")
            if len(site) != 0:
                username = input("Username: ") 
                if len(username) != 0:
                    password = input("Password: ")
                    if len(password) != 0:
                        f = open("credentials.txt", 'a')   
                        f.write("---------------------------------\n")
                        f.write("URL: ") 
                        f.write(site)
                        f.write("\nUsername: ") 
                        f.write(username)
                        f.write("\nPassword: ")
                        f.write(password)
                        f.write("\n---------------------------------")
                        f.write("\n")
                        f.close()
                        credentials["Username"].append([username])
                        credentials["Password"].append([password])
                        credentials["Site"].append([site])
                        f = open('credentials.csv','w')
                        w = csv.DictWriter(f,credentials.keys())
                        w.writerow(credentials)
                        f.close()
                        print("\nNew information has been saved !")
                        time.sleep(1)
                        print("\nReturning to the main menu....")
                        time.sleep(2)
                        os.system('cls')
                        menu() 
                    else:
                        print("\n***---Password cannot be blank ---***")
                        print("Please try again...")
                        os.system('cls')
                        time.sleep(2)
                        menu()
                else:
                    print("\n***---No Username entered ---***")
                    print("Please enter a Username !\n")
                    time.sleep(2)
                    os.system('cls')
                    menu()
            else:
                print("\n***---Website URL Missing ---***")
                print("Please enter the website URL !\n")
                time.sleep(2)
                os.system('cls')
                menu()
    except KeyboardInterrupt:
        os.system('cls')
        adduser()
    



# - - Update a stored Username


# - - Update a stored Password




# - - Update a stored URL




# - - View Stored Credentials
def view_all():
    print()
    print("-" * 40)
    print()
    print("Usernames: ", credentials["Username"])
    print("Passwords: ", credentials["Password"])
    print("Sites: ", credentials["Site"])
    print()
    print("-" * 40)
    wait = True
    while (True):
        time.sleep(2)
        anykey = input("\n\nPress ENTER to return to the main menu...\n\n")
        if anykey == "":
            wait = False
        os.system('cls')    
        menu()




# - - Title for the begginning of the program
def menu():
    os.system('cls')
    print("-------------------------------------------------")
    print("|                                               |")    
    print("|           Welcome to the DigiVault            |")    
    print("|              Password Manager                 |")
    print("|                                               |")
    print("|                                               |")
    print("| Developed by: Apps2U                          |")
    print("|          For: DigiCore                        |")
    print("-------------------------------------------------")
    print()
    print("Please make your selection from the menu:")
    print()
    print("(1) Add a new username and password    ")
    print("(2) Change previously stored Username  ")
    print("(3) Change previously stored Password  ")
    print("(4) Change previously stored URL       ")
    print("(5) View all stored credentials        ")
    print()
    print("(6) EXIT                               ")
    print()
    choice()

# - - Menu Choice
def choice():
    control = True
    try:        
        while (True):
            print("Enter a number between (0-6)")
            cmd = int(input("Please make your selection: "))
            if cmd == 1:
                adduser()
            if cmd == 2:
                update_user()
            if cmd == 3:
                update_pass()
            if cmd == 4:
                update_site()
            if cmd == 5:
                view_all()
            if cmd == 6:
                print('\n\nExiting...!')
                time.sleep(1)
                control = False
                quit()
            if cmd > 6:
                print("\nThat is not an option, try again !\n\n")
                time.sleep(2)
                os.system('cls')
                menu()
    
    except ValueError:
        print("\nInvalid option, please try again...")
        time.sleep(2)
        os.system('cls')
        menu()
       

menu()
