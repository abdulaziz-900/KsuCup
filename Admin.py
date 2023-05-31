import tkinter as tk
import re
import tkinter.messagebox
import datetime
import DataBase
import random

class Admin:

   def __init__(self):
      self.window = tk.Tk()
      self.window.title("Admin")
      self.window.geometry('800x800')
      self.window.configure(bg="beige")
      self.Create_Button = tk.Button(self.window, text='Create', width=10,command=self.checkAll)
      self.Create_Button.place(x=340, y=401)
      self.buttonBack = tk.Button(self.window, text='Logout', command=self.logout,width=10)
      self.buttonBack.place(x=520, y=401)
      self.Backup_Button = tk.Button(self.window, text='Backup', command=self.backUpInformation, width=10)
      self.Backup_Button.place(x=420, y=450)
      self.ksucup_label = tk.Label(self.window, text="KsuCup", bg="beige")
      self.ksucup_label.place(x=140, y=70)
      self.ksucup_label.config(font=40)
      self.Admin_label = tk.Label(self.window, text="Admin", bg="beige")
      self.Admin_label.place(x=170, y=120)
      self.event_name_label = tk.Label(self.window, text="Event Name:", bg="beige")
      self.event_name_label.place(x=184, y=200)
      self.event_name_entry = tk.Entry(self.window, bg="White", width=40)
      self.event_name_entry.place(x=370, y=200)
      self.event_location_label = tk.Label(self.window, text="Event Location:", bg="beige")
      self.event_location_label.place(x=184, y=250)
      self.event_location_entry = tk.Entry(self.window, bg="White", width=40)
      self.event_location_entry.place(x=370, y=250)
      self.event_capacity_label = tk.Label(self.window, text="Event Capacity:", bg="beige")
      self.event_capacity_label.place(x=184, y=300)
      self.event_capacity_entry = tk.Entry(self.window, bg="White", width=40)
      self.event_capacity_entry.place(x=370, y=300)
      self.event_dateandtime_label = tk.Label(self.window, text="Event Date and Time: \nin format (YYYY-mm-dd HH:MM)", bg="beige")
      self.event_dateandtime_label.place(x=150, y=350)
      self.event_dateandtime_entry = tk.Entry(self.window, bg="White", width=40)
      self.event_dateandtime_entry.place(x=370, y=350)
      self.window.mainloop()



   def logout(self):
      self.window.destroy()
      import Signup





   def checkEventName(self, eventname):
      reg = "^[A-Z a-z0-9]+$"
      pat = re.compile(reg)
      EName = re.search(pat, eventname)
      if eventname.isspace():
         return False
      else:
         if EName:

            return True
         else:

          return False



   def checkEventLocation(self,eventtlocation):
      reg = "^[A-Z a-z0-9]+$"
      pat = re.compile(reg)
      Elocation = re.search(pat, eventtlocation)
      if eventtlocation.isspace():
         return False
      else:
         if Elocation:

            return True
         else:

            return False



   def checkEventCapacity(self,EventCapacity):
      reg = "^([1-9])[0-9]{0,}$"
      pat = re.compile(reg)
      i = re.search(pat, EventCapacity)
      if i:

         return True
      else:

         return False


   def checkEventDateAndTime(self,time):
      try:
         reg = "^[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-5][0-9]$"
         pat = re.compile(reg)
         i = re.search(pat, time)
         print(i)
         if i:
            datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')

            return True
         else:
            return False
      except ValueError:

         return False


   def checkAll(self):
      eventname = self.event_name_entry.get().strip()
      eventlocation = self.event_location_entry.get().strip()
      eventcapacity = self.event_capacity_entry.get().strip()
      eventdateandtime = self.event_dateandtime_entry.get().strip()
      if not self.checkEventName(eventname):
         tk.messagebox.showerror('Error', "Event name must be characters or digits")
      elif not self.checkEventLocation(eventlocation):
         tk.messagebox.showerror('Error', "Event location must be in characters or digits")
      elif not self.checkEventCapacity(eventcapacity):
         tk.messagebox.showerror('Error', "it must be above 0 and only numbers")
      elif not self.checkEventDateAndTime(eventdateandtime):
         tk.messagebox.showerror('Error', " the date and time must be in this format YYYY-mm-dd HH:MM \nfor example 2022-12-23 20:59, and be carefull of the months that dosent end with 30 and 31")

      else:
         x = f'{random.randint(1, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
         if DataBase.EventInserting(x,eventname, eventlocation, eventcapacity, eventdateandtime):
            tk.messagebox.showinfo("info", "Event has been created")
            self.event_name_entry.delete(0,tk.END)
            self.event_location_entry.delete(0, tk.END)
            self.event_capacity_entry.delete(0, tk.END)
            self.event_dateandtime_entry.delete(0, tk.END)
         else:
            tk.messagebox.showerror('Error', "Event already created ")

   def backUpInformation(self):
      DataBase.bkup()

