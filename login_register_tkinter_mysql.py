import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox


w = tk.Tk()
w.title('Register')

connection = mysql.connector.connect(host='localhost',
                                database='hard_dz',
                                user='root',
                                password='') # Connect to the database 

cursor = connection.cursor()


def register():
    # Registers the user, checks whether he entered the password correctly and zips it into the database
    if entry1.get() != '' and entry2.get() != '' and entry3.get() != '': # Checks whether the terms are empty
        if entry2.get() == entry3.get(): # Checks if the passwords are the same
            cursor.execute('INSERT INTO usersreg (login, password) VALUES ("{}", "{}")'.format(entry1.get(), entry2.get())) # Writes data to the database
            connection.commit()
        else:
            messagebox.showinfo('Information', 'Repeat the password')
    else:
        messagebox.showerror('Error', 'The line is empty')
        
        
def login():
    # Logs you into the database and tells you if you are logged in
    output_table = cursor.execute("SELECT login, password FROM usersreg WHERE login = '{}' AND password = '{}' ".format(e1.get(), e2.get())) # Connects to the database and displays what we specified 

    if cursor.fetchone(): # If it displays information from the database, it says whether you are logged in
        messagebox.showinfo('Information', 'You lig in')
    else:
        messagebox.showerror('Information', 'You not lig in')

        
f1 = tk.Frame(master=w, width=300, height=750, bg='blue') # Makes a blue window
f1.pack(fill=tk.BOTH, side=tk.LEFT)

f2 = tk.Frame(master=w, width=300, height=750, bg='yellow') # Makes a yellow window
f2.pack(fill=tk.BOTH, side=tk.RIGHT)

label1 = tk.Label(master=f1, text="login:") # Makes the name of the input field
entry1 = tk.Entry(master=f1, width=60) # Makes a deadline for entering a login

label1.grid(row=1, column=0, sticky="n", padx=10, pady=10)
entry1.grid(row=1, column=1, padx=10, pady=10)

label2 = tk.Label(master=f1, text="password:") # Makes the name of the input field
entry2 = tk.Entry(master=f1, width=60) # Makes a deadline for entering a password

label2.grid(row=2, column=0, sticky=tk.N, padx=10, pady=10)
entry2.grid(row=2, column=1, padx=10, pady=10)

label3 = tk.Label(master=f1, text="password:") # Makes the name of the input field
entry3 = tk.Entry(master=f1, width=60) # Makes a deadline for entering a password

label3.grid(row=3, column=0, sticky=tk.N, padx=10, pady=10)
entry3.grid(row=3, column=1, padx=10, pady=10)


l1 = tk.Label(master=f2,text="login:") # Makes the name of the input field
e1 = tk.Entry(master=f2, width=57) # Makes a deadline for entering a login

l1.grid(row=1, column=0, sticky=tk.N, padx=10, pady=10)
e1.grid(row=1, column=1, padx=15, pady=15)

l2 = tk.Label(master=f2,text="password:") # Makes the name of the input field
e2 = tk.Entry(master=f2, width=57) # Makes a deadline for entering a password

l2.grid(row=2, column=0, sticky=tk.N, padx=10, pady=10)
e2.grid(row=2, column=1, padx=15, pady=15)

b1 = tk.Button(master=f1, width=45, command=register, text="Register") # Makes a button that registers
b1.grid(sticky=tk.N, padx=10)

b2 = tk.Button(master=f2, width=25, command=login,  text="Login") # Makes a button that logs in
b2.grid(sticky=tk.N, pady=15)

w.mainloop()

cursor.close()
connection.close()
