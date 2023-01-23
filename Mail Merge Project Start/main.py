#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    with open("./Input/Names/invited_names.txt") as names:
        names_list = names.readlines()
        for name in names_list:
            name_stripped = name.replace("\n", "")
            new_letter = contents.replace("[name]", name_stripped)

            print(new_letter)

            with open(f"./Output/letter_for_{name_stripped}.txt", mode="w") as new_file:
                new_file.write(new_letter)

