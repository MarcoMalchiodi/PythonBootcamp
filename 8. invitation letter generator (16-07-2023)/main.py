#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

file_temp = open('C:/Users/Marco/Desktop/project/Input/Letters/starting_letter.txt')
template = file_temp.read()
file_temp.close()

namefile = open('C:/Users/Marco/Desktop/project/Input/Names/invited_names.txt')
names = namefile.readlines()
namefile.close()

names = [name.strip() for name in names]


for x in names:
    file = open(f"{x}'s invitation letter.txt", mode='w')
    old_word = '[name]'
    new_letter = template.replace(old_word,x)
    file.write(new_letter)
    file.close()