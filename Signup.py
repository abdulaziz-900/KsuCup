import tkinter as tk
import re
import tkinter.messagebox
import DataBase


class Signup:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sign up")
        self.window.geometry('800x800')
        self.window.geometry("+600+200")
        self.window.configure(bg="beige")
        self.buttonBack = tk.Button(self.window, text='Login', width=10, command=self.go_login)
        self.buttonBack.place(x=330, y=500)
        self.sybmitbutton = tk.Button(self.window, text='Submit', width=10, command=self.checkAll)
        self.sybmitbutton.place(x=530, y=500)
        self.ksucup_label = tk.Label(self.window, text="KsuCup", bg="beige")
        self.ksucup_label.place(x=140, y=70)
        self.ksucup_label.config(font=40)
        self.Singup_label = tk.Label(self.window, text="Sign Up", bg="beige")
        self.Singup_label.place(x=170, y=120)
        self.Singup_label.config(font=40)
        self.ID_label = tk.Label(self.window, text="ID:", bg="beige")
        self.ID_label.place(x=250, y=150)
        self.ID_entry = tk.Entry(self.window, bg="White", width=40)
        self.ID_entry.place(x=350, y=150)
        self.first_name_label = tk.Label(self.window, text="FirstName:", bg="beige")
        self.first_name_label.place(x=250, y=200)
        self.first_name_entry = tk.Entry(self.window, bg="White", width=40)
        self.first_name_entry.place(x=350, y=200)
        self.last_name_label = tk.Label(self.window, text="LastName:", bg="beige")
        self.last_name_label.place(x=250, y=250)
        self.last_name_entry = tk.Entry(self.window, bg="White", width=40)
        self.last_name_entry.place(x=350, y=250)
        self.password_label = tk.Label(self.window, text="Password:", bg="beige")
        self.password_label.place(x=250, y=300)
        self.password_entry = tk.Entry(self.window, bg="White", width=40)
        self.password_entry.place(x=350, y=300)
        self.email_label = tk.Label(self.window, text="Email:", bg="beige")
        self.email_label.place(x=250, y=350)
        self.email_entry = tk.Entry(self.window, bg="White", width=40)
        self.email_entry.place(x=350, y=350)
        self.phonenumber_label = tk.Label(self.window, text="PhoneNumber:", bg="beige")
        self.phonenumber_label.place(x=250, y=400)
        self.phonenumber_entry = tk.Entry(self.window, bg="White", width=40)
        self.phonenumber_entry.place(x=350, y=400)
        DataBase.create()
        DataBase.createEvents()
        DataBase.createreservation()
        DataBase.adminInserting()

        self.window.mainloop()

    def go_login(self):
        self.window.destroy()
        import Login

        Login.Login()

    def checkFirstAndLastName(self, first, last):
        reg = "^[A-Za-z]+$"
        pat = re.compile(reg)
        fName = re.search(pat, first)
        lName = re.search(pat, last)
        if fName and lName:

            return True
        else:

            return False

    def checkID(self, id1):
        reg = "^[0-9]{10}$"
        pat = re.compile(reg)
        i = re.search(pat, id1)
        if i:

            return True
        else:

            return False

    def checkPassword(self, pas):
        reg = "^[a-zA-Z0-9]{6,}$"
        pat = re.compile(reg)
        p = re.search(pat, pas)
        if p:

            return True
        else:

            return False

    def checkEmail(self, email):
        reg = "^([A-Za-z0-9._-]+)@ksu\.edu\.sa$"
        pat = re.compile(reg)
        e = re.search(pat, email)
        if e:

            return True
        else:

            return False

    def checkPhone(self, phone):
        reg = "^(05)[0-9]{8}$"
        pat = re.compile(reg)
        i = re.search(pat, phone)
        if i:

            return True
        else:

            return False

    def checkAll(self):
        id = self.ID_entry.get()
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        phonenumber = self.phonenumber_entry.get()
        if not self.checkID(id):
            tk.messagebox.showerror('Error', "id must be 10 digits")
        elif not self.checkFirstAndLastName(firstname, lastname):
            tk.messagebox.showerror('Error', "Firstname and last name must be characters")
        elif not self.checkPassword(password):
            tk.messagebox.showerror('Error', "password must be at least 6 digits or letters")
        elif not self.checkEmail(email):
            tk.messagebox.showerror('Error', " the email must be ended with that format @ksu.edu.sa")
        elif not self.checkPhone(phonenumber):
            tk.messagebox.showerror('Error', "the phone number must start with 05 and 8 digits after it")

        else:
            import DataBase
            if DataBase.studentInserting(id, firstname, lastname, password, email, phonenumber):
                tk.messagebox.showinfo("info", "Account has been created")
                self.ID_entry.delete(0, tk.END)
                self.first_name_entry.delete(0, tk.END)
                self.last_name_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.phonenumber_entry.delete(0, tk.END)
            else:
                tk.messagebox.showerror('Error', "Account already registered ")


Signup()
