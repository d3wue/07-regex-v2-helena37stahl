import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here



#check valid IPv6 Adresses
regv6 = re.compile('^([0-9a-f]{4}:){7}([0-9a-f]{4})$')

#check valid IPv4 Adresses
regv4 = re.compile('^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){3}((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2}))$')


ipv6Counter = 0
ipv4Counter = 0
invalidCounter = 0

for ip in ipAddresses:
    m = regv6.match(ip)
    m2 = regv4.match(ip)
    if m != None:
        ipv6Counter += 1
    elif m2 != None:
        ipv4Counter += 1
    else:
        invalidCounter += 1

print(f'Valid IPv6 Adresses: {ipv6Counter}')
print(f'Valid IPv4 Adresses: {ipv4Counter}')
print(f'Invalid IP Adresses: {invalidCounter}')









