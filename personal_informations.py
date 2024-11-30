import re

with open("./user_informations.txt", "w") as informations:
    while True:
        print("Please provide the following information:")
        while True:
            full_name = input ("Full Name: ")
            if re.fullmatch(r"[A-Za-z\s]+",full_name): #regex-make sure the input is valid only if the pattern is followed
                break
            print ("Make sure to fill this in with valid information (without digits or special characters).")
        while True:
            age = input ("Age: ")
            if age.isdigit():
                break 
            print ("Make sure to fill this in with valid information. Age must be in numbers only.")
        while True:
            birthday = input ("Date of Birth: ")
            if birthday:
                break 
            print ("Make sure to fill in this information.")
        while True:
            nationality = input ("Nationality: ")
            if re.fullmatch(r"[A-Za-z\s]+",nationality):
                break 
            print ("Make sure to fill this in with valid information.")
        while True:
            address = input ("Address: ")
            if "City" in address:
                break 
            print ("Make sure to fill in this information.")
        while True:
            phone_number = input ("Phone Number (+63): ")
            if len(phone_number) == 9 and phone_number.isdigit():
                break 
            print ("Make sure to fill this in with valid information.")
        while True:
            email = input ("Email Address (user@example.com): ")
            if "@" in email and "." in email:
                break 
            print ("Make sure to fill this in with valid information (e.g., user@example.com).")

        informations.write(
            f"Full Name: {full_name}\n"
            f"Age: {age}\n"
            f"Date of Birth: {birthday}\n"
            f"Nationality: {nationality}\n"
            f"Address: {address}\n"
            f"Phone Number: {phone_number}\n"
            f"Email Address: {email}\n"
        )

        informations.write ("\n")

        while True:
            another_person=input("Would you like to input another person's information? (yes/no): ")
            if another_person == "yes":
                break
            elif another_person == "no":
                print ("We have successfully collected all inputs.")
                break
            else:
                print ('Invalid input. Please enter if "yes" or "no"')
                
        if another_person == "no":
            break
            