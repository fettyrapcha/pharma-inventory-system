

import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Userlogin import Login
from Admin_menu import Admin
from User_menu import User
from Intro import splash
from PIL import Image, ImageTk

# MAIN WINDOW


class Main(splash, Login, Admin, User):

    def __init__(self):
        global b
        if b == 0:
            super().__init__()
            b = 1
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')  # LOGIN WINDOW EXITS
        self.mainw = Toplevel(bg="#FFFFFF")
        width = 1250
        height = 850
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.geometry("%dx%d+%d+%d" %
                            (width, height, x, y))
        self.mainw.title("Inventory")
        # self.mainw.resizable(1, 1)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()

    # OVERRIDING CLOSE BUTTON && DESTRUCTOR FOR CLASS LOGIN AND MAIN WINDOW
    def __Main_del__(self):
        if messagebox.askyesno("Quit", " Leave Inventory?") == True:
            self.loginw.quit()
            self.mainw.quit()
            exit(0)
        else:
            pass

    # FETCH USER DETAILS FROM PRODUCTS,USERS AND INVENTORY TABLE
    def getdetails(self):
        self.cur.execute("CREATE TABLE if not exists products(product_name varchar (50) NOT NULL,product_cat varchar (50),product_wprice NUMERIC NOT NULL,product_sprice NUMERIC NOT NULL,stocks INTEGER NOT NULL, expiry_date varchar (20));")
        self.cur.execute("CREATE TABLE if not exists salesday(Trans_id integer (50) NOT NULL, product_name varchar (50),product_sprice NUMERIC NOT NULL, quantity INTEGER NOT NULL, total NUMERIC NOT NULL, Time varchar (20), pay_method varchar (50));")
        self.cur.execute(
            "CREATE TABLE if not exists sales (Trans_id	INTEGER,product_name varchar (50), Quantity INTEGER NOT NULL, totals NUMERIC NOT NULL,Time varchar (20),Date varchar (20),pay_method varchar (50));")
        self.cur.execute("select * from products ")
        self.products = self.cur.fetchall()
        capuser = self.username.get()
        capuser = capuser.upper()
        global uuu
        self.uuu = capuser
        self.cur.execute(
            "select account_type from users where username= ? ", (capuser,))
        l = self.cur.fetchall()
        self.account_type = l[0][0]
        self.buildmain()

    #  ADD WIDGETS TO TOP OF MAIN WINDOW
    def buildmain(self):
        if self.account_type == 'ADMIN':
            super(Admin).__init__()
            self.admin_mainmenu(8, 8)
        else:
            super(User).__init__()
            self.user_mainmenu(8, 8)
        self.logout.config(command=self.__Main_del__)
        self.changeuser.config(command=self.change_user)
        self.topframe = LabelFrame(
            self.mainw, width=1400, height=60, bg="#ffffff")
        self.topframe.place(x=0, y=0)
        # self.storelable.config(font=("Time New Roman", 50, "bold"))
        # self.storelable.place(x=330, y=20)

        mi = Image.open("images/fetty.jpg")
        mi = mi.resize((1250,60))
        mi = ImageTk.PhotoImage(mi)
        self.mylogo = Label(self.topframe, image=mi)
        self.mylogo.image = mi
        self.mylogo.place(x=0, y=0)

        # mi = Image.open("images/line.jpg")
        # mi = mi.resize((1110, 10))
        # mi = ImageTk.PhotoImage(mi)
        # self.mylogo = Label(self.topframe, image=mi)
        # self.mylogo.image = mi
        # self.mylogo.place(x=300, y=100)

        # mi = PhotoImage(file="images/myprofile.png")
        mi = Image.open("images/user.png")
        mi = mi.resize((25, 25))
        mi = ImageTk.PhotoImage(mi)
        # mi = mi.subsample(4,4)
        self.myprofile = ttk.Label(self.topframe, text=(
            self.username.get()).capitalize(), image=mi, compound=TOP)
        self.myprofile.image = mi
        self.myprofile.place(x=1180, y=4)

        ''''
        if self.account_type == 'ADMIN':
            self.adminlabel= Label(self.topframe,text="Admin",font="Roboto 10 bold",bg="#4267b2")
        else:
            self.adminlabel = Label(self.topframe, text=" User", font="Roboto 10 bold", bg="#4267b2")
        self.adminlabel.place(x=1300,y=80)
        '''
        # DATE TIME LABEL
        ''''
        now = datetime.datetime.now()
        self.datetimelabel= Label(self.topframe,text=str(now.day)+'/'+str(now.month)+'/'+str(now.year),font="Roboto 10 bold", bg="skyblue2")
        self.datetimelabel.place(x=1290,y=90)
        '''

    # METHODS FOR ITEMS AND CHANGE USER BUTTONS
    def change_user(self):
        if messagebox.askyesno("Alert!", "Do  you want to change user?") == True:
            self.base.commit()
            self.mainw.destroy()
            self.loginw.destroy()
            self.__init__()


if __name__ == '__main__':
    b = 0
    w = Main()
    w.base.commit()
    w.mainw.mainloop()
