# - - - DigiVault.py
# - - - Giuseppe Raciti (S3113490)
# - - - Development Started 11_Oct_2022

from ast import Return
import os
import os.path
import time

# retrieve and display the current working directory
cwd = os.getcwd()
print("\nCurrent working directory: {0}\n\n".format(cwd))

# Creating a dictionary to store retrievable information
credentials = {}

# - - Menu
def title():
    print("----------------------------------------------")
    print("   Welcome to the DigiVault Password Manager  ")
    print("----------------------------------------------")
    print()

def menu():
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
                        if os.path.exists("credentials.txt"):
                            with open('credentials.txt', 'w') as f:
                                f.write("---------------------------------\n")
                                f.write("URL: ") 
                                f.write(site)
                                f.write("\nUsername: ") 
                                f.write(username)
                                f.write("\nPassword: ")
                                f.write(password)
                                f.write("\n---------------------------------")
                                f.write("\n")
                                f.close
                                new_values = {'Username': username, 'Password': password, 'Site': site}
                                credentials.update(new_values)
                            print("\nNew information has been saved !")
                            time.sleep(2)
                            print("\nReturning to the main menu....")
                            time.sleep(2)
                            menu() 
                        else:
                            menu()    
                    else:
                        print("\n***---Password cannot be blank !---***")
                        print("Please try again...")
                        time.sleep(1)
                        return
                else:
                    print("\n***---No Username entered !---***")
                    print("Please enter a Username !\n")
                    time.sleep(1)
                    return
            else:
                print("Website URL Missing !---***")
                print("Please enter the website URL !\n")
                time.sleep(1)
                return
    except KeyboardInterrupt:
        adduser()
    



# - - Update a stored Username

# - - Update a stored Password

# - - Update a stored URL

# - - View Stored Credentials
def view_all():
    print()
    print("-" * 40)
    print()
    print(credentials)
    print()
    print("-" * 40)
    wait = True
    while (True):
        time.sleep(2)
        anykey = input("\n\nPress any key to return to the main menu...\n\n")
        if anykey == "":
            wait = False
            menu()




# - - Menu Choice
def choice():
    control = True
    try:        
        while (True):
            cmd = int(input("Make your selection: "))
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
                menu()
    
    except ValueError:
        print("Invalid choice, please try again...")
        time.sleep(2)
        menu()
        
    except KeyboardInterrupt:
        print('\n\nNo choice was entered, try again...')
        time.sleep(2)
        menu()

title()
menu()
