from tkinter import *
import sqlite3
import os

# our courier font
ourFont = "Courier"

'''
Definitions
'''
def works():
    print("works")

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

    Frame.config(text="Check the console for the results")

    # update Frame with results
    return

def req2_result(Frame, name, phone):
    #connect to the database
    
    conn = sqlite3.connect('finalpart3 copy.db')
    c = conn.cursor()

    #execute the query
    c.execute("INSERT INTO Customer VALUES (NULL, ?, ?)", (name, phone))

    #get the results
    results = c.fetchall()
    print("updated the database with " + name + " " + phone) 
    Frame.config(text="Updated the database\n" + name + " " + phone)

    #if you want to commit the changes
    #conn.commit()

    return

def req3_result(Frame, vin, desc, year, type, cat):
    #connect to the database

    conn = sqlite3.connect('finalpart3 copy.db')
    c = conn.cursor()

    #execute the query
    c.execute("INSERT INTO Vehicle VALUES (?, ?, ?, ?, ?)", (vin, desc, year, type, cat))

    #get the results
    results = c.fetchall()
    print("updated the database with " + vin + " " + desc + " " + year + " " + type + " " + cat)
    Frame.config(text="Updated the database\n" + vin + " " + desc + " " + year + " " + type + " " + cat)

    #if you want to commit the changes
    #conn.commit()

    return

def req4_result(Frame, CustID, VehicleId, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount, PaymentDate):
    #connect to the database

    conn = sqlite3.connect('finalpart3 copy.db')
    c = conn.cursor()

    #execute the query
    c.execute("INSERT INTO RENTAL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (CustID, VehicleId, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount, PaymentDate, 'NULL'))

    #get the results
    results = c.fetchall()
    print("updated the database with " + CustID + " " + VehicleId + " " + StartDate + " " + OrderDate + " " + RentalType + " " + Qty + " " + ReturnDate + " " + TotalAmount + " " + PaymentDate)
    Frame.config(text="Updated the database\n" + CustID + " " + VehicleId + " " + StartDate + " " + OrderDate + " " + RentalType + " " + Qty + " " + ReturnDate + " " + TotalAmount + " " + PaymentDate)

    #if you want to commit the changes
    #conn.commit()
    return

def req5_result(Frame, CustName, VehicleID, ReturnDate):
    #connect to the database

    conn = sqlite3.connect('finalpart3 copy.db')
    c = conn.cursor()

    #execute the query
    query = "SELECT R.CustID, R.TotalAmount FROM RENTAL AS R JOIN CUSTOMER AS C ON R.CustID = C.CustID WHERE R.ReturnDate = \"" + ReturnDate + "\" AND C.Name= \"" + CustName + "\"  AND R.VehicleID = '" + VehicleID + "'"
    
    print(query)
    c.execute(query)
    
    #get the results
    results = c.fetchall()

    c.execute("UPDATE RENTAL SET Returned = 1, PaymentDate = CASE WHEN PaymentDate = 'NULL' THEN '" + ReturnDate + "' END WHERE CustID = " + str(results[0][0]) + " AND ReturnDate = '" + ReturnDate + "' AND VehicleID = '" + VehicleID + "'")
    print(c.fetchall())
    Frame.config(text=("Payment Due: \n" + str(results[0][1]) + "\n Updated the database.."))

    #A. Hernandez G. Clarkson
    #JM3KE4DYF0441471 19VDE1F3XEE414842
    #2019-09-13 2019-11-15
    
    #if you want to commit the changes
    conn.commit()
    return

def req1_func():
    #open a new window
    req1_window = Toplevel()
    req1_window.title("Select-From-Where Query")
    req1_window.geometry("500x500")

    #Frame to contain the input fields and output fields
    query_frame = Frame(req1_window)
    output_frame = Frame(req1_window)

    #create a label  -> Request 1
    req1_label = Label(query_frame, text="SELECT Query", font=ourFont)
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

def req2_func():
    #this is to add a new customer
    req2_window = Toplevel()
    req2_window.title("Add a new Customer")
    req2_window.geometry("600x500")

    #Frame to contain the input fields and output fields
    query_frame = Frame(req2_window)
    output_frame = Frame(req2_window)

    #create a label  -> Request 1
    req1_label = Label(query_frame, text="Add a new Customer", font=ourFont)
    req1_label.grid(row=0, column=0, columnspan=2, padx=200, pady=10)

    #create a label  -> Cust_name
    cust_name_label = Label(query_frame, text="Name: ", font=ourFont)
    cust_name_label.grid(row=1, column=0, padx=10, pady=10)
    #create an entry box
    cust_name_label_txt = Entry(query_frame, font=ourFont)
    cust_name_label_txt.grid(row=1, column=1, padx=10, pady=10)
    
    #create a label  -> FROM
    cust_phone_label = Label(query_frame, text="Phone: ", font=ourFont)
    cust_phone_label.grid(row=2, column=0, padx=10, pady=10)
    #create an entry box
    cust_phone_label_txt = Entry(query_frame, font=ourFont)
    cust_phone_label_txt.grid(row=2, column=1, padx=10, pady=10)
    
    results_label = Label(output_frame, text="", font=ourFont)
    results_label.grid(row=0, column=0, padx=10, pady=10)

    # button to submit the query
    submit_button = Button(query_frame, text="Submit", font=ourFont, command=lambda: req2_result(results_label, cust_name_label_txt.get(), cust_phone_label_txt.get()))
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    query_frame.grid(row=0, column=0)
    output_frame.grid(row=1, column=0)

    return 

def req3_func():
    #this is to add a new customer
    req3_window = Toplevel()
    req3_window.title("Add a new Vehicle")
    req3_window.geometry("600x500")

    #Frame to contain the input fields and output fields
    query_frame = Frame(req3_window)
    output_frame = Frame(req3_window)

    #create a label  -> Request 1
    req1_label = Label(query_frame, text="Add a new Vehicle", font=ourFont)
    req1_label.grid(row=0, column=0, columnspan=2, padx=200, pady=10)

    #VehicleID(VIN), Description, year, type, category

    #create a label  -> VIN
    vin_name_label = Label(query_frame, text="VehicleID: ", font=ourFont)
    vin_name_label.grid(row=1, column=0, padx=10, pady=10)
    #create an entry box
    vin_name_label_txt = Entry(query_frame, font=ourFont)
    vin_name_label_txt.grid(row=1, column=1, padx=10, pady=10)
    
    #create a label  -> DSEC
    desc_label = Label(query_frame, text="Description: ", font=ourFont)
    desc_label.grid(row=2, column=0, padx=10, pady=10)
    #create an entry box
    desc_label_txt = Entry(query_frame, font=ourFont)
    desc_label_txt.grid(row=2, column=1, padx=10, pady=10)

    #create a label  -> YEAR
    year_label = Label(query_frame, text="Year: ", font=ourFont)
    year_label.grid(row=3, column=0, padx=10, pady=10)
    #create an entry box
    year_label_txt = Entry(query_frame, font=ourFont)
    year_label_txt.grid(row=3, column=1, padx=10, pady=10)
    
    #create a label  -> TYPE
    type_label = Label(query_frame, text="Type: ", font=ourFont)
    type_label.grid(row=4, column=0, padx=10, pady=10)
    #create an entry box
    type_label_txt = Entry(query_frame, font=ourFont)
    type_label_txt.grid(row=4, column=1, padx=10, pady=10)

    #create a label  -> CATEGORY
    category_label = Label(query_frame, text="Category: ", font=ourFont)
    category_label.grid(row=5, column=0, padx=10, pady=10)
    #create an entry box
    category_label_txt = Entry(query_frame, font=ourFont)
    category_label_txt.grid(row=5, column=1, padx=10, pady=10)
    

    results_label = Label(output_frame, text="", font=ourFont)
    results_label.grid(row=0, column=0, padx=10, pady=10)

    # button to submit the query
    submit_button = Button(query_frame, text="Submit", font=ourFont, command=lambda: req3_result(results_label, vin_name_label_txt.get(), desc_label_txt.get(), year_label_txt.get(), type_label_txt.get(), category_label_txt.get()))
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    query_frame.grid(row=0, column=0)
    output_frame.grid(row=1, column=0)

    return 

def req4_func():
    #this is to add a new Reservation
    req4_window = Toplevel()
    req4_window.title("Add a new Reservation")
    req4_window.geometry("600x700")

    #Frame to contain the input fields and output fields
    query_frame = Frame(req4_window)
    output_frame = Frame(req4_window)

    #create a label  -> Request 1
    req1_label = Label(query_frame, text="Add a new Reservation", font=ourFont)
    req1_label.grid(row=0, column=0, columnspan=2, padx=200, pady=10)


    #CREATE ALL THE LABELS AND ENTRY BOXES

    CustID_name_label = Label(query_frame, text="CustID: ", font=ourFont)
    CustID_name_label.grid(row=1, column=0, padx=10, pady=10)
    CustID_name_label_txt = Entry(query_frame, font=ourFont)
    CustID_name_label_txt.grid(row=1, column=1, padx=10, pady=10)

    VehicleId_name_label = Label(query_frame, text="VehicleId: ", font=ourFont)
    VehicleId_name_label.grid(row=2, column=0, padx=10, pady=10)
    VehicleId_name_label_txt = Entry(query_frame, font=ourFont)
    VehicleId_name_label_txt.grid(row=2, column=1, padx=10, pady=10)

    StartDate_name_label = Label(query_frame, text="StartDate: ", font=ourFont)
    StartDate_name_label.grid(row=3, column=0, padx=10, pady=10)
    StartDate_name_label_txt = Entry(query_frame, font=ourFont)
    StartDate_name_label_txt.grid(row=3, column=1, padx=10, pady=10)

    OrderDate_name_label = Label(query_frame, text="OrderDate: ", font=ourFont)
    OrderDate_name_label.grid(row=4, column=0, padx=10, pady=10)
    OrderDate_name_label_txt = Entry(query_frame, font=ourFont)
    OrderDate_name_label_txt.grid(row=4, column=1, padx=10, pady=10)

    RentalType_name_label = Label(query_frame, text="RentalType: ", font=ourFont)
    RentalType_name_label.grid(row=5, column=0, padx=10, pady=10)
    RentalType_name_label_txt = Entry(query_frame, font=ourFont)
    RentalType_name_label_txt.grid(row=5, column=1, padx=10, pady=10)

    Qty_name_label = Label(query_frame, text="Qty: ", font=ourFont)
    Qty_name_label.grid(row=6, column=0, padx=10, pady=10)
    Qty_name_label_txt = Entry(query_frame, font=ourFont)
    Qty_name_label_txt.grid(row=6, column=1, padx=10, pady=10)

    ReturnDate_name_label = Label(query_frame, text="ReturnDate: ", font=ourFont)
    ReturnDate_name_label.grid(row=7, column=0, padx=10, pady=10)
    ReturnDate_name_label_txt = Entry(query_frame, font=ourFont)
    ReturnDate_name_label_txt.grid(row=7, column=1, padx=10, pady=10)

    TotalAmount_name_label = Label(query_frame, text="TotalAmount: ", font=ourFont)
    TotalAmount_name_label.grid(row=8, column=0, padx=10, pady=10)
    TotalAmount_name_label_txt = Entry(query_frame, font=ourFont)
    TotalAmount_name_label_txt.grid(row=8, column=1, padx=10, pady=10)

    PaymentDate_label = Label(query_frame, text="PaymentDate: ", font=ourFont)
    PaymentDate_label.grid(row=9, column=0, padx=10, pady=10)
    PaymentDate_label_txt = Entry(query_frame, font=ourFont)
    PaymentDate_label_txt.grid(row=9, column=1, padx=10, pady=10)  

    ## aAFGDDFGSDFGSFDGSDFG
    results_label = Label(output_frame, text="", font=ourFont)
    results_label.grid(row=0, column=0, padx=10, pady=10)

    # button to submit the query
    #
    submit_button = Button(query_frame, text="Submit", font=ourFont, command=lambda: req4_result(results_label, CustID_name_label_txt.get(), VehicleId_name_label_txt.get(), StartDate_name_label_txt.get(), OrderDate_name_label_txt.get(), RentalType_name_label_txt.get(), Qty_name_label_txt.get(), ReturnDate_name_label_txt.get(), TotalAmount_name_label_txt.get(), PaymentDate_label_txt.get()))
    submit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    query_frame.grid(row=0, column=0)
    output_frame.grid(row=1, column=0)

    return

def req5_func():
     #this is to add a new Reservation
    req5_window = Toplevel()
    req5_window.title("Handle Car Return")
    req5_window.geometry("600x700")

    #Frame to contain the input fields and output fields
    query_frame = Frame(req5_window)
    output_frame = Frame(req5_window)

    #create a label  -> Request 1
    req1_label = Label(query_frame, text="Handle Car Return", font=ourFont)
    req1_label.grid(row=0, column=0, columnspan=2, padx=200, pady=10)

    # Name, return date, vin
    #CREATE ALL THE LABELS AND ENTRY BOXES

    CustName_label = Label(query_frame, text="Cust. Name: ", font=ourFont)
    CustName_label.grid(row=1, column=0, padx=10, pady=10)
    CustName_label_txt = Entry(query_frame, font=ourFont)
    CustName_label_txt.grid(row=1, column=1, padx=10, pady=10)

    VehicleId_name_label = Label(query_frame, text="VehicleId: ", font=ourFont)
    VehicleId_name_label.grid(row=2, column=0, padx=10, pady=10)
    VehicleId_name_label_txt = Entry(query_frame, font=ourFont)
    VehicleId_name_label_txt.grid(row=2, column=1, padx=10, pady=10)

    ReturnDate_name_label = Label(query_frame, text="ReturnDate: ", font=ourFont)
    ReturnDate_name_label.grid(row=3, column=0, padx=10, pady=10)
    ReturnDate_name_label_txt = Entry(query_frame, font=ourFont)
    ReturnDate_name_label_txt.grid(row=3, column=1, padx=10, pady=10)

    ## aAFGDDFGSDFGSFDGSDFG
    results_label = Label(output_frame, text="", font=ourFont)
    results_label.grid(row=0, column=0, padx=10, pady=10)

    # button to submit the query
    #
    submit_button = Button(query_frame, text="Submit", font=ourFont, command=lambda: req5_result(results_label, CustName_label_txt.get(), VehicleId_name_label_txt.get(), ReturnDate_name_label_txt.get()))
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    query_frame.grid(row=0, column=0)
    output_frame.grid(row=1, column=0)

    return


'''
    ########################################

        MAIN PROGRAM STARTS HERE

    ########################################

'''


# add tkinter window
root = Tk()
root.title("Car Rental Database")
root.geometry("500x500")

# create a database or connect to one
conn = sqlite3.connect('finalpart3.db')

# create cursor
c = conn.cursor()

# add some text
text = Label(root, text="GUI CSE3330", font=ourFont)
text.grid(row=0, column=0, columnspan=2, padx=180, pady=10)
#horizontally center text


# button to add a record
# req1 = Button(root, text="SELECT-FROM-WHERE Query", font=ourFont, command=req1_func)
# req1.grid(row=1, column=0, columnspan=2, pady=10)

# button to add a record
req2 = Button(root, text="Add New Cutomer", font=ourFont,command=req2_func )
req2.grid(row=3, column=0, columnspan=2, pady=10)

# button to add a record
req3 = Button(root, text="New Vehicle", font=ourFont, command=req3_func)
req3.grid(row=5, column=0, columnspan=2, pady=10)

# button to add a record
req4 = Button(root, text="New Reservation", font=ourFont, command=req4_func)
req4.grid(row=7, column=0, columnspan=2, pady=10)

# button to add a record
req5 = Button(root, text="Handle Car Return", font=ourFont, command=req5_func)
req5.grid(row=9, column=0, columnspan=2, pady=10)

req6 = Button(root, text="Exit", font=ourFont, command=root.quit)

root.mainloop()
