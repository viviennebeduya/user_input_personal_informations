search_input = input ("Please enter the full name to search: ")

with open ("./user_informations.txt", "r") as informations:
    lines = informations.readlines()
    
    searched = False
    search_name = []

    for line in lines:
        if search_input in line: #searched, start collect
            searched = True
        if searched: # searched, collect continuous
            search_name.append(line)
        if searched and not line.strip(): # searched + blank line, end
            break


    print (search_name)