# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
to_replace = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for i in names:
        stripped_name = i.strip("\n")
        new_letter = letter.replace(to_replace, i.strip("\n"))
        with open (f"./Output/ReadyToSend/new_letter_for{stripped_name}.txt", mode="w") as letters:
            letters_to_send = letters.write(new_letter)