import tkinter as tk
import re
import DataBase
import tkinter.messagebox
class Login:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry('800x800')
        self.window.geometry("+600+200")
        self.window.configure(bg="beige")
        self.Login_Button = tk.Button(self.window, text='Login', width=10,command=self.check)
        self.Login_Button.place(x=400, y=300)
        self.ksucup_label = tk.Label(self.window, text="KsuCup", bg="beige")
        self.ksucup_label.place(x=140, y=70)
        self.ksucup_label.config(font=40)
        self.Login_label = tk.Label(self.window, text="Login", bg="beige")
        self.Login_label.place(x=170, y=120)
        self.Login_label.config(font=40)
        self.ID_label = tk.Label(self.window, text="ID:", bg="beige")
        self.ID_label.place(x=250, y=190)
        self.ID_entry = tk.Entry(self.window, bg="White", width=40)
        self.ID_entry.place(x=350, y=190)
        self.password_label = tk.Label(self.window, text="Password:", bg="beige")
        self.password_label.place(x=250, y=240)
        self.password_entry = tk.Entry(self.window, bg="White", width=40)
        self.password_entry.place(x=350, y=240)
        self.window.mainloop()


    def checkID(self,id):
        reg = "^[0-9]{10}$"
        pat = re.compile(reg)
        i = re.search(pat, id)
        if i:

            return True
        else:

            return False





    def checkPassword(self,pas):
        reg = "^[a-zA-Z0-9]{6,}$"
        pat = re.compile(reg)
        p = re.search(pat, pas)
        if p:

            return True
        else:

            return False





    def check(self):
        id = self.ID_entry.get()
        password = self.password_entry.get()
        if not self.checkID(id):
            tk.messagebox.showerror('Error', "id must be 10 digits")
            return
        elif not self.checkPassword(password):
            tk.messagebox.showerror('Error', "password must be at least 6 digits or letters")
            return
        x=DataBase.login(id,password)
        if x=="Admin":
            self.window.destroy()
            import Admin
            Admin.Admin()
        elif x=="Student":
             self.window.destroy()
             import Student
             Student.Student()
             print("Student")
        elif x=="n":
            self.password_entry.delete(0,tk.END)
            tk.messagebox.showerror("Error","the password or the ID are Invalid")