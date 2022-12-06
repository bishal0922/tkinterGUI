from tkinter import *
import sqlite3
import os

# add tkinter window
root = Tk()
root.title("Car Rental Database")
root.geometry("400x400")

# create a database or connect to one
conn = sqlite3.connect('finalpart3.db')

# create cursor
c = conn.cursor()

# add some text
text = Label(root, text="Add some text")
text.pack()

root.mainloop()