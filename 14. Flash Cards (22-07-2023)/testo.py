import pandas

file = pandas.read_csv('C:/Users/Marco/Desktop/project/data/french_words.csv')

french_words = [x for x in file["French"]]
english_words = [x for x in file["English"]]

print(english_words)