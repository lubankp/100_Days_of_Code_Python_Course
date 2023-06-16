with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as file:
        for line in letter:
            if "[name]" in line:
                line = line.replace("[name]", name.strip())
            file.writelines(line)
