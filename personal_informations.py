with open("./user_informations.txt", "w") as informations:
    print("Please provide the following information:")
    full_name = input ("Full Name: ")
    age = int(input ("Age: "))
    address = input ("Address: ")
    phone_number = int(input ("Phone Number: "))
    email = input ("Email Address: ")

    #print ("Please make sure to input accurate informations.")

    informations.write(
        f"Full Name: {full_name}\n"
    )