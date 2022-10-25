# - IP_v4_Sweeper.py
# - Giuseppe Raciti (S3113490)
# - Created 17th of October 2022
# - Final Version - - Version 3.0

# - Netscan will use input from the user to scan a set range IPv4 addresses
# and using that information, scan through the range of IP addresses to indicate
# which of the addresses receive a TTL response and displayed to the user with the
# IP address and whether the connection is Alive. 


import datetime
import platform
import os
import re
import time

os.system('cls')

def scan():
    print('\n\033[2;31;40mEnter the NETWORK address to scan\033[0;0m')
    print('Example..... \033[1;37;40m192.168.1.0\033[0;0m\n')
    
    try:
        user_input = 0
        while user_input == 0:
            # - User input network address in the format specified 000.000.000
            user_input = input('\033[2;31;40mEnter the network IP:\033[0;0m ')
            if re.match(r"^[0-9]*[0-9]*[0-9]*\.[0-9]*[0-9]*[0-9]*\.[0-9]*[0-9]*[0-9]*\.[0-9]*[0-9]*[0-9]*$", user_input):
                
                # - The users input is split into separate octets
                ip_parts = user_input.split('.')
                x = int(ip_parts[0])
                y = int(ip_parts[1])
                z = int(ip_parts[2])
                z1 = int(ip_parts[3]) # - This value is ignored
                
                # - Setting the range of each octet to be between 0 and 255
                if (x > -1) and (x < 256):
                    if (y > -1) and (y < 256):
                        if (z > -1) and (z < 256):
                            print("\n\033[2;32;40mNetwork address accepted !\033[0;0m")
                            time.sleep(1)
                            
                            # - With all conditions met, assemble octets into a network address
                            network_ip = ip_parts[0]+'.'+ip_parts[1]+'.'+ip_parts[2]+'.'
                        
                            first_host = -1
                            while first_host == -1:
                                try:
                                    # - User inputs the starting range of the last octet
                                    print("\n\033[2;31;40mSet lowest value of last Octet\033[0;0m")           
                                    first_host = int(input('Enter a value between \033[1;37;40m0-255\033[0;0m: '))
                                    # - Confirm value is within valid range of 0-255
                                    if (first_host > 0) and (first_host < 256):
                                        last_host = -1
                                        
                                        while last_host == -1:   
                                            try:
                                                # - User inputs the end range of the last octet
                                                print("\n\033[2;31;40mSet highest value of last Octet\033[0;0m")           
                                                last_host = int(input('Enter a value between \033[1;37;40m0-255\033[0;0m: '))
                                                # - Confirm value is within valid range of 0-255
                                                if (last_host > 0) and (last_host < 256):
                                                    last_host += 1

                                                    # - To define the operating system the ping will run from
                                                    oper = platform.system()

                                                    if(oper == 'Windows'):
                                                        ping = 'ping -n 1 '
                                                    else:
                                                        ping = 'ping -c 1 '

                                                    # - Create a timestamp of when scan begins
                                                    time1 = datetime.datetime.now()
                                                    print('\nScan started at :', time1)
                                                    print('\n\033[2;32;40mScanning in Progress.......\033[0;0m\nPlease wait........\n')

                                                    # - Set the range of IP addresses to be scanned
                                                    counter = 0
                                                    for ip in range(first_host,last_host):
                                                        addr = network_ip + str(ip)
                                                        command = ping + addr
                                                        response = os.popen(command)
                                                        list = response.readlines()
                                                        
                                                        # - If an address returns an active connection, return a LIVE value    
                                                        
                                                        for line in list:
                                                            if(line.count('TTL')):
                                                                print(addr, '--> \033[1;37;42m| LIVE |\033[0;0m <--')
                                                                counter += 1
                                                                
                                                    # - Create time stamp and calculate the time taken for scan to complete                                                                  
                                                    time2 = datetime.datetime.now()
                                                    total = time2 - time1
                                                    print('\nScanning complete in -->', total, '\n')
                                                    if counter >= 1:
                                                        print('NetScan discovered (\033[1;32;40m',counter,'\033[0;0m) active connections\n')
                                                        time.sleep(2)
                                                    else:
                                                        print('\033[1;37;40mNetScan did not discover any active connections\033[0;0m\n')
                                                        time.sleep(2)
                                                    # - Prompt user to scan again or exit the program
                                                    option = -1
                                                    while option != 'y' or 'n':    
                                                        option = input("Would you like to run another scan ? \033[1;37;40m(y/n)\033[0;0m: ")
                                                        if option == "y":
                                                            print("\nRestarting the scanner, please wait...")
                                                            time.sleep(2) 
                                                            title()
                                                        elif option == 'n':
                                                            print("\nThank you for using NetScan......\nGOODBYE....")
                                                            time.sleep(3) 
                                                            os.system('cls')
                                                            exit()
                                                    
                                                else:
                                                    print("\nOctet Value invalid, please try again...")            
                                                    time.sleep(2)
                                                
                                            except ValueError:
                                                print("\nNo value entered, please try again...")            
                                                time.sleep(2)     
                                    else:
                                        print("\nOctet Value invalid, please try again...")            
                                        time.sleep(2)
                                except ValueError:
                                    print("\nNo value entered, please try again...")            
                                    time.sleep(2)           
                        else:
                            print("\n3rd Octet Value invalid, please try again...")            
                            time.sleep(2)
                            title()
                    else:
                        print("\n2nd Octet Value invalid, please try again...")            
                        time.sleep(2)
                        title()
                else:
                    print("\n1st Octet Value invalid, please try again...")            
                    time.sleep(2)
                    title()
            else:
                print("\nInvalid Network Address, please try again...")            
                time.sleep(2)
                title()
    except:        
        pass  

  
def title():
    os.system('cls')
    print('\033[1;34;40m+'+"-" *55, end="+\n")
    print("\033[1;33;40m ____    __              _______                        ")
    print("|    \  |  |        _   |   ____|                    \033[2;31;40mTM\033[1;33;40m ")
    print("|     \ |  |_____ _| |_ |  |____ _____ _______ ___   __ ")
    print("|      \|  |  _  |_   _||___    |   __|   _   |   \ |  |")
    print("|  |\      |  ___| | |      |   |  |  |  |_|  |    \|  |")
    print("|  | \     | |___  | |   ___|   |  |__|   _   |  |\    |")
    print("|__|  \____|_____| |_|  |_______|_____|__| |__|__| \___|")
    print('\033[5;34;40m+'+"-" *55, end="+\n")
    print('+'+"-" *55, end="+\n\033[0;0m")
    scan()

title()


# - Developments concluded 23_Oct_22
# - Final Ver # 3.0