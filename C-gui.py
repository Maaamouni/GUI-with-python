import tkinter
import tkinter.messagebox
import customtkinter as ctk
import sqlite3


app = ctk.CTk()
app.title("Inscription")
app.geometry("470x600")
app.resizable(False, False)

def enter_data():
    accepted = terms_acc.get()

    if accepted == "Accepted":
        first_name = F_name_entry.get()
        last_name = F_lname_entry.get()

        if first_name and last_name:
            user_name = usr_name_entry.get()
            user_title = title_combobox.get()
            user_age = age_entry.get()
            user_nat = nat_combobox.get()
            user_phone = number_entry.get()
            user_email = email_entry.get()
        else:
            tkinter.messagebox.showwarning(title="error", message="First and last name are required")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have note accepted terms and conditions.")

    

    # to close the window
    app.destroy()

    print("First name "+ first_name + " Last name " +  last_name)
    print("Username "+ user_name + "  age " +  user_age)
    print("Phone "+ user_phone + " Nationality " +  user_nat)
    print("email  "+ user_email )

    #create table

    dt = sqlite3.connect('login_dat.db')
    table_create = '''CREATE TABLE IF NOT EXISTS logine_table(
        firstname TEXT, lastname TEXT, username TEXT, age int, nationality TEXT,email TEXT, phone int)'''
    
    dt.execute(table_create)
    #insert data
    data_insert = '''INSERT INTO logine_table(firstname, lastname, username, age, nationality, email, phone) VALUES (?,?,?,?,?,?,?)'''
    data_tuple = (first_name, last_name, user_name, user_age, user_nat, user_email, user_phone)

    cursor = dt.cursor()
    cursor.execute(data_insert, data_tuple)
    dt.commit() # to dave the data in database
    dt.close()


        

F_name = ctk.CTkLabel(app, text="First Name :")
F_name.place(relx=0.1,rely=0.03)

F_name_entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter your first name ..")
F_name_entry.place(relx=0.3,rely=0.03)

F_lname = ctk.CTkLabel(app, text="Last Name :")
F_lname.place(relx=0.1,rely=0.1)

F_lname_entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter your last name ..")
F_lname_entry.place(relx=0.3,rely=0.1)

usr_name = ctk.CTkLabel(app, text="Username :")
usr_name.place(relx=0.1,rely=0.17)

usr_name_entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter your Username ..")
usr_name_entry.place(relx=0.3,rely=0.17)

title = ctk.CTkLabel(app, text="Title: ")
title.place(relx = 0.1, rely=0.24)

title_combobox = ctk.CTkComboBox(app, values=["Mr.", "Ms", "Dr."], width=250)
title_combobox.place(relx = 0.3, rely = 0.24)

age = ctk.CTkLabel(app, text="Age: ")
age.place(relx = 0.1, rely=0.31)

age_entry = ctk.CTkEntry(app, placeholder_text="Enter your age..", width=250)
age_entry.place(relx = 0.3, rely=0.31)

nat = ctk.CTkLabel(app, text="Nationality: ")
nat.place(relx = 0.1, rely = 0.38)

nat_combobox = ctk.CTkComboBox(app, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], width=250)
nat_combobox.place(relx = 0.3, rely = 0.38)

number = ctk.CTkLabel(app, text="FAX:")
number.place(relx=0.1,rely=0.45)

number_entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter your phone number ..")
number_entry.place(relx=0.3,rely=0.45)

email = ctk.CTkLabel(app, text="Email:")
email.place(relx=0.1,rely=0.52)


email_entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter your email ..")
email_entry.place(relx=0.3,rely=0.52)

other = ctk.CTkLabel(app, text="Descirption:")
other.place(relx=0.1,rely=0.59)

other = ctk.CTkTextbox(app, width=250, height=150)
other.place(relx=0.3,rely=0.59)

terms_var = ctk.StringVar(value="Not accepted")

terms_acc = ctk.CTkCheckBox(app, text="Terms & Conditions", variable=terms_var, onvalue="Accepted", offvalue="Not Accepted")
terms_acc.place(relx=0.1, rely=0.85)

enter_b = ctk.CTkButton(app, text="Enter", command=enter_data)
enter_b.place(relx = 0.53, rely=0.92)


app.mainloop()
