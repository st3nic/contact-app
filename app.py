import tkinter as tk
import tkinter.messagebox 
import sqlite3

window = tk.Tk()

def search_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    #gets the text from teh name entry field
    name = [name_entry1.get()]
    c.execute('SELECT * FROM contacts WHERE name=?', name)
    result = c.fetchone()
    # check to see if the search return a contact if not display a warning
    if result == None:
        tkinter.messagebox.showerror(title='Search Contacts', message='No contact found')
    else:
        search_result.config(text=result)
    conn.close()
    #clars the field after the serach query has taken place
    name_entry1.delete(0, 'end')
    

def add_contact():
    #checks to see that the entry fields are not empty and then saves the data in a list instead of a plain string to stop SQL injections
    if name_entry.get() and email_entry.get() and phone_entry.get() != '':
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        contact = [name,email,phone]
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        # Insert a row of data
        c.execute('INSERT INTO contacts VALUES (?,?,?)', contact)
        conn.commit()
        conn.close()
        #clears all fields afetr an contact is added, displays a warning if the fields are empty
        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        tkinter.messagebox.showinfo(title='Add Contact', message='Contact Added')
    else:
        tkinter.messagebox.showerror(title='Add Contact', message='You didnt enter any contact information')
    

# to rename the title of the window
window.title('Contacts App')

#to set the size of the window
window.geometry('400x400')

# to stop the window from being resized
window.resizable(0, 0)

# create the frames and place them on the window
left_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
left_frame.place(x=0, y=0, width=200, height=250)

right_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
right_frame.place(x=200, y=0,width=200, height=250)

bottom_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
bottom_frame.place(x=0, y=250,width=400, height=150)

# add the different elements to the frames

#add contact frame
add = tk.Label(right_frame, text='Add Contact')
add.pack()

name_add = tk.Label(right_frame, text='Name')
name_add.pack()

name_entry = tk.Entry(right_frame)
name_entry.pack()

email_label = tk.Label(right_frame, text='Email')
email_label.pack()

email_entry = tk.Entry(right_frame)
email_entry.pack()

phone_label = tk.Label(right_frame, text='Phone Number')
phone_label.pack()

phone_entry = tk.Entry(right_frame)
phone_entry.pack()

button_add = tk.Button(right_frame, text = "Add Contact",command = add_contact)
button_add.pack()

#search contact frame
name_search= tk.Label(left_frame, text='Name')
name_search.pack()

search_label = tk.Label(left_frame, text="Search Contacts")
search_label.pack()

name_entry1 = tk.Entry(left_frame)
name_entry1.pack()

button_search = tk.Button(left_frame, text = "Search",command = search_contacts)
button_search.pack()

#search result frame
search_result = tk.Label(bottom_frame, text=' ')
search_result.pack()

#call the mainloop to display the app
window.mainloop()
