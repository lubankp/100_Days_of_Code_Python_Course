import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_loop = True
while is_loop:
    word = input("Choose word: ").upper()
    try:
        code_list = [nato_letter_dict[letter] for letter in word]
    except:
        print('Sorry, only letters in alphabet please.')
    else:
        is_loop = False

print(code_list)
