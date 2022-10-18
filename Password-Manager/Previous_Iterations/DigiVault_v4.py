
# - - - DigiVault.py
# - - - Giuseppe Raciti (S3113490)
# - - - Development Started 11_Oct_2022


import os
import os.path
import time
import csv


# Creating a dictionary to store retrievable information
credentials = {}

def add_values_in_dict(new_dict, key, list_of_values):
    # - Append multiple values to a key in the given dictionary 
    if key not in new_dict:
        new_dict[key] = list()
        new_dict[key].extend(list_of_values)
    return new_dict


# - - Add a new user's credentials
def adduser():
    try:
        while(True):
            website = input("\nEnter the Website URL: ")
            if len(website) != 0:
                username = input("Login Username: ") 
                if len(username) != 0:
                    password = input("Login Password: ")
                    if len(password) != 0:
                        # - Copy the details into "credentials.txt" with the format below
                        f = open("credentials.txt", 'a')   
                        f.write("---------------------------------\n")
                        f.write("URL: ") 
                        f.write(website)
                        f.write("\nUsername: ") 
                        f.write(username)
                        f.write("\nPassword: ")
                        f.write(password)
                        f.write("\n---------------------------------")
                        f.write("\n")
                        f.close()
                        id_val = len(credentials)
                        # - Copy the details into the credentials dictionary                 
                        add_values_in_dict(credentials, id_val, [username, password, website])

                        print(id_val)

                        # Acknowledge successful input of details
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
def update_user():
    os.system('cls')
    print('+', '-----' *7, '+', sep='')
    print('     Username Management Utility')
    print('+', '-----' *7, '+\n', sep='')
    #- Display the current list of usernames stored

    print(credentials)
    # current_user = input(print('Please select which username you wish to modify\n'))
    # try:
    #    if current_user is credentials([0]):
           
       
    # except:
    #    print()     

# - - Update a stored Password




# - - Update a stored URL
def update_pass():
    print(credentials)



# - - View Stored Credentials
def view_all():
    x = credentials.get("Username")
    y = credentials.get("Password")
    z = credentials.get("Website")
    print()
    print("-" * 60)
    print()
    print("Usernames: ", x, "\nPasswords: ", y, "\nWebsites: ", z)
    print()
    print("-" * 60)
    wait = True
    while (True):
        time.sleep(2)
        anykey = input("\n\nPress ENTER to return to the main menu...\n\n")
        if anykey == "":
            wait = False
            os.system('cls')    
            menu()
        else:
            wait = False
            os.system('cls')    
            menu()
            

# - - Title for the begginning of the program
def menu():
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
    print("(4) Change previously stored Website   ")
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
                update_website()
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
