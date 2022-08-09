import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from setuptools import Command


w = tk.Tk()
w.title('Register')

connection = pymysql.connect(
                                host='localhost',
                                database='hard-dz',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor)
    
cursor = connection.cursor()



def button1():

    if entry1.get() != '' and entry2.get() != ''and entry3.get() != '':
        if entry2.get() == entry3.get():
            cursor.execute('INSERT INTO usersreg (login, password) VALUES ("{}", "{}")'.format(entry1.get(), entry2.get()))
            connection.commit()
        else:
            messagebox.showinfo('Information', 'Repeat the password')
    else:
        messagebox.showerror('Information', 'The line is empty')
        

       
def button2():
    login = e1.get()
    password =e2.get()
    y = cursor.execute("SELECT login,password FROM usersreg WHERE login = %s AND password = %s ", (login,password)) 

    if cursor.fetchone():
        messagebox.showinfo('Information', 'You lig in')
    else:
        messagebox.showerror('Information', 'You not lig in')

f1 = tk.Frame(master=w, width=300, height=750, bg='blue')
f1.pack(fill=tk.BOTH, side=tk.LEFT)

f2 = tk.Frame(master=w, width=300, height=750, bg='yellow')
f2.pack(fill=tk.BOTH, side=tk.RIGHT)

label1 = tk.Label(master=f1, text="login::")
entry1 = tk.Entry(master=f1, width=60)

label1.grid(row=1, column=0, sticky="n", padx=10, pady=10)
entry1.grid(row=1, column=1, padx=10, pady=10)

label2 = tk.Label(master=f1, text="password:")
entry2 = tk.Entry(master=f1, width=60)

label2.grid(row=2, column=0, sticky=tk.N, padx=10, pady=10)
entry2.grid(row=2, column=1, padx=10, pady=10)

label3 = tk.Label(master=f1, text="password:")
entry3 = tk.Entry(master=f1, width=60)

label3.grid(row=3, column=0, sticky=tk.N, padx=10, pady=10)
entry3.grid(row=3, column=1, padx=10, pady=10)


l1 = tk.Label(master=f2,text="login:")
e1 = tk.Entry(master=f2, width=57)

l1.grid(row=1, column=0, sticky=tk.N, padx=10, pady=10)
e1.grid(row=1, column=1, padx=15, pady=15)

l2 = tk.Label(master=f2,text="password:")
e2 = tk.Entry(master=f2, width=57)

l2.grid(row=2, column=0, sticky=tk.N, padx=10, pady=10)
e2.grid(row=2, column=1, padx=15, pady=15)

b1 = tk.Button(master=f1, width=45, command=button1, text="Register")
b1.grid(sticky=tk.N, padx=10)

b2 = tk.Button(master=f2, width=25, command=button2,  text="Login")
b2.grid(sticky=tk.N, pady=15)

w.mainloop()

cursor.close()
#cursor.execute = 'SELECT login, password FROM usersreg  ("{}", "{}") '.format(e1.get(), e2.get())
        #