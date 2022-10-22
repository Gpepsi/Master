import datetime
import platform
import os
from urllib import response
 
os.system('cls')
print('Enter the Network range of the IP adresses to scan')
print('Example..... 192.168.1')
user_input = input('Enter the network IP: ')

ip_parts = user_input.split('.')

network_ip = ip_parts[0]+'.'+ip_parts[1]+'.'+ip_parts[2]+'.'


first_host = int(input('\nEnter the LOWEST value of the last Octet: '))

last_host = int(input('\nEnter the HIGHEST value of the last Octet: '))
last_host += 1

oper = platform.system()

if(oper == 'Windows'):
    ping = 'ping -n 1 '
else:
    ping = 'ping -c 1 '

time1 = datetime.datetime.now()
print('\nScan start at :', time1)
print('Scanning in Progress')

for ip in range(first_host,last_host):
    addr = network_ip + str(ip)
    command = ping + addr
    response = os.popen(command)
    list = response.readlines()
    
    for line in list:
        if(line.count('TTL')):
            print(addr, '--> LIVE')
            break

time2 = datetime.datetime.now()
total = time2 - time1
print('Scanning complete in -->', total)