search_input = input ("Enter the full name to search: ")

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

    else:
        print (f"There's no {search_input} in this file.")

if searched:
    print (f"\nHere are the informations for {search_input}: \n")
for list in search_name:
    print (list.strip())