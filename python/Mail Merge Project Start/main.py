PLACEHOLDER="[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as ready:
            ready.write(new_letter)
        
        
    