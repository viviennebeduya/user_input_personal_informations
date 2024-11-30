with open("./user_informations.txt", "w") as informations:
    print("Please provide the following information:")
    full_name = input ("Full Name: ")
    age = int(input ("Age: "))
    address = input ("Address: ")
    phone_number = input ("Phone Number: ")
    email = input ("Email Address: ")

    informations.write(
        f"Full Name: {full_name}\n"
        f"Age: {age}\n"
        f"Address: {address}\n"
        f"Phone Number: {phone_number}\n"
        f"Email Address: {email}\n"
    )