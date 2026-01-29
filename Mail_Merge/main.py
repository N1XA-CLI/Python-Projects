#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names:
        for name in names.readlines():
            name = name.rstrip("\n")
            ready_letter = f"""Dear {name},

You are invited to my birthday this Saturday.

Hope you can make it!

Angela"""
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
                letter.write(ready_letter)

