search_input = input ("Please enter the full name to search: ")

with open ("./user_informations.txt", "r") as informations:
    lines = informations.readlines()
    
    search_name = []
    for line in lines:
        if search_input in line:
            search_name.append(line)

    print (search_name)