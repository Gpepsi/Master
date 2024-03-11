import datetime
import nmap

nm = nmap.PortScanner()

print('\nScanning........ \nPlease Wait.......\n')
time1 = datetime.datetime.now()
print('Scan started at ',time1)

target = "192.168.10.6"
first = 75
last = 140
open_port = 0
closed = 0
filtered = 0
    
for i in range(first,last+1):
    result1 = nm.scan(target,str(i))
    result1 = result1['scan'][target]['tcp'][i]['state']
    result2 = nm.scan(target,str(i))
    result2 = result2['scan'][target]['tcp'][i]['name']
    if result1 == 'open':
        print(f'Port \033[1;34m{i}\033[0;0m is -->|\033[1;37;42m OPEN \033[0;0m|, running',result2,'service')
        open_port += +1
    elif result1 == 'filtered':
        filtered += +1
        print(f'Port \033[1;34m{i}\033[0;0m is -->|\033[1;30;43m FILTERED \033[0;0m|')
    elif result1 == 'closed':
        closed += +1
        print(f'Port \033[1;34m{i}\033[0;0m is -->|\033[1;37;41m CLOSED \033[0;0m|')

time2 = datetime.datetime.now()
total = time2 - time1

print('\nTotal time for scan completed -> ',total)

print('\nthere are \033[1;34m',open_port,'\033[0;0m  Open ports')
print('there are \033[1;34m',filtered,'\033[0;0m  Filtered ports')
print('there are \033[1;34m',closed,'\033[0;0m Closed ports\n')