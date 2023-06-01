'''
    INVENTORY MANAGEMENT SYSTEM
    Developed By->Evans Narh
'''
import sqlite3
from tkinter import font, ttk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from Addtional_features import mycombobox, myentry
from PIL import Image, ImageTk
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import time

# ADMIN MENU


class Admin:

    def __init__(self, mainw):
        self.mainw = mainw

    # ADD ADMIN MAIN MENU TO WINDOW,ALL FRAMES AND ADD IMAGE BUTTONS
    def admin_mainmenu(self, a, b):
        self.sideframe = LabelFrame(
            self.mainw, width=200, height=820, bg="#096e5b")
        self.sideframe.place(x=0, y=60)

###########Sidebar###############################
        icon = ImageTk.PhotoImage(Image.open(
                    "images/over.PNG").resize((20, 20)))
        self.items = Button(self.sideframe, text=" Dashboard", fg="#FFFFFF", bd=5,borderwidth=0,  image=icon,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.overview,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.items.image = icon
        self.items.place(x=10, y=25)


        icon = ImageTk.PhotoImage(Image.open(
                    "images/invent.png").resize((20, 20)))
        self.stocks = Button(self.sideframe, text=" Inventory", fg="#FFFFFF", bd=5,borderwidth=0,  image=icon,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.buildprodtable ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.stocks.image = icon
        self.stocks.place(x=10, y=85)


        icon = ImageTk.PhotoImage(Image.open(
                    "images/sales.png").resize((20, 20)))
        self.sales = Button(self.sideframe, text=" Sales    ", fg="#FFFFFF", bd=5,borderwidth=0,  image=icon,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.buildsalestable ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.sales.image = icon
        self.sales.place(x=10, y=145)

        icon = ImageTk.PhotoImage(Image.open(
                    "images/account.png").resize((20, 20)))
        self.accounts = Button(self.sideframe, text=" Profiles   ", fg="#FFFFFF", bd=5,borderwidth=0,  image=icon,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.buildusertable ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.accounts.image = icon
        self.accounts.place(x=10, y=205)

       
        mi = ImageTk.PhotoImage(Image.open(
            "images/sign-out.png").resize((20, 20)))
        self.changeuser = Button(self.sideframe, text=" Sign out   ",
                                    bd=5, font="poppins 16 normal",fg="#FFFFFF",borderwidth=0, image=mi, compound=LEFT,
                                     bg="#096e5b", activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.changeuser.image = mi
        self.changeuser.place(x=10, y=265)

        mi = ImageTk.PhotoImage(Image.open(
            "images/exit.png").resize((20, 20)))
       
        self.logout = Button(self.sideframe, text=" Close    ",fg="#FFFFFF", 
                                     bg="#096e5b", bd=5, font="poppins 16 normal", image=mi, compound=LEFT)
        self.logout.image = mi
        self.logout.place(x=10, y=680)

##############################################################

        self.leftframe = Frame(self.mainw, width=300, height=860, bg="#F3FDFE")
        self.leftframe.place(x=210, y=80)
        self.leftframeinfo = self.leftframe.place_info()

        self.leftframe1 = Frame(self.mainw, width=400, height=860, bg="#F3FDFE")
        self.leftframe1.place(x=210, y=80)
        self.leftframe1info = self.leftframe1.place_info()

        
        self.overframe = Frame(self.mainw, width=1050, height=860, bg="#F3FDFE")
        self.overframe.place(x=210, y=80)
        self.overframeinfo = self.overframe.place_info()

        self.salesframe = Frame(self.mainw, width=1050, height=860, bg="#F3FDFE")
        self.salesframe.place(x=210, y=80)
        self.salesframeinfo = self.salesframe.place_info()

        self.formframe1 = Frame(self.mainw, width=750, height=860, bg="#F3FDFE")
        self.formframe1.place(x=520, y=80)
        self.formframe1info = self.formframe1.place_info()

        self.formframe2 = Frame(self.mainw, width=650, height=860, bg="#F3FDFE")
        self.formframe2.place(x=620, y=80)
        self.formframe2info = self.formframe2.place_info()


        self.searchbut = Button(self.formframe1, text="Search Drug",
                                font="poppins 12",fg="#FFFFFF", bg="#096e5b", bd=5, command=self.searchprod)
        self.searchbut.place(x=10, y=20, height=40)

        self.searchvar = StringVar()
        self.searchentry = myentry(
            self.formframe1, textvariable=self.searchvar, font="poppins 14", width=28, bg="#FFFFFF")
        self.searchentry.place(x=145, y=20, height=40)

        self.cur.execute("select product_name from products")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
        self.searchentry.set_completion_list(a)
        
        self.resetbut = Button(self.formframe1, text="Reset", font="poppins 12",
                               bd=5,  bg="#F3FDFE", command=self.resetprodtabel)
        self.resetbut.place(x=480, y=20, height=40)

        self.cond = 0
        self.buildprodtable()

  ############## Build Product #################
    def buildprodtable(self):
        self.formframe2.place_forget()
        self.overframe.place_forget()
        self.salesframe.place_forget()
        self.leftframe1.place_forget()

        self.leftframe.place(self.leftframeinfo)
        self.formframe1.place(self.formframe1info)
         
        self.tableframe = LabelFrame(self.formframe1, width=350, height=650)
        self.tableframe.place(x=10, y=80)
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
                                                           'Selling Price', 'Quantity', 'Expiry Date'), selectmode="browse", height=24, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set, style="Treeview")
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

        self.inventory = Label(
                    self.leftframe, text="Inventory", font="poppins 16 bold", bg="#F3FDFE").place(x=10, y=10)

        va = 5
        l1 = ['Product Name', 'Category', 'Wholesale Price',
              'Selling Price', 'Quantity', 'Expiry Date']
        for i in range(0, 6):
            Label(self.formframe, text=l1[i], font="poppins 10 normal", bg="#F3FDFE").place(
                x=10, y=25+va)
            va += 60
        self.entry1 = Entry(self.formframe, textvariable=self.itemeditv, font="poppins 12 normal",
                            width=14)
        self.entry1.bind('<Button-1>', self.onclick)
        self.entry1.place(x=120, y=20, height=40)
        x = myentry(self.formframe, textvariable=self.itemeditcatv,
                    font="poppins 12 normal", bg="#FFFFFF", width=14)
        x.place(x=120, y=80, height=40)
        self.cur.execute("select product_cat from products")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
        x.set_completion_list(a)
        Entry(self.formframe, textvariable=self.itemeditwholepricev, font="poppins 12 normal",
              bg="#FFFFFF", width=14).place(x=120, y=140, height=40)
        Entry(self.formframe, textvariable=self.itemeditsellpricev, font="poppins 12 normal",
              bg="#FFFFFF", width=14).place(x=120, y=200, height=40)
        Entry(self.formframe, textvariable=self.itemeditstockv, font="poppins 12 normal",
              bg="#FFFFFF", width=14).place(x=120, y=260, height=40)

        Entry(self.formframe, textvariable=self.itemeditexpv, font="poppins 12 normal",
              bg="#FFFFFF", width=14).place(x=120, y=320, height=40)


        Button(self.formframe, text="Add item", font="poppins 10 normal",fg="#ffffff",bg="#096e5b", bd=5,
               command=self.insertitem).place(x=5, y=400)
        Button(self.formframe, text="Update", font="poppins 10 normal",fg="#ffffff",bg="#096e5b", bd=5,
               command=self.changeprodtable).place(x=95, y=400)
        Button(self.formframe, text="Remove Item", font="poppins 10 normal",fg="#ffffff",bg="#E93E3E", bd=5,
               command=self.delproduct).place(x=180, y=400)


        Label(self.leftframe, text='Total Stock:',
              font="poppins 14", bg="#FFFFFF").place(x=5, y=500)
        Label(self.leftframe, text='Total CP:',
              font="poppins 14", bg="#FFFFFF").place(x=5, y=550)
        Label(self.leftframe, text='Total SP:',
              font="poppins 14", bg="#FFFFFF").place(x=5, y=600)
        Label(self.leftframe, text='GP:',
              font="poppins 14", bg="#FFFFFF").place(x=5, y=650)

        self.cur.execute(
            "select product_wprice,product_sprice,stocks from products")
        li = self.cur.fetchall()
        costprice = 0
        sellingprice = 0
        count = 0
        gross = 0
        finishit = 0
        global fini
        fini = []
        for i in range(0, len(li)):
            myli = list(li[i])
            total_whole = myli[0] * myli[2]
            total_whole = float(total_whole)
            costprice += total_whole

            total_sell = myli[1] * myli[2]
            total_sell = float(total_sell)
            sellingprice += total_sell
            count += 1
            gross = sellingprice - costprice
            gross = float(gross)
            
            if myli[2] <= 2:
                finishit += 1
                if myli[2] in fini:
                    continue
                else:
                    fini.append(myli[2])
            self.finishit = f"{finishit}"
        self.total_count = f"{count}"
        self.total_cost = f"Ghc {costprice:.2f}"
        self.total_selling = f"Ghc{sellingprice:.2f}"
        self.total_gross = f"Ghc{gross:.2f}"

        self.totallable = Label(
            self.leftframe, text=self.total_count, bg="#a5f0e5", anchor="center")
        self.totallable.config(font="poppins 15 bold")
        self.totallable.place(x=130, y=500)

        self.totallable = Label(
            self.leftframe, text=self.total_cost, bg="#a5f0e5", anchor="center")
        self.totallable.config(font="poppins 15 bold")
        self.totallable.place(x=130, y=550)

        self.totallable = Label(
            self.leftframe, text=self.total_selling, bg="#a5f0e5", anchor="center")
        self.totallable.config(font="poppins 15 bold")
        self.totallable.place(x=130, y=600)

        self.totallable = Label(
            self.leftframe, text=self.total_gross, bg="#a5f0e5", anchor="center")
        self.totallable.config(font="poppins 15 bold")
        self.totallable.place(x=130, y=650)


##############serach product#####################
    def searchprod(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from products")
        li = self.cur.fetchall()
        for i in li:
            # print(i[0])
            if(self.searchvar.get().upper() in i[0]):
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


 # FETCH PRODUCTS FROM PRODUCTS TABLE

    def getproducts(self, x=0):
        ans = ''
        self.cur.execute("select * from products")
        productlist = self.cur.fetchall()
        for i in productlist:
            i = list(i)
            i[2] = "{:.2f}".format(i[2])
            i[3] = "{:.2f}".format(i[3])
            self.tree.insert('', 'end', values=(i))
            if (str(x) == i[0]):
                a = self.tree.get_children()
                ans = a[len(a)-1]

        return ans



# MODIFIES RECORD OF PRODUCT TABLE

    def changeprodtable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.itemeditv.set((self.itemeditv.get()).upper())
        self.itemeditcatv.set((self.itemeditcatv.get()).upper())
        if(len(li) == 6):
            if self.itemeditv.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            elif self.itemeditcatv.get() == '' or self.itemeditstockv.get() == '' or self.itemeditwholepricev.get() == '' or self.itemeditsellpricev.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            else:
                l = [self.itemeditstockv.get()]
                for i in range(0, len(l)):
                    if (not l[i].isdigit()):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
                    elif (float(l[i]) < 0):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return

            self.cur.execute("update products set product_name=?,product_cat=?,product_wprice=?,product_sprice = ?,stocks = ?, expiry_date = ? where product_name = ?;", (self.itemeditv.get(
            ), self.itemeditcatv.get(), float(self.itemeditwholepricev.get()), float(self.itemeditsellpricev.get()), int(self.itemeditstockv.get()), str(self.itemeditexpv.get()), li[0]))
            self.base.commit()
            # self.addstock.set('')
            self.tree.delete(*self.tree.get_children())
            cur = self.getproducts(li[0])
            self.tree.selection_set(cur)


    def insertitem(self):
        self.itemeditv.set((self.itemeditv.get()).upper())
        self.itemeditcatv.set((self.itemeditcatv.get()).upper())

        y = [self.itemeditexpv.get()]
        for i in range(0, len(y)):
            try:
                datetime.datetime.strptime(y[i], '%m/%Y')
            except:
                messagebox.showerror("Error", "Invalid date Provided")
                return

        if self.itemeditv.get() == '' or self.itemeditcatv.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return

        else:
            l = [self.itemeditstockv.get()]
            for i in range(0, len(l)):
                if(not l[i].isdigit()):
                    if(i == 0):
                        messagebox.showerror(
                            "Error", "Product ID should be in numeral")
                    else:
                        messagebox.showerror("Error", "Invalid Data Provided")
                    return
                elif(int(l[i]) < 0):
                    messagebox.showerror("Error", "Invalid Data Provided")
                    return

        x = float(self.itemeditwholepricev.get())
        y = float(self.itemeditsellpricev.get())
        z = int(self.itemeditstockv.get())
        self.cur.execute("insert into products values(?,?,?,?,?,?)", (self.itemeditv.get(
        ), self.itemeditcatv.get(), float("{:.2f}".format(x)), float("{:.2f}".format(y)), z, str(self.itemeditexpv.get())))
        self.itemeditv.set('')
        self.itemeditcatv.set('')
        self.itemeditwholepricev.set('')
        self.itemeditsellpricev.set('')
        self.itemeditstockv.set('')
        self.itemeditexpv.set('')
        messagebox.showinfo('Success', 'Item Added Successfully')
        self.base.commit()
        self.buildprodtable()


    def delproduct(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!', 'Do you want to remove product from inventory?') == True and len(li) == 6:
            self.cur.execute(
                "delete from products where product_name = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getproducts()
            self.itemeditv.set('')
            self.itemeditcatv.set('')
            self.itemeditwholepricev.set('')
            self.itemeditstockv.set('')
            self.itemeditsellpricev.set('')
            self.itemeditexpv.set('')
        else:
            messagebox.showinfo('Alert', 'No Product selected')

########################################## DASHBOARD ###############################################################

 # Overview tab
    def overview(self):
        self.formframe1.place_forget()
        self.formframe2.place_forget()
        self.leftframe.place_forget()
        self.salesframe.place_forget()
        self.leftframe1.place_forget()
        
        self.overframe.place(self.overframeinfo)

        self.cur.execute("select expiry_date from products")
        li = self.cur.fetchall()
        count_date = 0
        global items
        items = []
        for i in range(0, len(li)):
            current_date = datetime.datetime.now()
            expiry_date = str(li[i][0])
            expiry_date = datetime.datetime.strptime(
                expiry_date, "%m/%Y")
            if expiry_date.year - current_date.year == 0 and expiry_date.month - current_date.month <= 6:
                count_date += 1
                if li[i][0] in items:
                    continue
                else:
                    items.append(li[i][0])
            elif expiry_date.year - current_date.year == 1 and expiry_date.month - current_date.month <= -6:
                count_date += 1
                if li[i][0] in items:
                    continue
                else:
                    items.append(li[i][0])
            self.total_countdate = f"{count_date}"

        self.cur.execute(
            "select product_wprice,product_sprice,stocks from products")
        li = self.cur.fetchall()
        costprice = 0
        sellingprice = 0
        count = 0
        gross = 0
        finishit = 0
        global fini
        fini = []
        for i in range(0, len(li)):
            myli = list(li[i])
            total_whole = myli[0] * myli[2]
            total_whole = float(total_whole)
            costprice += total_whole

            total_sell = myli[1] * myli[2]
            total_sell = float(total_sell)
            sellingprice += total_sell
            count += 1
            gross = sellingprice - costprice
            gross = float(gross)
            if myli[2] <= 2:
                finishit += 1
                if myli[2] in fini:
                    continue
                else:
                    fini.append(myli[2])
            self.finishit = f"{finishit}"
        self.total_count = f"{count}"
        self.total_cost = f"Ghc{costprice:.2f}"
        self.total_selling = f"Ghc{sellingprice:.2f}"
        self.total_gross = f"Ghc{gross:.2f}"

        self.stockframe = LabelFrame(self.overframe, width=200, height=120, bg = "#0a6fa6")
        self.stockframe.place(x=10, y=50)
        self.stockframeinfo = self.stockframe.place_info()
        Label(self.stockframe, text="Summary of Total Stock", font="poppins 10 normal",fg="#ffffff", bg="#0a6fa6").place(x=10, y=80)
        Label(self.stockframe, text=self.total_count, font="poppins 40 bold",fg="#ffffff",
              bg="#0a6fa6").place(x=10, y=10)

        self.priceframe = LabelFrame(self.overframe, width=200, height=120, bg ="#a6940a")
        self.priceframe.place(x=230, y=50)
        self.priceframeinfo = self.stockframe.place_info()
        Label(self.priceframe, text="Total Stock Price", font="poppins 10 normal",fg="#ffffff", bg="#a6940a").place(x=10, y=80)
        Label(self.priceframe, text=self.total_selling, font="poppins 16 bold",fg="#ffffff",
              bg="#a6940a").place(x=10, y=20)

        self.expireframe = LabelFrame(self.overframe, width=200, height=120, bg="#E93E3E")
        self.expireframe.place(x=450, y=50)
        self.expireframeinfo = self.stockframe.place_info()
        Label(self.expireframe, text="Expiring within 6months", font="poppins 10 normal",fg="#ffffff", bg="#E93E3E").place(x=10, y=80)
        Label(self.expireframe, text=self.total_countdate, font="poppins 40 bold",fg="#ffffff",
              bg="#E93E3E").place(x=10, y=10)     
        Button(self.expireframe, text="View All", font="poppins 10 normal",
              bg="#096e5b", fg="#ffffff", command=self.expireitems).place(x=110, y=30) 

        self.finishframe = LabelFrame(self.overframe, width=230, height=120, bg ="#05b0a2")
        self.finishframe.place(x=670, y=50)
        self.finishframeinfo = self.stockframe.place_info()
        Label(self.finishframe, text="Summary of Finished Item", font="poppins 10 normal",fg="#ffffff", bg="#05b0a2").place(x=10, y=80)
        Label(self.finishframe, text=self.finishit, font="poppins 40 bold",fg="#ffffff",
              bg="#05b0a2").place(x=10, y=10)     
        Button(self.finishframe, text="View All", font="poppins 10 normal",
              bg="#096e5b", fg="#ffffff", command=self.finishitem).place(x=120, y=30)  
        
        self.dashboard = Label(
                    self.overframe, text="Dashboard", font="poppins 16 bold", bg="#F3FDFE").place(x=10, y=10)

        self.dashboard = Label(
                    self.overframe, text="Customer Purchasing Trends", font="poppins 14 bold", bg="#F3FDFE").place(x=10, y=200)


        ##################
        self.chart = Frame(self.overframe, width = 1000, height=600)
        self.chart.place(x=10, y=250)
        self.chartinfo = self.chart.place_info()

        self.base = sqlite3.connect("login.db")
        df = pd.read_sql("select product_name, Quantity, Date from sales", self.base)
        df = df.tail(1600)


        figure1 = plt.Figure(figsize=(10, 5), dpi=100, constrained_layout=True)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.chart)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1 = df[['product_name', 'Quantity']].groupby('product_name').sum()

        df1.sort_values(by=['Quantity'], inplace = True)
        df1 = df1.tail(20)
        df1.plot(kind="bar", legend=True, ax =ax1)
        ax1.set_title("Drugs Vs Quantity sold for the pass 30 days")



     



    def expireitems(self):
        self.mainw = Toplevel(bg="#FFFFFF")
        self.mainw.geometry("750x550")
        self.mainw.title("Items Are About To expire")
        self.mainw.resizable(1, 1)

        self.main1 = LabelFrame(self.mainw, width=650,
                                height=500, bg="snow", relief="sunken")
        self.main1.place(x=100, y=40)
        # Button(self.mainw, text="close", height=3, width=8, bd=6, command=self.exir_btn,
        #        bg="#FFFFFF").place(x=50, y=470)

        scrollbarx = Scrollbar(self.main1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.main1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.main1, columns=("Product Name", 'Quantity', "Category", 'Expiry Date'),
                                 selectmode="browse", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0,
                         width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=150)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0,
                         width=150, anchor='center')
        self.tree.column('#4', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Category', text="Category", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Expiry Date', text="Expiry Date", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.expiretab()

    # def exir_btn(self):
    #     self.mainw.withdraw()
    #     self.mainw.update()

    def expiretab(self):

        for s in range(0, len(items)):
            self.cur.execute(
                "select product_name,product_cat, stocks, expiry_date from products where expiry_date =?", (items[s],))
            expirelist = self.cur.fetchall()

            for i in expirelist:

                self.tree.insert('', 'end', values=(i))

    def finishitem(self):
        self.mainw = Toplevel(bg="#FFFFFF")
        self.mainw.geometry("750x550")
        self.mainw.title("Summary of Finished Items")
        self.mainw.resizable(1, 1)

        self.main1 = LabelFrame(self.mainw, width=650,
                                height=500, bg="snow", relief="sunken")
        self.main1.place(x=100, y=40)
        Button(self.mainw, text="close", height=3, width=8, bd=6, command=self.exir_btn,
               bg="#FFFFFF").place(x=50, y=450)

        scrollbarx = Scrollbar(self.main1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.main1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.main1, columns=("Product Name",  "Category", "Quantity"),
                                 selectmode="browse", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=150)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0,
                         width=150, anchor='center')
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Category', text="Category", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.finishtab()

    def finishtab(self):
        for s in range(0, len(fini)):
            self.cur.execute(
                "select product_name,product_cat, stocks from products where stocks =?", (fini[s],))
            finilist = self.cur.fetchall()
            for i in finilist:
                self.tree.insert('', 'end', values=(i))





        ######################## overview tab ended ######################################################################### 


        #########################sales table################
     # BUILD SALES TABLE
    def buildsalestable(self):
        self.formframe1.place_forget()
        self.formframe2.place_forget()
        self.leftframe.place_forget()
        self.overframe.place_forget()
        self.leftframe1.place_forget()
        self.salesframe.place(self.salesframeinfo)

       

        self.tableframe2 = LabelFrame(self.salesframe, width=1000, height=650)
        self.tableframe2.place(x=10, y=120)
        self.tableframe2info = self.tableframe2.place_info()
        
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe2, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe2, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe2, columns=("Trans_id", "Product Name",
                                                            'Quantity', 'Total Price', 'Time', 'Date', 'Payment Method'), selectmode="browse", height=22,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=140)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=170)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Trans_id', text="Trans_id", anchor=W)
        self.tree.heading('Product Name', text="Prodect Name", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Total Price', text="Total Price", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.heading('Payment Method', text="Payment Method", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)

        self.viewbut = Button(self.salesframe, text="View Today's Sales", font="poppins 10",
                              bd=5,fg="#ffffff", bg="#096e5b", command=self.makeprint).place(x=820, y=25)

        self.getsales()
        self.mainsearch()

        self.totalsales = Label(
            self.salesframe, text="Total Sales", font="poppins 16 bold", bg="#F3FDFE").place(x=10, y=10)

    def getsales(self):
        self.cur.execute(
            "select * from sales")
        saleslist = self.cur.fetchall()
        for i in saleslist:
            i = list(i)
            i[3] = float("{:.2f}".format(i[3]))
            self.tree.insert('', 'end', values=(i))
    

    def searchinvoice(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from sales")
        saleslist = self.cur.fetchall()
        for j in saleslist:
            if (str(j[5]) == str(self.searchvar.get())):
                self.tree.insert('', 'end', values=(j))

    
    def mainsearch(self):

        self.salesframe.place(self.salesframeinfo)
        self.searchbut = Button(self.salesframe, text="Search Date",
                                font="poppins 14", fg="#ffffff", bg="#096e5b", bd=5, command=self.searchinvoice)
        self.searchbut.place(x=10, y=60, height=40)
        self.searchvar2 = StringVar()
        self.searchentry2 = myentry(
            self.salesframe, textvariable=self.searchvar, font="poppins 14", width=28, bg="#FFFFFF")
        self.searchentry2.place(x=165, y=60, height=40)

        self.cur.execute("select Date from sales")
        li = self.cur.fetchall()
        a = []
      
        for i in range(0, len(li)):
            if(a.count(str(li[i][0])) == 0):
                a.append(str(li[i][0]))
        self.searchentry2.set_completion_list(a)

        self.resetbut = Button(self.salesframe, text="Reset", font="poppins 14",
                               bd=5, bg="#FFFFFF", command=self.buildsalestable)
        self.resetbut.place(x=550, y=60, height=40) 

    
    ############################ user ######################

    def buildusertable(self):
        
        self.overframe.place_forget()
        self.salesframe.place_forget()
        self.formframe1.place_forget()
        self.leftframe.place_forget()

        self.formframe2.place(self.formframe2info)
        self.leftframe1.place( self.leftframe1info)

        self.tableframe = LabelFrame(self.formframe2, width=350, height=650)
        self.tableframe.place(x=50, y=100)
        self.tableframeinfo = self.tableframe.place_info()

        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe, columns=("Username", "Password", "Account Type"),
                                 selectmode="browse", height=17, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=170)
        self.tree.column('#2', stretch=NO, minwidth=0, width=170)
        self.tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.tree.heading('Username', text="Username", anchor=W)
        self.tree.heading('Password', text="Password", anchor=W)
        self.tree.heading('Account Type', text="Account Type", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getusers()
        self.tree.bind("<<TreeviewSelect>>", self.clickusertable)
        self.formframe1.focus_set()
        self.usernamedit = StringVar()
        self.passwordedit = StringVar()
        self.accedit = StringVar()
        va = 110
        l1 = ['Username', 'Password', 'Profile Type']
        for i in range(0, 3):
            Label(self.leftframe1, text=l1[i], font="poppins 10 normal", bg="#F3FDFE").place(
                x=5, y=va)
            va += 70
        Entry(self.leftframe1, textvariable=self.usernamedit, font="poppins 14 normal",
              bg="#FFFFFF", width=22, state='readonly').place(x=105, y=105, height=40)
        Entry(self.leftframe1, textvariable=self.passwordedit, font="poppins 14 normal",
              bg="#FFFFFF", width=22).place(x=105, y=175, height=40)
        profiles = mycombobox(self.leftframe1, font="poppins 14 normal",
                              width=20, textvariable=self.accedit)
        profiles.place(x=105, y=245, height=40)

        profiles.set_completion_list(['ADMIN', 'USER'])
        Button(self.leftframe1, text="Create a User", font="poppins 12 normal",fg="#ffffff", bg="#096e5b", bd=5,
               command=self.adduser).place(x=5, y=381)
        Button(self.leftframe1, text="Update", font="poppins 12 normal",fg="#ffffff", bg="#096e5b", bd=5,
               command=self.changeusertable).place(x=155, y=381)
        Button(self.leftframe1, text="Remove", font="poppins 12 normal",fg="#ffffff", bg="#E93E3E", bd=5,
               command=self.deluser).place(x=265, y=381)
        self.totalsales = Label(
            self.leftframe1, text="User Account", font="poppins 16 bold", bg="#F3FDFE").place(x=10, y=10)

            
      # FETCH USERS FROM USERS TABLE

    def getusers(self, x=0):
        ans = ''
        self.cur.execute("select * from users")
        userslist = self.cur.fetchall()
        for i in userslist:
            self.tree.insert('', 'end', values=(i))
            if (str(x) == i[0]):
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def changeusertable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.usernamedit.set((self.usernamedit.get()).upper())
        self.passwordedit.set((self.passwordedit.get()).upper())
        self.accedit.set((self.accedit.get()).upper())
        if (len(li) == 3):
            if self.usernamedit.get() == '' or self.accedit.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            if(self.accedit.get() != 'ADMIN' and self.accedit.get() != 'USER'):
                messagebox.showerror("Error", "Unknown account type!")
                return
            self.cur.execute(
                "update users set password = ?,account_type = ? where username = ?;", (
                    self.passwordedit.get(), self.accedit.get(), self.usernamedit.get()))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            cur = self.getusers(li[0])
            self.tree.selection_set(cur)

    def deluser(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        fa = 0
        if(self.username.get() == li[0]):
            if(messagebox.askyesno("Alert!", "Remove Current User?") == True):
                fa = 1
            else:
                return
        if messagebox.askyesno('Alert!', 'Do you want to remove this profile?') == True and len(li) == 3:
            self.cur.execute("delete from users where username = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getusers()
            self.usernamedit.set('')
            self.passwordedit.set('')
            self.accedit.set('')
        if(fa == 1):
            self.change_user()

    def adduser(self):
        self.reguser()
        self.loginw.state('normal')  # LOGIN WINDOW ENTERS

    def searchuser(self):
        if(self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from users")
        li = self.cur.fetchall()
        for i in li:
            if(i[0] == self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetusertable(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getusers()

    def clickusertable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.usernamedit.set((li[0]))
            self.passwordedit.set((li[1]))
            self.accedit.set((li[2]))


    def makeprint(self):
        self.bill_win = Toplevel(bg="#FFFFFF")
        win_width, win_height = 727, 492
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = int((screen_width/2) - (win_width/2)) - 7
        y = int((screen_height/2) - (win_height/2)) - 35
        self.bill_win.geometry(f'{win_width}x{win_height}+{x}+{y}')
        self.bill_win.resizable(1, 1)
        self.bill_win.attributes('-topmost', 'true')
        self.bill_win.title("BILL")

        bill_frame = ttk.Frame(
            self.bill_win, width=win_width, height=win_height)
        bill_frame.place(x=0, y=0)

        sales_title = ttk.Label(bill_frame, text="BILL", font="Consolas 30 bold",
                                border=7, relief="groove", anchor='c',
                                background='#282c34', foreground='#fff')
        sales_title.grid(row=0, ipadx=317)

        self.bill_text = ScrolledText(bill_frame, font="Consolas 10",
                                      width=101, height=29)
        self.bill_text.grid(row=1, sticky='W')
        now = datetime.datetime.now()
        if now.hour == 17:
            self.cus = "Morning"
        else:
            self.cus = "Aftermoon"

        heading = "Sales"
        cust_name = f"Cashier : {self.uuu}"
        cust_phno = f"Shift  : {self.cus}"
        # Defining date and time variables
        x = datetime.datetime.now()
        self.date_string = "Date : "+time.strftime("%d/%b/%Y")
        self.time_string = "Time : "+time.strftime("%I:%M:%S %p")

        self.bill_text.delete('1.0', 'end')
        self.bill_text.insert('end', "\n"+heading+"\n")
        self.bill_text.insert('end', "\n"+cust_name)
        self.bill_text.insert(
            'end', "\t\t\t\t\t\t\t\t\t"+self.date_string+"\n")
        self.bill_text.insert('end', "\n"+cust_phno)
        self.bill_text.insert(
            'end', "\t\t\t\t\t\t\t\t\t"+self.time_string+"\n\n")

        self.bill_text.insert('end', "-"*130+"\n")
        self.bill_text.insert(
            'end', "No\t   Product Name\t\t\t\t\t   Quantity\t\t     Price(Ghc)\t\t     Total(Ghc)\n")
        self.bill_text.insert('end', "-"*130+"\n")

        sum = 0.0
        x = 0
        self.cur.execute(
            'select product_name,quantity,product_sprice, total from salesday')
        self.li = self.cur.fetchall()
        for i in range(0, len(self.li)):
            item = self.li[i]
            self.bill_text.insert(
                'end', f"\n  {i+1}\t  {item[0]}\t\t\t\t\t\t{item[1]}\t\t{item[2]:.2f}\t\t{item[3]:.2f}")
            total_col = item[3]
            total_col = float(total_col)
            sum = sum + total_col
            x += 1
        self.bill_text.insert('end', "\n\n\n\n"+"-"*130+"\n")
        # print(sum)
        self.total_amt = f"Ghc {sum:.2f}"
        self.bill_text.insert('end', f"TOTAL =  {self.total_amt}")
        self.bill_text.insert('end', "\n"+"-"*130+"\n")

        # Tags and styling
        self.bill_text.tag_add('heading', '2.0', '2.end')
        self.bill_text.tag_config(
            'heading', font='Arial 20 bold', justify='center')
        self.bill_text.tag_add('customer', '4.0', '6.end')
        self.bill_text.tag_config(
            'customer', font='Consolas 11', lmargin1=20)
        self.bill_text.tag_add('sub-head', '9.0', '9.end')
        self.bill_text.tag_config(
            'sub-head', font='Consolas 12 bold', lmargin1=10)

        self.bill_text.config(state='disabled')