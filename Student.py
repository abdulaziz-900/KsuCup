import tkinter as tk
from tkinter import ttk
import DataBase
import sqlite3
import tkinter.messagebox
import datetime

class Student:

    def __init__(self):
        self.mainwindow = tk.Tk()
        self.mainwindow.title("Student")
        self.mainwindow.geometry("800x330")
        self.mainwindow.configure(background="beige")
        self.notebook = ttk.Notebook(self.mainwindow,width=100)
        self.notebook.pack(fill="both")
        self.frame1 = tk.Frame(self.mainwindow,background="beige")
        self.frame1.pack(fill="both")
        self.frame2 = tk.Frame(self.mainwindow,background="beige")
        self.frame2.pack(fill="both")
        # frame1
        self.Book_button=tk.Button(self.frame1,text='Book ticket',width=10,command=self.Book)
        self.Logout_button = tk.Button(self.frame1, text='Logout', width=10,command=self.logout)
        self.Book_button.grid(row=2,column=1,padx=140,pady=50)
        self.Logout_button.grid(row=2,column=2)
        self.notebook.add(self.frame1, text='Book a Ticket')
        self.notebook.add(self.frame2, text='view my tickets')
        self.tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4), show='headings', height=8, selectmode='browse')
        self.tv.heading(1, text="Event Id")
        self.tv.heading(2, text="Event name")
        self.tv.heading(3, text="Event location")
        self.tv.heading(4, text="Date and time")
        self.tv.grid(row=1,column=1,columnspan=3)
        # frame2
        self.show_button = tk.Button(self.frame2, text='Show Button', width=10,command=self.dispaly2)
        self.Logout2_button = tk.Button(self.frame2, text='Logout', width=10, command=self.logout)
        self.show_button.grid(row=2, column=1, padx=140, pady=50)
        self.Logout2_button.grid(row=2, column=2)
        self.tv2 = ttk.Treeview(self.frame2, columns=(1, 2, 3, 4), show='headings', height=8)
        self.tv2.heading(1, text="Event Id")
        self.tv2.heading(2, text="Event name")
        self.tv2.heading(3, text="Event location")
        self.tv2.heading(4, text="Date and time")
        self.tv2.grid(row=1, column=1, columnspan=3)
        self.display()
        self.mainwindow.mainloop()


    def logout(self):
        self.mainwindow.destroy()
        import Signup






    def display(self):
        conn = sqlite3.connect("ksuCup.db")
        cursor = conn.execute("SELECT EventID, EventName, EventLocation,EventDateAndTime from EVENT")
        count = 0
        for row in cursor:
            f = datetime.datetime.now()
            f = f.strftime('%Y-%m-%d %H:%M')
            if row[3] > f:
                self.tv.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3]))
                count += 1
        conn.close()





    def dispaly2(self):

        for item in self.tv2.get_children():
            self.tv2.delete(item)
        self.tv.update()
        conn = sqlite3.connect("ksuCup.db")
        showlist=DataBase.showButton()

        if len(showlist)==0:
            tk.messagebox.showerror("Error","you didn't book anything")
        else:
            count=0
            for rty in showlist:
                cursor = conn.execute(f"SELECT EventID, EventName, EventLocation,EventDateAndTime from EVENT where EventID='{rty}'")
                for row in cursor:
                    f = datetime.datetime.now()
                    f = f.strftime('%Y-%m-%d %H:%M')
                    if row[3]>f:
                        self.tv2.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3]))
                        count += 1





    def Book(self):
        selected=self.tv.focus()
        data=self.tv.item(selected)

        if data["values"]=="":
            tk.messagebox.showerror('Error', "you must choose an event")
        else:
            check=DataBase.Booking(data["values"])
            if check=="full":
                tk.messagebox.showerror("Error","the capacity is full try again later")
            elif check=="booked":
                tk.messagebox.showerror("Error","you have already booked the event")
            elif check=="s":
                tk.messagebox.showinfo("info","you booked the event successfully")
