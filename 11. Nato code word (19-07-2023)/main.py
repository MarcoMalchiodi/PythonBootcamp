import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

dictionary = {data.letter[x]:data.code[x] for x in data.index}

def generate_phonetic():
    user_input = list((input("Type your word: ")).upper())
    nato_code = []

    try:
        for letter in user_input:
            nato_code.append(f"{letter} : {dictionary[letter]}")
    except:
        print('Sorry, only letters allowed')
        generate_phonetic()
    else:
        print(nato_code)




