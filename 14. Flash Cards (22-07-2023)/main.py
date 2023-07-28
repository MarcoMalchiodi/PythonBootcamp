import pandas
import random
from tkinter import *
import csv
BACKGROUND_COLOR = "#B1DDC6"
RANDOM_INDEX = 0





#--------------------------------- CREATING CARDS ---------------------------#

data = pandas.read_csv('C:/Users/Marco/Desktop/project/data/french_words.csv')
french_words = [x for x in data["French"]]
english_words = [x for x in data["English"]]

#file = pandas.read_csv('C:/Users/Marco/Desktop/project/data/known_words.csv')

#-------------------------------- RETRIEVING CARDS --------------------------#

def remove_row_from_csv(csv_file, condition):
    # Read the CSV file into a pandas DataFrame
    df = pandas.read_csv(csv_file)

    # Identify and remove the row(s) matching the condition
    df = df[~((df['French'] == condition[0]) & (df['English'] == condition[1]))]

    # Write the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)

def generate_index():
    global RANDOM_INDEX
    random_num = len(french_words)
    RANDOM_INDEX = random.randint(0,random_num)
    
def generate_random_french():
    global word
    global title
    global data
    
    with open('C:/Users/Marco/Desktop/project/data/known_words.csv', 'a', newline='') as file:
        fields=[french_words[RANDOM_INDEX],english_words[RANDOM_INDEX]]
        writer = csv.writer(file)
        writer.writerow(fields)
    
    csv_file_name = 'C:/Users/Marco/Desktop/project/data/french_words.csv'
    row_to_remove = (french_words[RANDOM_INDEX], english_words[RANDOM_INDEX])
    remove_row_from_csv(csv_file_name, row_to_remove)
    

    
    generate_index()
    title.config(text='French')
    word.config(text=french_words[RANDOM_INDEX])
    
def generate_random_french_wrong():
    global word
    global title
    global current_french
    
    generate_index()
    title.config(text='French')
    word.config(text=french_words[RANDOM_INDEX])
    
    

def flip_english():
    global word
    global title
    global current_french
    
    current_french=french_words[RANDOM_INDEX]
    
    title.config(text='English')
    word.config(text=english_words[RANDOM_INDEX])
    
  


#----------------------------------- UI -------------------------------------#

window = Tk()
window.title('My Flashcard Project')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(height=526,width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
lock_img = PhotoImage(file='C:/Users/Marco/Desktop/project/images/card_front.png')
image_container = canvas.create_image(405,260, image=lock_img)
canvas.grid(column=0,row=0,columnspan=3)

generate_index()
current_french=french_words[RANDOM_INDEX]
#Words to guess
title = Label(text='French', font=('Ariel', 30, 'italic'), bg='white')
title.place(x=350,y=150)
word = Label(text=current_french, font=('Ariel',50,'bold'), bg='white')
word.place(x=300,y=263)



#Options
wrong_image = PhotoImage(file='C:/Users/Marco/Desktop/project/images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_french_wrong)
wrong_button.grid(column=0,row=1)
correct_image = PhotoImage(file='C:/Users/Marco/Desktop/project/images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_french)
correct_button.grid(column=2,row=1)
show_button = Button(text='SHOW',highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_english)
show_button.grid(column=1,row=1)

window.mainloop()