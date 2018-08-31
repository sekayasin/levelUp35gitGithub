
# Open our Registrations file in read mode
vip_reg_file = open('vip_list.txt', 'r')
ordinary_reg_file = open('ordinary_list.txt', 'r')

# Declare variables to hold users confirmed on Guest list and Ordinary list
vip_guests = []
ordinary_guests = []

# Read our Registrations file
vip_list = vip_reg_file.readlines()
ordinary_list = ordinary_reg_file.readlines()

# Remove the new line character caused by readlines method
for name in vip_list:
    vip_guests.append(name.rstrip('\n'))

for name in ordinary_list:
    ordinary_guests.append(name.rstrip('\n'))


def registration_checker_vip(name):
    for guest in vip_guests:
        if guest.lower().find(name.lower()) is not -1:
            return guest + ", VIP"

    for guest in vip_guests:
        if guest.lower().find(name.lower()) == -1:
            return "Not Registered"

def registration_checker_ordinary(name):
    for guest in ordinary_guests:
        if guest.lower().find(name.lower()) is not -1:
            return guest 
    
    for guest in ordinary_guests:
        if guest.lower().find(name.lower()) == -1:
            return "Not Registered"

# Flush and close our Registrations files
vip_reg_file.close()
ordinary_reg_file.close()   

# print(registration_checker_vip("alex"))
# print(registration_checker_ordinary("alex"))

# print(vip_guests)
# print()
# print(ordinary_guests)
