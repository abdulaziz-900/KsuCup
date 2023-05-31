import sqlite3
import hashlib
import logging
import csv
logging.basicConfig(filename='transactions.log',
 filemode='a',
 format='%(asctime)s - %(message)s',
 level=logging.DEBUG)
def create():
     try:

        conn = sqlite3.connect("ksuCup.db")
        print("database has opened successfully")
        conn.execute('''CREATE TABLE ACCOUNT
        (ID TEXT PRIMARY KEY  NOT NULL,
        firstName TEXT NOT NULL,
        lastName TEXT  NOT NULL,
        PASSWORD TEXT   NOT NULL,
        EMAIL  TEXT NOT NULL,
        phoneNumber  VARCHAR(10) NOT NULL,
        accountTYPE TEXT NOT NULL);''')
        print("Table created successfully")
        conn.close()
     except:
        print("Table hasn't been created")






def createEvents():
    try:

        conn = sqlite3.connect("ksuCup.db")
        print("database has opened successfully")
        conn.execute('''CREATE TABLE EVENT
        (EventID TEXT PRIMARY KEY  NOT NULL,
        EventName TEXT NOT NULL,
        EventLocation TEXT  NOT NULL,
        EventCapacity INT   NOT NULL,
        bookingNumber  INT NOT NULL,
        EventDateAndTime  DateTime NOT NULL);''')
        print("Table created successfully")
        conn.close()
    except:
        print("Table hasn't been created")








def createreservation():
    try:

        conn = sqlite3.connect("ksuCup.db")
        print("database has opened successfully")
        conn.execute('''CREATE TABLE reservation
        (acID TEXT NOT NULL,
        Eid TEXT NOT NULL,
        PRIMARY KEY(acID,Eid),
        foreign key(acID) references ACCOUNT(ID),
        foreign key(Eid) references EVENT(EventID));''')
        print("Table created successfully")
        conn.close()
    except:
        print("Table hasn't been created")









def adminInserting():
   conn=sqlite3.connect("ksuCup.db")
   print("has connected to the database")
   try:
     pas='5679abc'
     result = hashlib.sha256(pas.encode()).hexdigest()
     conn.execute(f"INSERT INTO ACCOUNT (ID,firstName,lastName,PASSWORD,EMAIL,phoneNumber,accountTYPE) \
     VALUES ('1234567890', 'Ali', 'khaild', '{result}', 'ali990@ksu.edu.sa','0544993238','Admin' )")
     conn.commit()
     conn.close()
     print("admin has been successfully created")
   except sqlite3.IntegrityError:
       print("account is already there")








def login(Id, password):
       hashpas = hashlib.sha256(password.encode()).hexdigest()
       conn = sqlite3.connect("ksuCup.db")
       cur = conn.execute(f"Select * from ACCOUNT where ID = {Id} and  PASSWORD = '{hashpas}'")
       global account
       account = []

       NotFound = True
       for x in cur:
           NotFound = False
           if x[6] == 'Admin':

               account = list(x)
               conn.close()
               return 'Admin'
           elif x[6] == 'Student':

               account = list(x)
               conn.close()
               return 'Student'
       if NotFound:

           conn.close()
           # not found
           return 'n'






def studentInserting(id,firstname,lastname,password,email,phonenumber):
    conn = sqlite3.connect("ksuCup.db")
    print("has connected to the database")
    try:
        pas = password
        result = hashlib.sha256(pas.encode()).hexdigest()
        conn.execute(f"INSERT INTO ACCOUNT (ID,firstName,lastName,PASSWORD,EMAIL,phoneNumber,accountTYPE) \
        VALUES ('{id}', '{firstname}', '{lastname}', '{result}', '{email}','{phonenumber}','Student' )")
        conn.commit()
        conn.close()

        return True
    except sqlite3.IntegrityError:

        return False








def EventInserting(eventid,eventname,eventlocation,eventcapacity,eventdateandtime):
    conn = sqlite3.connect("ksuCup.db")
    print("has connected to the database")
    try:
        conn.execute(f"INSERT INTO EVENT (EventID,EventName,EventLocation,EventCapacity,bookingNumber,EventDateAndTime) \
        VALUES ('{eventid}', '{eventname}', '{eventlocation}', {eventcapacity}, {0},'{eventdateandtime}')")
        conn.commit()
        conn.close()

        return True
    except sqlite3.IntegrityError:

        return False









def Booking(books):
    conn = sqlite3.connect("ksuCup.db")
    print("has connected to the database")
    try:

        chosenid=books[0]
        currsor=conn.execute(f"Select EventCapacity,bookingNumber,EventName,EventLocation from EVENT where EventID = {chosenid}")
        Ec=-1
        bn=0
        En=""
        El=""
        for row in currsor:

            Ec=row[0]
            bn=row[1]
            En=row[2]
            El=row[3]

        if bn==Ec:
            return "full"
        else:
            global account
            currsor=conn.execute(f"Select * from reservation where acID ='{account[0]}' and Eid='{chosenid}' ")
            count=0
            for row in currsor:
              count=count+1
            if count==1:
                return "booked"
            else:
                conn.execute(f"update EVENT set bookingNumber=bookingNumber+1 where EventID = {chosenid} ")
                conn.commit()
                conn.execute(f"INSERT INTO reservation (acID,Eid) \
                 VALUES ('{account[0]}','{chosenid}')")
                conn.commit()
                logging.info(f"the Event name= {En}, Event location= {El}, Student id= {account[0]}")
                return "s"
    except sqlite3.IntegrityError as er:
        print(er)







def showButton():
    conn = sqlite3.connect("ksuCup.db")
    print("has connected to the database")
    showlist=[]
    try:
        global account
        currsor = conn.execute(f"Select * from reservation where acID ='{account[0]}'")
        for row in currsor:
            showlist.append(row[1])

        return showlist
    except sqlite3.IntegrityError as er:
        print(er)


def bkup():
    print('Back up ')
    conn = sqlite3.connect("ksuCup.db")
    file = open("backup.csv", "w", newline="")
    heading1 = "ID,firstName,lastName,PASSWORD,EMAIL,phoneNumber,accountTYPE"
    csvwriter = csv.writer(file)
    csvwriter.writerow(heading1.split(","))
    currsor = conn.execute("SELECT * FROM ACCOUNT")
    for row in currsor:
        acc = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}"

        csvwriter.writerow(acc.split(","))


    heading2 = "EventID,EventName,EventLocation,EventCapacity,bookingNumber,EventDateAndTime"
    currsor2 = conn.execute("SELECT * FROM EVENT")
    csvwriter.writerow(heading2.split(","))

    for row in currsor2:
        evn = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}"

        csvwriter.writerow(evn.split(","))

    heading3 = "acID,Eid"
    currsor3 = conn.execute("SELECT * FROM reservation")
    csvwriter.writerow(heading3.split(","))
    for row in currsor3:
        res = f"{row[0]},{row[1]}"

        csvwriter.writerow(res.split(","))

    file.close()
    conn.close()

