with open("./user_informations.txt", "w") as informations:
    while True:
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

        another_person=input("Would you like to input another person's information? (yes/no): ")
        if another_person != "yes":
            print ("We have successfully collected all inputs.")
            break