
# - - - DigiVault.py
# - - - Giuseppe Raciti (S3113490)
# - - - Development Started 11_Oct_2022

import os
import os.path
import time

os.system('cls')

# - Creating a dictionary to store retrievable information - NOT REAL CREDENTIALS
credentials = {
    0: ['Tom', 'Helloworld', 'www.google.com'],
    1: ['Jasper', 'Huggywuggy', 'www.roblox.com'],
    2: ['Angel', 'Shakinit', 'www.youtube.com'],
    3: ['Hannah', 'Loudmouth', 'www.shein.com'],
    4: ['Elizabeth', 'Lizzywizzy', 'www.facebook.com']
}

# - Function that applies dictionary key and values
def add_values_in_dict(dict_name, key, list_of_values):
    # - Append multiple values to a key in the given dictionary 
    if key not in dict_name:
        dict_name[key] = list()
        dict_name[key].extend(list_of_values)
    return dict_name

# - - Add a new user's credentials
def adduser():
    os.system('cls')
    sub_title()
    print('   ***** ADD NEW CREDENTIALS TO DATABASE *****\n')
    print('     Please enter the details required below')
    try:
        website = input("\nEnter the Website URL: ")
        if len(website) != 0:
            username = input("Login Username: ") 
            if len(username) != 0:
                password = input("Login Password: ")
                if len(password) != 0:
                    # - Check the dictionary to see if there is a duplicate entry
                    new_entry = [username,password,website]
                    check = (new_entry in credentials.values())
                    if check != True:
                        # - Copy the details into "credentials.txt" with the format below
                        f = open("credentials.txt", 'a')   
                        f.write("\nURL: ") 
                        f.write(website)
                        f.write("\nUsername: ") 
                        f.write(username)
                        f.write("\nPassword: ")
                        f.write(password)
                        f.write("\n---------------------------------")
                        f.close()
                        # - Copy the details into the credentials dictionary  
                        id_val = len(credentials)               
                        add_values_in_dict(credentials, id_val, [username, password, website])
                        # Acknowledge successful input of details
                        print("\nNew information has been saved !")
                        time.sleep(1)
                        print("\nReturning to the main menu....")
                        time.sleep(2)
                        menu() 
                    else:
                        print("\n***--- These credentials already EXIST ---***")
                        print("    Please check the database and try again...\n")
                        time.sleep(2)
                        os.system('pause')
                        menu()    
                else:
                    print("\n***--- Password cannot be blank ---***")
                    print("Please try again...")
                    os.system('cls')
                    time.sleep(2)
                    menu()
            else:
                print("\n***--- No Username entered ---***")
                print("Please enter a Username !\n")
                time.sleep(2)
                os.system('cls')
                menu()
        else:
            print("\n***--- Website URL Missing ---***")
            print("Please enter the website URL !\n")
            time.sleep(2)
            menu()
    except:
        os.system('cls')
        menu()

# - - Update a stored Username
def update_user():
    sub_title()
    try:
        #- Display the current list of usernames stored
        print('     ***** MODIFY USERNAME OF EXISTING USER *****\n')
        print('     Displaying list of currently stored Usernames')
        print('-' *50, sep='')
        for key in credentials.keys():
            user_old = credentials[key][0]
            print ('ID:', key,' - Username:', user_old)
        print('-' *50, '\n', sep='') 
        print('Enter -1, To return to the Main Menu....\n')
        # - Prompt user to change username by entering ID number  
        user_id = int(input("Enter the ID Number of the Username to modify: "))
        if user_id == -1:
            print('\nReturning to the Main Menu.....\nPlease Wait.....')
            time.sleep(3)
            menu() 
        # - Return the values from the dictionary for confirmation    
        elif user_id <= len(credentials.items()) - 1:
            for key in credentials.keys():
                current_user = credentials[user_id][0]
                password = credentials[user_id][1]
                website = credentials[user_id][2]
                
                # - Confirm the details the user is changing
                print('\nYou are changing the Username', current_user,', with ID:',user_id)    
                confirmation = 1
                while confirmation != 'y' or 'n':
                    confirmation = input('Is this correct? (y/n): ')
                    if confirmation == 'n':
                        print('\nReturning to the menu')
                        time.sleep(2)
                        update_user()
                    elif confirmation == 'y':
                        while confirmation == 'y':
                            try:
                                new_username = input('\nPlease enter the new Username : ')
                                if new_username != current_user:
                                    if len(new_username) != 0:
                                        confirmation_2 = '1'
                                        print('\nUpdate',current_user,', with the new Username: ',new_username) 
                                        while confirmation_2 != 'y' or 'n':
                                            try:
                                                confirmation_2 = input('Is this correct? (y/n): ')
                                                if confirmation_2 == 'y':
                                                    # - Update the username in the dictionary
                                                    credentials[user_id] = [new_username,password,website]
                                                    ammended_user = credentials[user_id][0]
                                                    
                                                    # - Update the username in the txt file
                                                    search = current_user
                                                    replace = new_username
                                                    with open('credentials.txt', 'r') as file:
                                                        data = file.read()
                                                        data = data.replace(search, replace)
                                                    with open('credentials.txt', 'w') as file:
                                                        file.writelines(data)                                                  
                                                    
                                                    # - Print confirmation of changes, return to main menu
                                                    print()
                                                    print('*--- Username',ammended_user,'Updated Successfully ---*\n')
                                                    time.sleep(1)
                                                    os.system ('pause')
                                                    update_user()  
                                                elif confirmation_2 == 'n':
                                                    print('\nReturning to the menu')
                                                    time.sleep(2)
                                                    update_user() 
                                            except:
                                                pass 
                                    else:
                                        print('*** Username cannot be blank !!!')
                                        time.sleep(1)                 
                                else:
                                    if new_username == current_user:
                                        print("\n*** New Username cannot be the same ---")
                                        print("*** Please enter another Username...")
                                        time.sleep(2)                
                            except:
                                pass 
        else:
            if user_id > len(credentials.items()) - 1:
                print('\n*** That Username ID number does not exist !\nPlease try again....')
                time.sleep(2)
                update_user()                    
    except ValueError:
        print("\n*** No ID number entered")
        print("*** Please try again...")
        time.sleep(2)
        os.system('cls')
        update_user()

# - - Update a stored Password
def update_pass():
    sub_title()
    try:
        #- Display the current list of usernames stored
        print('     ***** MODIFY PASSWORD OF EXISTING USER *****\n')
        print('     Displaying list of currently stored Usernames')
        print('-' *50, sep='')
        for key in credentials.keys():
            username = credentials[key][0]
            print ('ID:', key,' - Username:', username)
        print('-' *50, '\n', sep='') 
        print('Enter -1, To return to the Main Menu....\n')
        # - Prompt user which username to update password by entering ID number  
        user_id = int(input("Enter the ID of the password you wish to update: "))
        if user_id == -1:
            print('\nReturning to the Main Menu.....\nPlease Wait.....')
            time.sleep(3)
            menu() 
        elif user_id <= len(credentials.items()) - 1:
            for key in credentials.keys():
                username = credentials[user_id][0]
                old_pass = credentials[user_id][1]
                website = credentials[user_id][2]
                
                # - Confirm the Username of the password to update with (y/n) loop
                print('\nYou are changing the password for', username,'that is currently \"',old_pass,'\"')    
                confirmation = '1'
                while confirmation != 'y' or 'n':
                    confirmation = input('Is this correct? (y/n): ')
                    if confirmation == 'n':
                        print('\nReturning to the menu')
                        time.sleep(2)
                        update_pass()
                    elif confirmation == 'y':
                        while confirmation == 'y':
                            try:
                                new_pass = input('\nPlease enter the new password for this user: ')
                                if new_pass != old_pass:
                                    if len(new_pass) != 0:
                                        confirmation_2 = '1'
                                        print('\nUpdate',username,', with the new password: ',new_pass)
                                        while confirmation_2 != 'y' or 'n':
                                            try:
                                                confirmation_2 = input('Is this correct? (y/n): ')    
                                                if confirmation_2 == 'y':
                                                    # - Update the password in the dictionary
                                                    credentials[user_id] = [username,new_pass,website]
                                                    ammended_pass = credentials[user_id][1]
                                                    
                                                    # - Update the username in the txt file
                                                    search = old_pass
                                                    replace = new_pass
                                                    with open('credentials.txt', 'r') as file:
                                                        data = file.read()
                                                        data = data.replace(search, replace)
                                                    with open('credentials.txt', 'w') as file:
                                                        file.writelines(data)  
                                                    
                                                    # - Print confirmation of changes, return to main menu    
                                                    print()
                                                    print('*--- The password for',username,\
                                                    'was successfully updated to',ammended_pass,' ---*\n')
                                                    time.sleep(1)
                                                    os.system ('pause')
                                                    update_pass()  
                                                elif confirmation_2 == 'n':
                                                    print('\nReturning to the menu')
                                                    time.sleep(2)
                                                    update_pass()      
                                            except:
                                                pass 
                                    else:
                                        print('*** Password cannot be blank !!!')
                                        time.sleep(2)
                                else:
                                    if new_pass == old_pass:
                                        print("\n*** New Password cannot be the same ---")
                                        print("*** Please enter another Password...")
                                        time.sleep(2)          
                            except:
                                pass                              
        else:
            if user_id > len(credentials.items()) - 1:
                print('\nThat Username ID number does not exist !\nPlease try again....')
                time.sleep(2)
                update_pass()                    
    except ValueError:
        print("\n***---No ID number entered ---***")
        print("        Please try again...")
        time.sleep(2)
        os.system('cls')
        update_pass()

# - - Update a stored URL
def update_website():
    sub_title()
    try:
        #- Display the current list of usernames stored
        print('     ***** MODIFY WEBSITE OF EXISTING USER *****\n')
        print('     Displaying list of currently stored Usernames')
        print('-' *50, sep='')
        for key in credentials.keys():
            username = credentials[key][0]
            current_website = credentials[key][2]
            print ('ID:', key,' - Website: ', current_website,' - Username:', username)
        print('-' *50, '\n', sep='') 
        print('Enter -1, To return to the Main Menu....\n')
        # - Prompt user which username to update password by entering ID number  
        user_id = int(input("Enter the ID of the website you wish to update: "))
        if user_id == -1:
            print('\nReturning to the Main Menu.....\nPlease Wait.....')
            time.sleep(3)
            menu() 
        elif user_id <= len(credentials.items()) - 1:
            for key in credentials.keys():
                username = credentials[user_id][0]
                password = credentials[user_id][1]
                old_website = credentials[user_id][2]
                
                # - Confirm the website of the username to update with (y/n) loop
                print('\nYou are changing the website for', username,'that is currently \"',old_website,'\"')    
                confirmation = '1'
                while confirmation != 'y' or 'n':
                    confirmation = input('Is this correct? (y/n): ')
                    if confirmation == 'n':
                        print('\nReturning to the menu')
                        time.sleep(2)
                        update_website()
                    elif confirmation == 'y':
                        while confirmation == 'y':
                            try:
                                new_website = input('\nPlease enter the new website for this user: ')
                                if new_website != old_website:
                                    if len(new_website) != 0:
                                        confirmation_2 = '1'
                                        print('\nUpdate',username,', with the new website: ',new_website)
                                        while confirmation_2 != 'y' or 'n':
                                            try:
                                                confirmation_2 = input('Is this correct? (y/n): ')    
                                                if confirmation_2 == 'y':
                                                    # - Update the website in the dictionary
                                                    credentials[user_id] = [username,password,new_website]
                                                    ammended_website = credentials[user_id][2]
                                                    
                                                    # - Update the username in the txt file
                                                    search = old_website
                                                    replace = new_website
                                                    with open('credentials.txt', 'r') as file:
                                                        data = file.read()
                                                        data = data.replace(search, replace)
                                                    with open('credentials.txt', 'w') as file:
                                                        file.writelines(data)  
                                                    
                                                    # - Print confirmation of changes, return to main menu    
                                                    print()
                                                    print('*--- The website for',username,\
                                                    'was successfully updated to',ammended_website,' ---*\n')
                                                    time.sleep(1)
                                                    os.system ('pause')
                                                    update_website()  
                                                elif confirmation_2 == 'n':
                                                    print('\nReturning to the menu')
                                                    time.sleep(2)
                                                    update_website()      
                                            except:
                                                pass 
                                    else:
                                        print('*** Website cannot be blank !!!')
                                        time.sleep(2)
                                else:
                                    if new_website == old_website:
                                        print("\n*** New Website cannot be the same ---")
                                        print("*** Please enter another URL...")
                                        time.sleep(2)          
                            except:
                                pass                              
        else:
            if user_id > len(credentials.items()) - 1:
                print('\nThat Username ID number does not exist !\nPlease try again....')
                time.sleep(2)
                update_website()                    
    except ValueError:
        print("\n***---No ID number entered ---***")
        print("        Please try again...")
        time.sleep(2)
        os.system('cls')
        update_website()
    
# - - View Stored Credentials
def view_all():
    sub_title()
    print('     ***** WELCOME TO THE DATABASE *****\n')
    print('    Displaying contents of ALL stored Users\n')
    print('-' *50, sep='')
    for key in credentials.keys():
        user_name = credentials[key][0]
        user_pass = credentials[key][1]        
        user_site = credentials[key][2]       
        print ('ID:', key,' - Username:', user_name,' - Password:', user_pass,' - Website:', user_site)
    print('-' *50, '\n', sep='') 
    time.sleep(2)   
    os.system ('pause')
    menu()    

# - - View the contents of the TXT file        
def view_txt():
    sub_title()
    print('     ***** WELCOME TO THE DATABASE *****\n')
    print('   Displaying contents of the TXT backup File')
     
    # - Open and read the contents of the TXT file
    txt_file = open('credentials.txt', 'r')
    
    # - Read the contents of file into a string
    display_txt = txt_file.read()
    
    # - Display the contents of the TXT file
    print(display_txt)
    
    # - Close the file
    txt_file.close()
   
    time.sleep(2)   
    os.system ('pause')
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
    print("Please make your selection from the menu:        ")
    print()
    print("(1) Add a new username and password              ")
    print("(2) Change previously stored Username            ")
    print("(3) Change previously stored Password            ")
    print("(4) Change previously stored Website             ")
    print("(5) View all stored credentials                  ")
    print("(6) View stored credentials of TXT file          ")    
    print()
    print("(7) EXIT                                         ")
    print()
    choice()

# - Title for sub menus in modification areas
def sub_title():
    os.system('cls')
    print('+', '-' *50, '+', sep='')
    print('|            User Management Utility               |')
    print('+', '-' *50, '+\n', sep='')

# - - Menu Choice
def choice():
    control = True
    try:        
        while (True):
            print("Enter a number between (0-7)")
            cmd = int(input("Please make your selection: "))
            if cmd <= 0:
                print("\nThat is not an option, try again !\n\n")
                time.sleep(2)
                os.system('cls')
                menu()
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
                view_txt()                
            if cmd == 7:
                print('\n\nExiting...!')
                time.sleep(1)
                control = False
                exit()
            if cmd > 7:
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