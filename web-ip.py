banner = ('''\033[91m11111111111111111111111111
11111100111111111100111111
11110001111100111110001111
11000001111000011110000011
10000000111000011100000001
10000000000000000000000001
00000000000000000000000000
00000000000000000000000000
10000000000000000000000001
10000110001000010001100001
11001111111100111111110011
11100111111100111111100111
11111111111111111111111111\033[0m''')
print(banner)
banner = ('''\033[91m #####  #    # ######     ####### #######    #    #     # 
#     # #   #  #     #       #    #         # #   ##   ## 
#       #  #   #     #       #    #        #   #  # # # # 
 #####  ###    ######        #    #####   #     # #  #  # 
      # #  #   #     #       #    #       ####### #     # 
#     # #   #  #     #       #    #       #     # #     # 
 #####  #    # ######        #    ####### #     # #     # 
                                                          
\033[0m''')
print(banner)

import socket

def get_website_ip(website):
    try:
        ip = socket.gethostbyname(website)
        return ip
    except socket.gaierror:
        return "Could not resolve the hostname."

ip_addresses = []
website = input("Enter URL>>")

while True:
    print(f"The IP address of {website} is: {get_website_ip(website)}")
    choice = input("Do you want to check another website's IP address? (y/n): ")
    if choice.lower() != 'y':
        break
    website = input("Enter URL>>")
▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
██████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀▒▒█
█▒▒▒▒▒▒▄▀▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▒▒▒▒██▒▒▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██████████▒▒▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██████████▒▒▄▀▒▒█
█████▒▒▄▀▒▒█████▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██████████▒▒▄▀▒▒█
█████▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█
█████████████████████████████████████████████████████████████████████''')
print(banner)
import socket

def get_website_ip(website):
    try:
        ip = socket.gethostbyname(website)
        return ip
    except socket.gaierror:
        return "Could not resolve the hostname."

ip_addresses = []
print('$[1]get ip address')
print('$[2]Exit')

while True:
    choice = input("Select>>")
    if choice == '2':
        break
    elif choice == '1':
        website = input("Enter URL>>")
        ip_address = get_website_ip(website)
        ip_addresses.append((website, ip_address))

for website, ip_address in ip_addresses:
    print(f"The IP address of {website} is: {ip_address}")
