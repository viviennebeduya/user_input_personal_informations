search_input = input ("Please enter the full name to search: ")

with open ("./user_informations.txt", "r") as informations:
    lines = informations.readlines()
    for line in lines:
        print (line.strip())