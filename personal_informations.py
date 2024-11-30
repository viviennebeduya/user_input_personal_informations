with open("./user_informations.txt", "w") as informations:
    while True:
        print("Please provide the following information:")
        while True:
            full_name = input ("Full Name: ")
            if full_name:
                break
            print ("Make sure to fill in this information.")
        while True:
            age = input ("Age: ")
            if age:
                break 
            print ("Make sure to fill in this information.")
        while True:
            birthday = input ("Date of Birth: ")
            if birthday:
                break 
            print ("Make sure to fill in this information.")
        while True:
            nationality = input ("Nationality: ")
            if nationality:
                break 
            print ("Make sure to fill in this information.")
        while True:
            address = input ("Address: ")
            if address:
                break 
            print ("Make sure to fill in this information.")
        while True:
            phone_number = input ("Phone Number: ")
            if phone_number:
                break 
            print ("Make sure to fill in this information.")
        while True:
            email = input ("Email Address: ")
            if email:
                break 
            print ("Make sure to fill in this information.")

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
            