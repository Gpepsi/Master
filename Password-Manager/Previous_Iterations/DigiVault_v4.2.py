
# - - - DigiVault.py
# - - - Giuseppe Raciti (S3113490)
# - - - Development Started 11_Oct_2022

#THIS ITERATION HAS A COMPLETE AND WORKING ADD USER TO DICTIONARY.......
# DO NOT CHANGE THE ADD USER SECTION OR DICTIONARY DEF'S

from ast import main
import os
import os.path
import time

os.system('cls')

# - Creating a dictionary to store retrievable information - NOT REAL CREDENTIALS
credentials = {
    0: ['Giuseppe', 'Helloworld', 'www.google.com'],
    1: ['Phoenix', 'Huggywuggy', 'www.roblox.com'],
    2: ['Angel', 'Shaka', 'www.youtube.com'],
    3: ['Hannah', 'Loudmouth', 'www.shein.com']
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
    print('Please enter the details required below')
    try:
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
                    print("\n***--- Password cannot be blank ---***")
                    print("Please try again...")
                    os.system('cls')
                    time.sleep(2)
                    adduser()
            else:
                print("\n***--- No Username entered ---***")
                print("Please enter a Username !\n")
                time.sleep(2)
                os.system('cls')
                adduser()
        else:
            print("\n***--- Website URL Missing ---***")
            print("Please enter the website URL !\n")
            time.sleep(2)
            os.system('cls')
            adduser()
    except:
        os.system('cls')
        menu()

# - - Update a stored Username
def update_user():
    sub_title()
    try:
        #- Display the current list of usernames stored
        print('Displaying list of currently stored Usernames')
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
        elif user_id <= len(credentials.items()) - 1:
            # - Confirm the Username to be changed with (y/n) loop
            for key in credentials.keys():
                current_user = credentials[user_id][0]
                print('\nYou are changing the Username', current_user,', with ID:',user_id)    
                confirmation = '1'
                while confirmation != 'y' or 'n':
                    confirmation = input('Is this correct? (y/n): ')
                    try:
                        # - 2nd Confirmation before the username is changed with (y/n) loop
                        confirmation_2 = '1'
                        new_username = input('\nPlease enter the new Username : ')
                        while confirmation_2 != 'y' or 'n':
                            if confirmation == 'y' and new_username !='':
                                try:
                                    print('Update',current_user,', with the new Username: ',new_username) 
                                    confirmation_2 = input('Is this correct? (y/n): ')
                                    if confirmation_2 == 'y':
                                        credentials[user_id] = [new_username]
                                        ammended_user = credentials[user_id][0]
                                        print()
                                        print('*--- Username',ammended_user,'Updated Sucessfully ---*\n')
                                        time.sleep(1)
                                        os.system ('pause')
                                        update_user()  
                                    elif confirmation_2 == 'n':
                                        print('\nReturning to the menu')
                                        time.sleep(2)
                                        update_user()
                                except ValueError:
                                    print("\nInvalid option !!! \nPlease Try Again!")  
                                    time.sleep(2)        
                            elif confirmation == 'n':
                                print('\nReturning to the menu')
                                time.sleep(2)
                                update_user()                        
                            else:
                                print("\nUsername Invalid !!! \nPlease Try Again!")  
                                time.sleep(2)
                                update_user()   
                    except ValueError:
                        print("\nInvalid option !!! \nPlease Try Again!")  
                        time.sleep(2)
        else:
            if user_id > len(credentials.items()) - 1:
                print('\nThat Username ID number does not exist !\nPlease try again....')
                time.sleep(2)
                update_user()                    
    except ValueError:
        print("\n***---No ID number entered ---***")
        print("        Please try again...")
        time.sleep(2)
        os.system('cls')
        update_user()

  

            
    # print('\n', [x[0] for x in credentials.values()], '\n')        
            
            

        
# try:
#     index = int(input('id(?): ')) -1
#     currentusername = table[index][1]
#     try:
#         newusername = input('New Username: ')
#         if len(newusername) != 0:
#             db.update_username(currentusername=currentusername,
#             newusername=newusername,
#             currentpassword=db.get_cred_password(username=currentusername, site=table[index][0]))
#             print("Updated Username Sucessfully!!")
#             time.sleep(1)
#         else:
#             print("New Username Cannot be empty!! \nTry Again!")
#             time.sleep(1)
#     except Exception :
#         pass
      

    
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
    sub_title()
    print('Displaying contents of ALL stored Users\n')
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
    print("(4) Change previously stored Website   ")
    print("(5) View all stored credentials        ")
    print()
    print("(6) EXIT                               ")
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
