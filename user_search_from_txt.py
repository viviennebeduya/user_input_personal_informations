with open ("./user_informations.txt", "r") as informations:
    lines = informations.readlines()
    for line in lines:
        print (line.strip())