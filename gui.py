from tkinter import *
import sqlite3
import os

# our courier font
ourFont = "Courier"

'''
Definitions
'''
def req1_result(Frame, select, from_table, where):
    #connect to the database
    
    conn = sqlite3.connect('finalpart3 copy.db')
    c = conn.cursor()

    #execute the query
    if len(where) != 0:
        c.execute("SELECT " + select + " FROM " + from_table + " WHERE " + where)
    else:
        c.execute("SELECT " + select + " FROM " + from_table)

    #get the results
    results = c.fetchall()
    print(results)

    #Frame.config(text=results)

    # update Frame with results
    return


def test_works():
    print("it works")
    return

def req1_func():
    #open a new window
    req1_window = Toplevel()
    req1_window.title("Request 1")
    req1_window.geometry("500x500")

    #Frame to contain the input fields and output fields
    query_frame = Frame(req1_window)
    output_frame = Frame(req1_window)

    #create a label  -> Request 1
    req1_label = Label(query_frame, text="Request 1", font=ourFont)
    req1_label.grid(row=0, column=0, columnspan=2, padx=200, pady=10)

    #create a label  -> SELECT
    select_label = Label(query_frame, text="SELECT", font=ourFont)
    select_label.grid(row=1, column=0, padx=10, pady=10)
    #create an entry box
    select_label_txt = Entry(query_frame, font=ourFont)
    select_label_txt.grid(row=1, column=1, padx=10, pady=10)
    
    #create a label  -> FROM
    from_label = Label(query_frame, text="FROM", font=ourFont)
    from_label.grid(row=2, column=0, padx=10, pady=10)
    #create an entry box
    from_label_txt = Entry(query_frame, font=ourFont)
    from_label_txt.grid(row=2, column=1, padx=10, pady=10)
    
    #create a label  -> WHERE
    where_label = Label(query_frame, text="WHERE", font=ourFont)
    where_label.grid(row=3, column=0, padx=10, pady=10)
    #create an entry box
    where_label_txt = Entry(query_frame, font=ourFont)
    where_label_txt.grid(row=3, column=1, padx=10, pady=10)
    
    results_label = Label(output_frame, text="", font=ourFont)
    results_label.grid(row=0, column=0, padx=10, pady=10)

    # button to submit the query
    submit_button = Button(query_frame, text="Submit", font=ourFont, command=lambda: req1_result(results_label, select_label_txt.get(), from_label_txt.get(), where_label_txt.get()))
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    

   

    query_frame.grid(row=0, column=0)
    output_frame.grid(row=1, column=0)

    return

# add tkinter window
root = Tk()
root.title("Car Rental Database")
root.geometry("500x500")

# create a database or connect to one
conn = sqlite3.connect('finalpart3.db')

# create cursor
c = conn.cursor()



# add some text
text = Label(root, text="Add some text", font=ourFont)
text.grid(row=0, column=0, columnspan=2, padx=180, pady=10)
#horizontally center text


# button to add a record
req1 = Button(root, text="SELECT-FROM-WHERE Query", font=ourFont, command=req1_func)
req1.grid(row=1, column=0, columnspan=2, pady=10)

# button to add a record
req2 = Button(root, text="Button1", font=ourFont,command=test_works )
req2.grid(row=3, column=0, columnspan=2, pady=10)

# button to add a record
req3 = Button(root, text="Button1", font=ourFont, command=test_works)
req3.grid(row=5, column=0, columnspan=2, pady=10)

# button to add a record
req4 = Button(root, text="Button1", font=ourFont, command=test_works)
req4.grid(row=7, column=0, columnspan=2, pady=10)

# button to add a record
req5 = Button(root, text="Button1", font=ourFont, command=test_works)
req5.grid(row=9, column=0, columnspan=2, pady=10)



root.mainloop()
