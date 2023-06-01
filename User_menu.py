
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from Addtional_features import mycombobox, myentry
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import os
import time
import csv


# USER MENU


class User:
    def __init__(self, mainw, uuu):
        self.mainw = mainw
        self.uuu = uuu

    def user_mainmenu(self, a, b):
        # self.mainframe = LabelFrame(
        #     self.mainw, width=800, height=140, bg="#f7f7f7")
        # self.mainframe.place(x=230, y=120)

        self.mainframe = LabelFrame(
            self.mainw, width=200, height=820, bg="#096e5b")
        self.mainframe.place(x=0, y=60)
        self.now = datetime.date.today()

        messagebox.showinfo(
            "WELCOME", f"{self.now} \n\n Welcome {self.uuu} ")

        icon = ImageTk.PhotoImage(Image.open(
                    "images/over.PNG").resize((20, 20)))
        self.items2 = Button(self.mainframe, text=" Dashboard", fg="#FFFFFF", bd=5,  image=icon,borderwidth=0,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.overview1,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.items2.image = icon
        self.items2.place(x=10, y=25)
################################################

        icon = ImageTk.PhotoImage(Image.open(
                    "images/invent.png").resize((20, 20)))
        self.stocks = Button(self.mainframe, text=" Invoice", fg="#FFFFFF", bd=5,  image=icon,borderwidth=0,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.make_invoice ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.stocks.image = icon
        self.stocks.place(x=10, y=85)
################################################

        icon = ImageTk.PhotoImage(Image.open(
                    "images/invent.png").resize((20, 20)))
        self.stocks = Button(self.mainframe, text=" Daily Sales", fg="#FFFFFF", bd=5,  image=icon,borderwidth=0,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.make_sale ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.stocks.image = icon
        self.stocks.place(x=10, y=145)
################################################

        icon = ImageTk.PhotoImage(Image.open(
                    "images/invent.png").resize((20, 20)))
        self.stocks = Button(self.mainframe, text=" Items", fg="#FFFFFF", bd=5,  image=icon,borderwidth=0,
                                    font="poppins 16 normal",bg="#096e5b", compound=LEFT, command=self.builditemtable ,
                                    activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.stocks.image = icon
        self.stocks.place(x=10, y=205)



################################################

        mi = ImageTk.PhotoImage(Image.open(
            "images/sign-out.png").resize((20, 20)))
        self.changeuser = Button(self.mainframe, text=" Sign out   ",
                                    bd=5, font="poppins 16 normal",fg="#FFFFFF", image=mi, compound=LEFT,borderwidth=0,
                                     bg="#096e5b", activebackground='#FFFFFF' ,activeforeground='#096e5b')
        self.changeuser.image = mi
        self.changeuser.place(x=10, y=265)



################################################

        mi = ImageTk.PhotoImage(Image.open(
            "images/exit.png").resize((20, 20)))
       
        self.logout = Button(self.mainframe, text=" Quit    ", fg="#FFFFFF", 
                                     bg="#096e5b", bd=5, font="poppins 16 normal", image=mi, compound=LEFT)
        self.logout.image = mi
        self.logout.place(x=10, y=700)

################################################


        self.tableframe1 = Frame(
            self.mainw, width=150, height=500, bg="#FFFFFF")
        self.tableframe1.place(x=220, y=70)
        self.tableframe1info = self.tableframe1.place_info()

        self.tableframe = Frame(self.mainw, width=900,
                                height=900, bg="#FFFFFF")
        self.tableframe.place(x=300, y=70)
        self.tableframeinfo = self.tableframe.place_info()
        
        self.entryframe = Frame(self.mainw, width=800,
                                height=400, bg="#FFFFFF")
        self.entryframe.place(x=700, y=460+20)
        self.entryframeinfo = self.entryframe.place_info()
                                
        self.itemframe2 = Frame(
            self.mainw, bg="#FFFFFF", width=600, height=500)
        self.itemframe2.place(x=420, y=280)
        self.itemframe2info = self.itemframe2.place_info()
    
        
        self.entryframe1 = Frame(
            self.mainw, width=450, height=400, bg="#FFFFFF")
        self.entryframe1.place(x=220, y=460+20)
        self.entryframe1info = self.entryframe1.place_info()

        self.overframe1 = Frame(self.mainw, width=1050, height=860, bg="#F3FDFE")
        self.overframe1.place(x=210, y=50)
        self.overframe1info = self.overframe1.place_info()


        self.salesframe = Frame(
            self.mainw, bg="#FFFFFF", width=600, height=500)
        self.salesframe.place(x=220, y=70)
        self.salesframeinfo = self.salesframe.place_info()

        self.salesentry = Frame(
            self.mainw, bg="#FFFFFF", width=1000, height=300)
        self.salesentry.place(x=220, y=620)
        self.salesentryinfo = self.salesentry.place_info()

##
       



        self.make_invoice()

    def overview1(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.salesframe.place_forget()
        self.salesentry.place_forget()
        self.overframe1.place(self.overframe1info)

        self.cur.execute("select expiry_date from products")
        li = self.cur.fetchall()
        count_date = 0
        global items1
        items1 = []
        for i in range(0, len(li)):
            current_date = datetime.datetime.now()
            expiry_date = str(li[i][0])
            expiry_date = datetime.datetime.strptime(
                expiry_date, "%m/%Y")
            if expiry_date.year - current_date.year == 0 and expiry_date.month - current_date.month <= 6:
                count_date += 1
                if li[i][0] in items1:
                    continue
                else:
                    items1.append(li[i][0])
            elif expiry_date.year - current_date.year == 1 and expiry_date.month - current_date.month <= -6:
                count_date += 1
                if li[i][0] in items1:
                    continue
                else:
                    items1.append(li[i][0])
            self.total_countdate = f"{count_date}"

        self.cur.execute(
            "select product_wprice,product_sprice,stocks from products")
        li = self.cur.fetchall()
        costprice = 0
        sellingprice = 0
        count = 0
        gross = 0
        finishit = 0
        global fini1
        fini1 = []
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
                if myli[2] in fini1:
                    continue
                else:
                    fini1.append(myli[2])
            self.finishit = f"{finishit}"
        self.total_count = f"{count}"
        self.total_cost = f"Ghc{costprice:.2f}"
        self.total_selling = f"Ghc{sellingprice:.2f}"
        self.total_gross = f"Ghc{gross:.2f}"

        self.stockframe = LabelFrame(self.overframe1, width=200, height=120, bg = "#0a6fa6")
        self.stockframe.place(x=10, y=50)
        self.stockframeinfo = self.stockframe.place_info()
        Label(self.stockframe, text="Summary of Total Stock", font="poppins 10 normal",fg="#ffffff", bg="#0a6fa6").place(x=10, y=80)
        Label(self.stockframe, text=self.total_count, font="poppins 40 bold",fg="#ffffff",
              bg="#0a6fa6").place(x=10, y=10)


        self.priceframe = LabelFrame(self.overframe1, width=200, height=120, bg ="#a6940a")
        self.priceframe.place(x=230, y=50)
        self.priceframeinfo = self.stockframe.place_info()
        Label(self.priceframe, text="Total Stock Price", font="poppins 10 normal",fg="#ffffff", bg="#a6940a").place(x=10, y=80)
        Label(self.priceframe, text=self.total_selling, font="poppins 16 bold",fg="#ffffff",
              bg="#a6940a").place(x=10, y=20)

        self.expireframe = LabelFrame(self.overframe1, width=200, height=120, bg="#E93E3E")
        self.expireframe.place(x=450, y=50)
        self.expireframeinfo = self.stockframe.place_info()
        Label(self.expireframe, text="Expiring within 6months", font="poppins 10 normal",fg="#ffffff", bg="#E93E3E").place(x=10, y=80)
        Label(self.expireframe, text=self.total_countdate, font="poppins 40 bold",fg="#ffffff",
              bg="#E93E3E").place(x=10, y=10)     
        Button(self.expireframe, text="View All", font="poppins 10 normal",
              bg="#096e5b", fg="#ffffff", command=self.expireitems1).place(x=110, y=30) 

        self.finishframe = LabelFrame(self.overframe1, width=230, height=120, bg ="#05b0a2")
        self.finishframe.place(x=670, y=50)
        self.finishframeinfo = self.stockframe.place_info()
        Label(self.finishframe, text="Summary of Finished Item", font="poppins 10 normal",fg="#ffffff", bg="#05b0a2").place(x=10, y=80)
        Label(self.finishframe, text=self.finishit, font="poppins 40 bold",fg="#ffffff",
              bg="#05b0a2").place(x=10, y=10)     
        Button(self.finishframe, text="View All", font="poppins 10 normal",
              bg="#096e5b", fg="#ffffff", command=self.finishitems).place(x=120, y=30)  
        
        self.dashboard = Label(
                    self.overframe1, text="Dashboard", font="poppins 16 bold", bg="#F3FDFE").place(x=10, y=10)

        self.dashboard = Label(
                    self.overframe1, text="Customer Purchasing Trends", font="poppins 14 bold", bg="#F3FDFE").place(x=10, y=200)


        ##################
        self.chart = Frame(self.overframe1, width = 1000, height=600)
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

        # self.cur.execute(
        #     "select product_wprice,product_sprice,stocks from products")
        # li = self.cur.fetchall()

        # costprice = 0
        # sellingprice = 0
        # count = 0
        # gross = 0
        # finishit = 0
        # global fini1
        # fini1 = []
        # for i in range(0, len(li)):
        #     myli = list(li[i])
        #     total_whole = myli[0] * myli[2]
        #     total_whole = float(total_whole)
        #     costprice += total_whole

        #     total_sell = myli[1] * myli[2]
        #     total_sell = float(total_sell)
        #     sellingprice += total_sell
        #     count += 1
        #     gross = sellingprice - costprice
        #     gross = float(gross)
        #     self.total_count = f"{count}"
        #     self.total_cost = f"Ghc{costprice:.2f}"
        #     self.total_selling = f"Ghc{sellingprice:.2f}"
        #     self.total_gross = f"Ghc{gross:.2f}"
        #     if myli[2] <= 2:
        #         finishit += 1
        #         if myli[2] in fini1:
        #             continue
        #         else:
        #             fini1.append(myli[2])
        #     self.finishit = f"{finishit}"

        # self.cur.execute("select expiry_date from products")
        # li = self.cur.fetchall()
        # count_date = 0
        # for i in range(0, len(li)):
        #     current_date = datetime.datetime.now()
        #     expiry_date = str(li[i][0])
        #     expiry_date = datetime.datetime.strptime(
        #         expiry_date, "%m/%Y")
        #     if expiry_date.year - current_date.year == 0 and expiry_date.month - current_date.month <= 6:
        #         count_date += 1
        #     elif expiry_date.year - current_date.year == 1 and expiry_date.month - current_date.month <= -6:
        #         count_date += 1
        #     self.total_countdate = f"{count_date}"

        # Label(self.itemframe2, text="Summary of Total Stock:", font="poppins 14 bold", bg="#ffffff").grid(
        #     row=0, column=0, pady=15, sticky="w")
        # Label(self.itemframe2, text="Total Stock Price:", font="poppins 14 bold", bg="#ffffff").grid(
        #     row=1, column=0, pady=15, sticky="w")
        # Label(self.itemframe2, text="Gross Profit:", font="poppins 14 bold", bg="#ffffff").grid(
        #     row=2, column=0, pady=15, sticky="w")
        # Button(self.itemframe2, text="Expiring within 6months", font="poppins 14 bold", bg="#ffffff", command=self.expiryitems).grid(
        #     row=3, column=0, pady=15, sticky="w")
        # Button(self.itemframe2, text="Summary of Finished Item", font="poppins 14 bold", bg="#ffffff", command=self.finishitems).grid(
        #     row=4, column=0, pady=15, sticky="w")

        # Label(self.itemframe2, width=40, text=self.total_count, font="poppins 20 bold",
        #       bg="#ffffff", fg="#0dd932").grid(row=0, column=1, pady=15, padx=10, ipady=3)

        # Label(self.itemframe2, width=40, text=self.total_selling, font="poppins 20 bold",
        #       bg="#ffffff", fg="#0dd932").grid(row=1, column=1, pady=15, padx=10, ipady=3)
        # Label(self.itemframe2, width=40, text=self.total_gross, font="poppins 20 bold",
        #       bg="#ffffff", fg="#0dd932").grid(row=2, column=1, pady=15, padx=10, ipady=3)

        # Label(self.itemframe2, width=40, text=self.total_countdate, font="poppins 20 bold",
        #       bg="#ffffff", fg="#0dd932").grid(row=3, column=1, pady=15, padx=10, ipady=3)

        # Label(self.itemframe2, width=40, text=self.finishit, font="poppins 20 bold",
        #       bg="#ffffff", fg="#0dd932").grid(row=4, column=1, pady=15, padx=10, ipady=3)

    def expireitems1 (self):
        self.mainw = Toplevel(bg="#FFFFFF")
        self.mainw.geometry("750x550")
        self.mainw.title("Items About to expire")
        self.mainw.resizable(1, 1)
        self.mainw.attributes('-topmost', 'true')

        self.main1 = LabelFrame(self.mainw, width=650,
                                height=500, bg="snow", relief="sunken")
        self.main1.place(x=100, y=40)
        Button(self.mainw, text="close", height=3, width=8, bd=6, command=self.exir_btn,
               bg="#FFFFFF").place(x=50, y=470)

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
        self.expiretab1()

    def exir_btn(self):
        self.mainw.withdraw()
        self.mainw.update()
    
    def expiretab1(self):

        for s in range(0, len(items1)):
            self.cur.execute(
                "select product_name,product_cat, stocks, expiry_date from products where expiry_date =?", (items1[s],))
            expirelist = self.cur.fetchall()

            for i in expirelist:

                self.tree.insert('', 'end', values=(i))

    # def expiretab1(self):
    #     self.cur.execute("select expiry_date from products")
    #     li = self.cur.fetchall()
    #     item2 = []
    #     for i in range(0, len(li)):
    #         current_date = datetime.datetime.now()
    #         expiry_date = str(li[i][0])
    #         expiry_date = datetime.datetime.strptime(
    #             expiry_date, "%m/%Y")
    #         if expiry_date.year - current_date.year == 0 and expiry_date.month - current_date.month <= 6:
    #             if li[i][0] in item2:
    #                 continue
    #             else:
    #                 item2.append(li[i][0])
    #         elif expiry_date.year - current_date.year == 1 and expiry_date.month - current_date.month <= -6:
    #             if li[i][0] in item2:
    #                 continue
    #             else:
    #                 item2.append(li[i][0])

    #     for s in range(0, len(item2)):
    #         self.cur.execute(
    #             "select product_name,product_cat, stocks, expiry_date from products where expiry_date =?", (item2[s],))
    #         expirelist = self.cur.fetchall()

    #         for i in expirelist:

    #             self.tree.insert('', 'end', values=(i))

    def finishitems(self):
        self.mainw = Toplevel(bg="#FFFFFF")
        self.mainw.geometry("750x550")
        self.mainw.title("Summary of Finished Items")
        self.mainw.resizable(1, 1)
        self.mainw.attributes('-topmost', 'true')
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
        self.finishtabs()

    def finishtabs(self):
        for s in range(0, len(fini1)):
            self.cur.execute(
                "select product_name,product_cat, stocks from products where stocks =?", (fini1[s],))
            finilist = self.cur.fetchall()
            for i in finilist:
                self.tree.insert('', 'end', values=(i))

        ######################## overview tab ended #########################################################################

    def builditemtable(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.itemframe2.place_forget()
        self.overframe1.place_forget()
        self.tableframe1.place_forget()
        self.salesframe.place_forget()
        self.salesentry.place_forget()
        self.tableframe.place(self.tableframeinfo)
        

        self.searchbut = Button(self.tableframe, text="Search Drug", fg="#ffffff",
                                font="poppins 14", bg="#096e5b", bd=5, command=self.searchprod)
        self.searchbut.place(x=10, y=20, height=40)

        self.searchvar = StringVar()
        self.searchentry = myentry(
            self.tableframe, textvariable=self.searchvar, font="poppins 14", width=32, bg="#FFFFFF")
        self.searchentry.place(x=145, y=20, height=40)

        self.cur.execute("select product_name from products")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
        self.searchentry.set_completion_list(a)
        
        self.resetbut = Button(self.tableframe, text="Reset", font="poppins 14",
                               bd=5, bg="#FFFFFF", command=self.resetprodtabel)
        self.resetbut.place(x=540, y=20, height=40)

        self.tableframe2 = LabelFrame(self.tableframe, width=700, height=800)
        self.tableframe2.place(x=10, y=100)
        self.tableframe2info = self.tableframe2.place_info()

        scrollbarx = Scrollbar(self.tableframe2, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe2, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe2, columns=("Product Name", "Category", "Wholesale Price",
                                                           'Selling Price', 'Stocks', 'Expiry Date'), selectmode="extended", height=30,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)

        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Category', text="Category", anchor=W)
        self.tree.heading('Wholesale Price', text="Wholesale Price", anchor=W)
        self.tree.heading('Selling Price', text="Selling Price", anchor=W)
        self.tree.heading('Stocks', text="Stocks", anchor=W)
        self.tree.heading('Expiry Date', text="Expiry Date", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getproducts()


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

    def getproducts(self):
        self.cur.execute("select * from products")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))

#################################### Make sales #############################################################################

    def make_sale(self):
        self.tableframe.place_forget()
        self.itemframe2.place_forget()
        self.overframe1.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
    
        self.salesframe.place(self.salesframeinfo)
        self.salesentry.place(self.salesentryinfo)

        scrollbarx = Scrollbar(self.salesframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.salesframe, orient=VERTICAL)
        self.tree = ttk.Treeview(self.salesframe, columns=("Trans ID", "Product Name", 'Price', 'Quantity', 'Total', 'Time',
                                 'Payment Method', 'Customer Name', 'Customer Number'), selectmode="browse", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=60)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0,
                         width=110, anchor='center')
        self.tree.column('#4', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#5', stretch=NO, minwidth=0,
                         width=120, anchor='center')
        self.tree.column('#6', stretch=NO, minwidth=0,
                         width=120, anchor='center')
        self.tree.column('#7', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#8', stretch=NO, minwidth=0, width=120)
        self.tree.column('#9', stretch=NO, minwidth=0, width=120)

        self.tree.heading('Trans ID', text="Trans ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Total', text="Total", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.heading('Payment Method', text="Payment Method", anchor=W)
        self.tree.heading('Customer Name', text="Customer Name", anchor=W)
        self.tree.heading('Customer Number', text="Customer Number", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.clicktranstable)
        self.cur.execute("select * from todaysales")
        lisales = self.cur.fetchall()
        for l in lisales:
            l = list(l)
            l[2] = float("{:.2f}".format(l[2]))
            l[4] = float("{:.2f}".format(l[4]))
            self.tree.insert('', 'end', values=(l))
        self.sales_sum()
    
    def sales_sum(self):
        self.addpay = StringVar()
        self.total = DoubleVar(value=0)
        self.cashpay = DoubleVar(value=0)
        self.momopay = DoubleVar(value=0)

        self.cur.execute('select total from todaysales')
        tlist = self.cur.fetchall()
        for t in range(len(tlist)):
            self.total.set(self.total.get() +
                           float("{:.2f}".format(tlist[t][0])))

        
        self.cur.execute('select total from todaysales where pay_method =?', ("Cash",))
        clist = self.cur.fetchall()
        for c in range(len(clist)):
        
            self.cashpay.set(self.cashpay.get() +
                           float("{:.2f}".format(clist[c][0])))

        self.cur.execute('select total from todaysales where pay_method =?', ("MoMo",))
        mlist = self.cur.fetchall()
        for m in range(len(mlist)):
            self.momopay.set(self.momopay.get() +
                           float("{:.2f}".format(mlist[m][0])))

        Label(self.salesentry, text="Cash Payment:",
              font="poppins 10 normal", bg="#ffffff").place(x=20, y=100)
        cartcash = Entry(self.salesentry, textvariable=self.cashpay,
                          width=8, state='readonly', bg="#a89932", font="poppins 14 normal")
        cartcash.place(x=130, y=100, height=30)


        Label(self.salesentry, text="Momo Payment:",
              font="poppins 10 normal", bg="#ffffff").place(x=350, y=100)  
        cartmomo = Entry(self.salesentry, textvariable=self.momopay,
                          width=8, state='readonly', bg="#a89932", font="poppins 14 normal")
        cartmomo.place(x=470, y=100, height=30)

        Label(self.salesentry, text="Total Sales",
              font="poppins 16 bold", fg="#a89932").place(x=650, y=100)
        carttotal = Entry(self.salesentry, textvariable=self.total,
                          width=10, state='readonly', bg="#a89932", font="poppins 14 normal")
        carttotal.place(x=810, y=100, height=30)

        # Button(self.entryframe, text="Remove", command=self.removecart, bd=10,fg="#ffffff",
        #          bg="#E93E3E", font="poppins 12 normal").place(x=200, y=180)
        
        Button(self.salesentry, text="Close Sales", command=self.transtable,fg="#ffffff",  bd=10, width=100,
                 bg="#096e5b", font="poppins 12 normal").place(x=20, y=10)


    def transtable(self):
        x = self.tree.get_children()
        if(len(x) == 0):
            messagebox.showerror('Error', 'Empty cart!')
            return
        if (messagebox.askyesno('Alert!', 'Do you want to close sales') == False):
            return

        self.cur.execute(
            "select Trans_id, product_name, quantity, total, Time, pay_method, cus_name, cus_number from todaysales")
        lisales = self.cur.fetchall()
        for i in lisales:
            i = list(i)
            now = datetime.datetime.now()
            i.insert(5, str(now.day)+'/'+str(now.month)+'/'+str(now.year))

            self.cur.execute("insert into sales values (?,?,?,?,?,?,?,?,?)", (int(
                i[0]), i[1], int(i[2]), float(i[3]), i[4], i[5], i[6], i[7], i[8]))

            self.base.commit()
        messagebox.showinfo('Success', 'Transaction Successful!')
        self.makeprint1()



##################################################################################################################
            

    def make_invoice(self):
        self.tableframe.place_forget()
        self.itemframe2.place_forget()
        self.overframe1.place_forget()
        self.salesframe.place_forget()
        self.salesentry.place_forget()
        self.entryframe.place(self.entryframeinfo)
        self.entryframe1.place(self.entryframe1info)
        self.tableframe1.place(self.tableframe1info)
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Trans ID", "Product Name", 'Price', 'Quantity', 'Total', 'Time',
                                 'Payment Method', 'Customer Name', 'Customer Number'), selectmode="browse", height=16, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=60)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0,
                         width=110, anchor='center')
        self.tree.column('#4', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#5', stretch=NO, minwidth=0,
                         width=120, anchor='center')
        self.tree.column('#6', stretch=NO, minwidth=0,
                         width=120, anchor='center')
        self.tree.column('#7', stretch=NO, minwidth=0,
                         width=100, anchor='center')
        self.tree.column('#8', stretch=NO, minwidth=0, width=120)
        self.tree.column('#9', stretch=NO, minwidth=0, width=120)

        self.tree.heading('Trans ID', text="Trans ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Total', text="Total", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.heading('Payment Method', text="Payment Method", anchor=W)
        self.tree.heading('Customer Name', text="Customer Name", anchor=W)
        self.tree.heading('Customer Number', text="Customer Number", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.clicktranstable)
        self.cur.execute("select * from salesday")
        lisales = self.cur.fetchall()
        for l in lisales:
            l = list(l)
            l[2] = float("{:.2f}".format(l[2]))
            l[4] = float("{:.2f}".format(l[4]))
            self.tree.insert('', 'end', values=(l))
        self.user_input()

    def user_input(self):
        self.cur.execute('select max(trans_id) from salesday')
        li = self.cur.fetchall()
        if(li[0][0] != None):
            self.transid = li[0][0] + 1
        else:
            self.transid = 1
        self.qty = StringVar(value=1)
        self.name = StringVar()
        self.number = StringVar()
        self.additem = StringVar()
        self.addpay = StringVar()
        self.total = DoubleVar(value=0)
        self.cashpay = DoubleVar(value=0)
        self.momopay = DoubleVar(value=0)

        self.cur.execute('select total from salesday')
        tlist = self.cur.fetchall()
        for t in range(len(tlist)):
            self.total.set(self.total.get() +
                           float("{:.2f}".format(tlist[t][0])))

        
        self.cur.execute('select total from salesday where pay_method =?', ("Cash",))
        clist = self.cur.fetchall()
        for c in range(len(clist)):
        
            self.cashpay.set(self.cashpay.get() +
                           float("{:.2f}".format(clist[c][0])))

        self.cur.execute('select total from salesday where pay_method =?', ("MoMo",))
        mlist = self.cur.fetchall()
        for m in range(len(mlist)):
            self.momopay.set(self.momopay.get() +
                           float("{:.2f}".format(mlist[m][0])))

        # Label(self.entryframe, text="Cash Payment",
        #       font="poppins 10 normal", bg="#ffffff").place(x=350, y=280)
        
        # Label(self.entryframe, text="Momo Payment",
        #       font="poppins 10 normal", bg="#ffffff").place(x=350, y=340)  

        # cartcash = Entry(self.entryframe, textvariable=self.cashpay,
        #                   width=8, state='readonly', bg="#a89932", font="poppins 14 normal")
        # cartcash.place(x=450, y=280, height=30)

        # cartmomo = Entry(self.entryframe, textvariable=self.momopay,
        #                   width=8, state='readonly', bg="#a89932", font="poppins 14 normal")
        # cartmomo.place(x=450, y=340, height=30)
       
        Button(self.entryframe, text="Add to cart", command=self.addtotrans, bd=10, width=16,fg="#ffffff",
                 bg="#096e5b", font="poppins 12 normal").place(x=20, y=200)
        Button(self.entryframe, text="Remove", command=self.removecart, bd=10, width=16,fg="#ffffff",
                 bg="#E93E3E", font="poppins 12 normal").place(x=250, y=200)
        entercart = mycombobox(self.entryframe,
                               textvariable=self.additem, font="poppins 10 normal")
        entercart.place(x=20, y=60, height=30)
        cartqty = Entry(self.entryframe, textvariable=self.qty,
                        width=9, bg="#ffffff", font="poppins 10 normal")
        cartqty.place(x=220, y=60, height=30)
       
        cartname = Entry(self.entryframe, textvariable=self.name,
                         bg="#ffffff", font="poppins 10 normal")
        cartname.place(x=20, y=130, height=30, width=170)

        cartnum = Entry(self.entryframe, textvariable=self.number,
                         bg="#ffffff", font="poppins 10 normal")
        cartnum.place(x=250, y=130, height=30,width=170)

        enterpayment = ttk.Combobox(
            self.entryframe, width=14, textvariable=self.addpay, state='readonly', font="poppins 10 normal")
        enterpayment['values'] = ["Cash", "MoMo"]
        enterpayment.current(0)
        enterpayment.place(x=320, y=60, height=30)

        Label(self.entryframe, text="Quantity",
              font="poppins 12 normal", bg="#ffffff").place(x=220, y=30)
        
        Label(self.entryframe, text="Customer",
              font="poppins 12 normal", bg="#ffffff").place(x=20, y=100)

        Label(self.entryframe, text="Phone",
              font="poppins 12 normal", bg="#ffffff").place(x=250, y=100)

        Label(self.entryframe, text="Payment Method",
              font="poppins 12 normal", bg="#ffffff").place(x=320, y=30)

        Label(self.entryframe, text="Search",
              font="poppins 12 normal", bg="#ffffff").place(x=20, y=30)
        
        Button(self.entryframe, text="Make Invoice", command=self.transtableadd,fg="#ffffff",  bd=10, width=40,
                 bg="#096e5b", font="poppins 12 normal").place(x=20, y=280)

        self.today = x = str(datetime.datetime.now().strftime("%d-%m-%y"))
        Label(self.tableframe1, text="Sales Date : "+str(self.today),
              font="poppins 14 normal", bg="#ffffff").grid(row=0, column=0)

        self.cur.execute("select product_name,product_sprice from products")
        li = self.cur.fetchall()
        self.inventory = []
        self.desc_price = dict()
        for i in range(0, len(li)):
            if (self.inventory.count(li[i][0]) == 0):
                self.inventory.append(li[i][0])
            self.desc_price[li[i][0]] = li[i][1]
        entercart.set_completion_list(self.inventory)

        li = ['Product Name', 'Price', 'Left Stock']
        va = 50
        for i in range(0, 3):
            Label(self.entryframe1, text=li[i], font="poppins 14 bold", bg="#FFFFFF").place(
                x=0, y=va)
            va += 65
        self.cartitem = StringVar()
        self.cartitemprice = StringVar()
        self.cartitemstock = StringVar()
        Entry(self.entryframe1, textvariable=self.cartitem, font="poppins 14",
               width=20, state='readonly').place(x=162, y=50, height=40)
        Entry(self.entryframe1, textvariable=self.cartitemprice, font="poppins 14",
               width=20, state='readonly').place(x=162, y=115, height=40)
        Entry(self.entryframe1, textvariable=self.cartitemstock, font="poppins 14",
               width=20, state='readonly').place(x=162, y=180, height=40)
        Label(self.entryframe1, text="Total Sales",
              font="poppins 16 bold", fg="#a89932").place(x=0, y=250)
        carttotal = Entry(self.entryframe1, textvariable=self.total,
                          width=16, state='readonly', bg="#a89932", font="poppins 14 normal")
        carttotal.place(x=162, y=250, height=40)

    def addtotrans(self):
        if(len(self.additem.get()) == 0 or self.inventory.count(self.additem.get()) == 0):
            messagebox.showerror("Error", "Product Not Found!")
            return
        else:
            if(not self.qty.get().isdigit()):
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            if(int(self.qty.get()) <= 0):
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            self.cur.execute(
                "select product_name, product_sprice from products where product_name = ? ", (self.additem.get(),))
            row = self.cur.fetchall()
            row = [list(row[0])]
            row[0].insert(0, self.transid)
            row[0].append(int(self.qty.get()))
            row[0].append(
                (int(self.qty.get())*self.desc_price[self.additem.get()]))
            x = datetime.datetime.now()
            x = str(x.hour)+' : '+str(x.minute)+' : '+str(x.second)
            row[0].append(x)
            row[0].append(str(self.addpay.get()))
            row[0].append(str(self.name.get()))
            row[0].append(str(self.number.get()))
            row = [tuple(row[0])]

            self.cartitemprice.set(self.desc_price[self.additem.get()])
            self.cartitem.set(row[0][1])
            self.cur.execute(
                "select stocks from products where product_name=?", (row[0][1],))
            li = self.cur.fetchall()
            if(li[0][0]-int(self.qty.get()) < 0):
                if(li[0][0] != 0):
                    messagebox.showerror(
                        'Error', 'Product with this quantity not available!')
                else:
                    messagebox.showerror('Error', 'Product out of stock!')
                return

            self.cartitemstock.set(li[0][0]-row[0][3])
            for data in row:
                self.cur.execute("insert into salesday values (?,?,?,?,?,?,?,?,?)", (int(data[0]), data[1], float(
                    data[2]), int(data[3]), float(data[4]), data[5], data[6], data[7], data[8]))

                self.cur.execute(
                    "select stocks from products where product_name=?", (data[1],))
                l = self.cur.fetchall()
                self.cur.execute("update products set stocks=? where product_name=?",
                                 (l[0][0]-data[3], data[1]))
                self.base.commit()
            # self.total.set(self.total.get() + (int(self.qty.get())
            #                * self.desc_price[self.additem.get()]))
            self.make_invoice()

    def transtableadd(self):
        x = self.tree.get_children()
        if(len(x) == 0):
            messagebox.showerror('Error', 'Empty cart!')
            return
        if (messagebox.askyesno('Alert!', 'Do you want to close sales') == False):
            return

        self.cur.execute(
            "select * from salesday")
        liinv = self.cur.fetchall()
        for i in liinv:
            i = list(i)
            # now = datetime.datetime.now()
            # i.insert(5, str(now.day)+'/'+str(now.month)+'/'+str(now.year))

            self.cur.execute("insert into todaysales values (?,?,?,?,?,?,?,?,?)", (int(
                i[0]), i[1], int(i[2]), float(i[3]), i[4], i[5], i[6], i[7], i[8]))

            self.base.commit()
        messagebox.showinfo('Success', 'Transaction Successful!')
        # self.makeprint1()
        self.cur.execute(
            "delete from salesday")
        self.base.commit()
        self.tree.delete(*self.tree.get_children())
        self.cartitemstock.set('')
        self.cartitem.set('')
        self.total.set(0)
        self.cartitemprice.set('')
        self.additem.set('')
        self.qty.set('1')

    def removecart(self):
        re = self.tree.selection()
        if(len(re) == 0):
            messagebox.showerror('Error', 'No cart selected')
            return
        if (messagebox.askyesno('Alert!', 'Remove cart?') == True):
            x = self.tree.get_children()
            re = re[0]
            l = []
            self.fi = []
            for i in x:
                if(i != re):
                    l.append(tuple((self.tree.item(i))['values']))
                else:
                    self.fi = ((self.tree.item(i))['values'])

            self.cur.execute(
                "delete from salesday where trans_id = ?;", (self.fi[0],))
            self.base.commit()
            self.cur.execute(
                "select stocks from products where product_name=?", (self.fi[1],))
            l = self.cur.fetchall()
            self.cur.execute("update products set stocks=? where product_name=?",
                             (l[0][0]+self.fi[3], self.fi[1]))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            for i in l:
                self.tree.insert('', 'end', values=(i))
            self.cartitemstock.set('')
            self.cartitem.set('')
            self.cartitemprice.set('')
            self.additem.set('')
            self.name.set('')
            self.number.set('')
            self.qty.set('1')
            # self.fi[1] -= self.fi[3]
            self.total.set(self.total.get()-float(self.fi[4]))
            self.make_invoice()

    def makeprint1(self):
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
            'select product_name,quantity,product_sprice, total from todaysales')
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

        # Disabling modification of bill
        self.bill_text.config(state='disabled')

        self.write_to_disk(self.bill_win)

    #=======================  Other METHODS  ========================================#
    def write_to_disk(self, widget):
        date_string = time.strftime("%d-%b-%Y")
        time_string = time.strftime("%I-%M-%S %p")
        # Declaring variable for creating Current Date\ Time folder
        folder = f"{date_string}/{time_string}"  # Date folder/Time folder
        if not os.path.exists(f"Bill Records//{folder}"):
            os.makedirs(f"Bill Records/{folder}")

        # Write to Local Disk as text file
        file = open(
            f"Bill Records/{folder}/{self.uuu}, {self.cus}.txt", "w")
        file.write(self.bill_text.get('1.0', 'end').replace('Ghs', 'Rs'))
        file.close()

        # Write to Local Disk as csv file
        # Headings
        headings = [['CUSTOMER NAME', f'{self.uuu}'], [
            'CUSTOMER CONTACT', f'{self.cus}']]
        # field names
        fields = ['PRODUCT NAME', 'QUANTITY', "RATE(GHc)", "TOTAL(Ghc)"]
        # Total
        total = ['TOTAL', '', '', f'{self.total_amt}']

        # writing to csv file
        with open(f"Bill Records/{folder}/{self.uuu}, {self.cus}.csv", 'w', encoding='utf-8-sig', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # Writing the headings
            csvwriter.writerows(headings)
            # Adding blank line
            csvwriter.writerows([''])
            # Writing the fields
            csvwriter.writerow(fields)
            # Writing the items rows
            csvwriter.writerows(self.li)
            # Adding blank line
            csvwriter.writerows([''])
            # Writting total amount
            csvwriter.writerow(total)

        self.cur.execute(
            "delete from todaysales")
        self.base.commit()
        self.tree.delete(*self.tree.get_children())
        self.cartitemstock.set('')
        self.cartitem.set('')
        self.total.set(0)
        self.cartitemprice.set('')
        self.additem.set('')
        self.qty.set('1')

    def clicktranstable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li1 = cur['values']
        if (len(li1) == 7):
            self.cartitem.set((li1[0]))
            self.cur.execute(
                "select product_sprice,stocks from products where product_name=?", (li1[1],))
            li = self.cur.fetchall()
            self.cartitemprice.set(li[0][0])
            self.cartitemstock.set(li[0][1]-li1[3])
