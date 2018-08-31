from reception import reception

def registration_checker():
    input_guest = input("Enter is your first name: ")
    input_category = input("Enter your category! Vip or Ordinary: ")

    name = str(input_guest)
    category = str(input_category)

    if name and (category.lower() == "vip"):
        return reception.registration_checker_vip(name)
    elif name and (category.lower() == "ordinary"):
        return reception.registration_checker_ordinary(name)
    else:
        return "May be Check Floor 1 down, This is Andela UG48 Kampala Edition Event"

print(registration_checker())

