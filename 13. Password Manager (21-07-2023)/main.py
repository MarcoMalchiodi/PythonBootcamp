from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(): 
    password_entry.delete(0,END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
  
    password_entry.insert(0, password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    
    
        
        
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='One of the fields is empty!')
    else:
        try:
            with open('data.json', 'r') as file:
                #json.dump(new_data, file, indent=4) to erase and write anew
                data = json.load(file)  #to read the file 
                data.update(new_data)   #to append without errors
      
        
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        
        except:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)   
        
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)
    
# ----------------------------SEARCH WEBSITE--------------------------- #

def search_website():
    
    website = website_entry.get()
    
    with open ('data.json', 'r') as file:
        try: #an alternative would be 'if website in data'!
            data = json.load(file)
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        except:
            messagebox.showinfo(title=website, message='No profile was found with this website!')




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=lock_img) #the 100's are the x and y postions
canvas.grid(row=0, column=1)

label1 = Label(text='Website')
label1.grid(column=0,row=1)
label2 = Label(text='Email/Username:')
label2.grid(column=0,row=2)
label3 = Label(text='Password:')
label3.grid(column=0,row=3)

website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'notanaddress@gmail.com') #0...n / END is the number of the character where the text starts
password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search Website', command=search_website)
search_button.grid(column=2, row=1)

window.mainloop()