'''
    INVENTORY MANAGEMENT SYSTEM
    Developed By->Evans Narh
'''
import sqlite3
from tkinter import font, ttk
from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from Addtional_features import mycombobox, myentry
from PIL import Image, ImageTk
import datetime

import time

# ADMIN MENU


class Admin:

    def __init__(self, mainw):
        self.mainw = mainw

    # ADD ADMIN MAIN MENU TO WINDOW,ALL FRAMES AND ADD IMAGE BUTTONS
    def admin_mainmenu(self, a, b):
        self.sideframe = LabelFrame(
            self.mainw, width=200, height=800, bg="#096e5b")
        self.sideframe.place(x=0, y=60)

###########Sidebar###############################
        icon = ImageTk.PhotoImage(Image.open(
                    "images/over.PNG").resize((20, 20)))
        self.items = Button(self.sideframe, text=" Overviaw", fg="#FFFFFF", bd=5,  image=icon,borderless=1,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command="",
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.items.image = icon
        self.items.place(x=10, y=25)


        icon = ImageTk.PhotoImage(Image.open(
                    "images/invent.png").resize((20, 20)))
        self.stocks = Button(self.sideframe, text=" Inventory", fg="#FFFFFF", bd=5,  image=icon,borderless=1,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.buildprodtable ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.stocks.image = icon
        self.stocks.place(x=10, y=75)


        icon = ImageTk.PhotoImage(Image.open(
                    "images/sales.png").resize((20, 20)))
        self.sales = Button(self.sideframe, text=" Sales    ", fg="#FFFFFF", bd=5,  image=icon,borderless=1,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command="" ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.sales.image = icon
        self.sales.place(x=10, y=125)

        icon = ImageTk.PhotoImage(Image.open(
                    "images/account.png").resize((20, 20)))
        self.accounts = Button(self.sideframe, text=" Profiles   ", fg="#FFFFFF", bd=5,  image=icon,borderless=1,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command="" ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.accounts.image = icon
        self.accounts.place(x=10, y=175)

       
        mi = ImageTk.PhotoImage(Image.open(
            "images/sign-out.png").resize((20, 20)))
        self.changeuser = Button(self.sideframe, text=" Sign out   ",
                                    bd=5, font="poppins 16 normal",fg="#FFFFFF", image=mi, compound=LEFT, borderless=1,
                                     bg="#096e5b", activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.changeuser.image = mi
        self.changeuser.place(x=10, y=225)

        mi = ImageTk.PhotoImage(Image.open(
            "images/exit.png").resize((20, 20)))
       
        self.logout = Button(self.sideframe, text=" Close    ", borderless=1,fg="#FFFFFF", 
                                     bg="#096e5b", bd=5, font="poppins 16 normal", image=mi, compound=LEFT)
        self.logout.image = mi
        self.logout.place(x=10, y=600)

##############################################################

        self.leftframe = Frame(self.mainw, width=300, height=700, bg="#F3FDFE")
        self.leftframe.place(x=210, y=80)
        self.leftframeinfo = self.leftframe.place_info()

        

        self.formframe1 = Frame(self.mainw, width=750, height=700, bg="#F3FDFE")
        self.formframe1.place(x=520, y=80)
        self.formframe1info = self.formframe1.place_info()


        self.searchbut = Button(self.formframe1, text="Search Drug",
                                font="poppins 14", bg="#FFFFFF", bd=5, command=self.searchprod)
        self.searchbut.place(x=10, y=20, height=40)

        self.searchvar = StringVar()
        self.searchentry = myentry(
            self.formframe1, textvariable=self.searchvar, font="poppins 14", width=40, bg="#FFFFFF")
        self.searchentry.place(x=155, y=20, height=40)

        self.cur.execute("select product_name from products")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
    
        self.searchentry.set_completion_list(a)
        self.resetbut = Button(self.formframe1, text="Reset", font="poppins 14",
                               bd=5, width=80, bg="#FFFFFF", command=self.resetprodtabel)
        self.resetbut.place(x=540, y=20, height=40)

        self.cond = 0
        self.buildprodtable()

  ############## Build Product #################
    def buildprodtable(self):
        self.leftframe.place(self.leftframeinfo)
        self.formframe1.place(self.formframe1info)
         
        self.tableframe = LabelFrame(self.formframe1, width=350, height=650)
        self.tableframe.place(x=10, y=100)
        self.tableframeinfo = self.tableframe.place_info()
        
        if(self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
       
        scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
        
        self.style=ttk.Style()
        self.style.configure('Treeview', rowheight=25)

        self.tree = ttk.Treeview(self.tableframe, columns=("Product Name", "Category", "Wholesale Price",
                                                           'Selling Price', 'Quantity', 'Expiry Date'), selectmode="browse", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set, style="Treeview")
        self.tree.column('#0', stretch=NO, minwidth=0,
                         width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=150)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#4', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#5', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#6', stretch=NO, minwidth=0,
                         width=100, anchor='center')

        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Category', text="Category", anchor=W)
        self.tree.heading('Wholesale Price', text="Wholesale Price", anchor=W)
        self.tree.heading('Selling Price', text="Selling Price", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Expiry Date', text="Expiry Date", anchor=W)

        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getproducts()

        self.formframe = Frame(self.leftframe, width=300, height=500, bg="#F3FDFE")
        self.formframe.place(x=0, y=20)
        self.formframeinfo = self.formframe.place_info()

        self.tree.bind("<<TreeviewSelect>>", self.clickprodtable)
        self.formframe.focus_set()
        self.itemeditv = StringVar()
        self.itemeditcatv = StringVar()
        self.itemeditwholepricev = StringVar()
        self.itemeditsellpricev = StringVar()
        self.itemeditstockv = StringVar()
        self.itemeditexpv = StringVar()

        va = 5
        l1 = ['Product Name', 'Category', 'Wholesale Price',
              'Selling Price', 'Quantity', 'Expiry Date']
        for i in range(0, 6):
            Label(self.formframe, text=l1[i], font="poppins 12 normal", bg="#F3FDFE").place(
                x=10, y=5+va)
            va += 60
        self.entry1 = Entry(self.formframe, textvariable=self.itemeditv, font="poppins 12 normal",
                            width=20)
        self.entry1.bind('<Button-1>', self.onclick)
        self.entry1.place(x=120, y=0, height=40)
        x = myentry(self.formframe, textvariable=self.itemeditcatv,
                    font="poppins 12 normal", bg="#FFFFFF", width=20)
        x.place(x=120, y=60, height=40)
        self.cur.execute("select product_cat from products")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
        x.set_completion_list(a)
        Entry(self.formframe, textvariable=self.itemeditwholepricev, font="poppins 12 normal",
              bg="#FFFFFF", width=20).place(x=120, y=120, height=40)
        Entry(self.formframe, textvariable=self.itemeditsellpricev, font="poppins 12 normal",
              bg="#FFFFFF", width=20).place(x=120, y=180, height=40)
        Entry(self.formframe, textvariable=self.itemeditstockv, font="poppins 12 normal",
              bg="#FFFFFF", width=20).place(x=120, y=240, height=40)

        Entry(self.formframe, textvariable=self.itemeditexpv, font="poppins 12 normal",
              bg="#FFFFFF", width=20).place(x=120, y=300, height=40)


        Button(self.formframe, text="Add item", font="poppins 10 normal",bg="#096e5b", fg="#FFFFFF", bd=5, width=60,
               command="").place(x=5, y=380)
        Button(self.formframe, text="Edit", font="poppins 10 normal",bg="#096e5b", fg="#FFFFFF", bd=5, width=60,
               command="").place(x=105, y=380)
        Button(self.formframe, text="Remove Item", font="poppins 10 normal",bg="#096e5b", fg="#FFFFFF", bd=5, width=80,
               command="").place(x=200, y=380)



##############serach product#####################
    def searchprod(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from products")
        li = self.cur.fetchall()
        for i in li:
            if(i[0] == self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetprodtabel(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getproducts()

     # ONCLICK EVENT FOR PRODUCT TABLE
    def clickprodtable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 6):
            self.itemeditv.set((li[0]))
            self.itemeditcatv.set((li[1]))
            self.itemeditwholepricev.set((li[2]))
            self.itemeditsellpricev.set(str(li[3]))
            self.itemeditstockv.set(str(li[4]))
            self.itemeditexpv.set((li[5]))