'''
    INVENTORY MANAGEMENT SYSTEM
    Developed By->PJ28105
    Started On ->08/11/18
'''
import sqlite3
from tkinter import font, ttk
from tkinter import *
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
        self.mainframe = LabelFrame(
            self.mainw, width=1170, height=145, bg="#f7f7f7")
        self.mainframe.place(x=50, y=100)

        mi = ImageTk.PhotoImage(Image.open(
            "images/over.PNG").resize((50, 50)))
        self.items = Button(self.mainframe, text="Overviaw", bd=5, image=mi,
                            font="roboto 11 bold", compound=TOP, command=self.overview)
        self.items.image = mi
        self.items.place(x=47, y=27)

        mi = ImageTk.PhotoImage(Image.open(
            "images/invent.png").resize((50, 50)))
        self.stocks = Button(self.mainframe, text="Inventory", bd=5, image=mi,
                             font="roboto 11 bold", compound=TOP, command=self.buildprodtable)
        self.stocks.image = mi
        self.stocks.place(x=205, y=27)

        mi = ImageTk.PhotoImage(Image.open(
            "images/sales.png").resize((50, 50)))
        self.sales = Button(self.mainframe, text="Sales", bd=5, font="roboto 11 bold",
                            image=mi, compound=TOP, command=self.buildsalestable)
        self.sales.image = mi
        self.sales.place(x=355, y=27)

        mi = Image.open("images/account.png").resize((50, 50))
        mi = ImageTk.PhotoImage(mi)
        # mi = mi.subsample(a, b)
        self.accounts = Button(self.mainframe, text="Profiles", font="roboto 11 bold",
                               bd=5, image=mi, compound=TOP, command=self.buildusertable)
        self.accounts.image = mi
        self.accounts.place(x=505, y=27)

        mi = ImageTk.PhotoImage(Image.open(
            "images/sign-out.png").resize((50, 50)))
        self.changeuser = Button(self.mainframe, text="Sign out",
                                 bd=5, font="roboto 11 bold", image=mi, compound=TOP)
        self.changeuser.image = mi
        self.changeuser.place(x=655, y=27)

        mi = ImageTk.PhotoImage(Image.open(
            "images/exit.png").resize((50, 50)))
        # mi = PhotoImage(file="images/Door_Out-512.png")
        # mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="Close",
                             bd=5, font="roboto 11 bold", image=mi, compound=TOP)
        self.logout.image = mi
        self.logout.place(x=950, y=27)

        self.formframe = Frame(self.mainw, width=500, height=550, bg="#FFFFFF")
        self.formframe.place(x=100, y=315)
        self.formframeinfo = self.formframe.place_info()
        self.tableframe1 = LabelFrame(self.mainw, width=350, height=700)
        self.tableframe1.place(x=1200, y=315, anchor=NE)
        self.tableframe1info = self.tableframe1.place_info()
        self.tableframe = LabelFrame(self.mainw, width=350, height=700)
        self.tableframe.place(x=1200, y=315, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.itemframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
        self.itemframe.place(x=420, y=280, anchor=NW)
        self.itemframeinfo = self.itemframe.place_info()
        self.formframe1 = Frame(self.mainw, width=500,
                                height=445, bg="#FFFFFF")
        self.formframe1.place(x=100, y=275)
        self.formframe1info = self.formframe1.place_info()
        self.searchframe = Frame(
            self.mainw, width=720, height=70, bg="#FFFFFF")
        self.searchframe.place(x=575, y=260)
        self.searchframeinfo = self.searchframe.place_info()
        self.searchbut = Button(self.searchframe, text="Search Drug",
                                font="roboto 14", bg="#FFFFFF", bd=5, command=self.searchprod)
        self.searchbut.place(x=0, y=20, height=40)
        self.searchvar = StringVar()
        self.searchentry = myentry(
            self.searchframe, textvariable=self.searchvar, font="roboto 14", width=25, bg="#FFFFFF")
        self.searchentry.place(x=210, y=20, height=40)
        self.cur.execute("select product_name from products")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
        self.searchentry.set_completion_list(a)
        self.resetbut = Button(self.searchframe, text="Reset", font="roboto 14",
                               bd=5, width=8, bg="#FFFFFF", command=self.resetprodtabel)
        self.resetbut.place(x=510, y=20, height=40)
        self.cond = 0
        self.buildprodtable()

    # ADMIN MAIN MENU ENDS

    # BUILD PRODUCT TABLE AT INVENTORY

    def buildprodtable(self):
        self.searchframe.place_forget()
        self.tableframe.place(self.tableframeinfo)
        self.formframe.place(self.formframeinfo)
        self.tableframe1.place_forget()
        self.formframe1.place_forget()
        self.itemframe.place_forget()
        if(self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe, columns=("Product Name", "Category", "Wholesale Price",
                                                           'Selling Price', 'Quantity', 'Expiry Date'), selectmode="browse", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
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
        self.tree.bind("<<TreeviewSelect>>", self.clickprodtable)
        self.formframe.focus_set()
        self.itemeditv = StringVar()
        self.itemeditv.set("eg: EFPAC")
        self.itemeditcatv = StringVar()
        self.itemeditwholepricev = StringVar()
        self.itemeditsellpricev = StringVar()
        self.itemeditstockv = StringVar()
        self.itemeditexpv = StringVar()

        va = 5
        l1 = ['Product Name', 'Category', 'Wholsesale Price',
              'Selling Price', 'Quantity', 'Expiry Date']
        for i in range(0, 6):
            Label(self.formframe, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(
                x=0, y=va)
            va += 60
        self.entry1 = Entry(self.formframe, textvariable=self.itemeditv, font="roboto 14",
                            width=20)
        self.entry1.bind('<Button-1>', self.onclick)
        self.entry1.place(x=142, y=0, height=40)
        x = myentry(self.formframe, textvariable=self.itemeditcatv,
                    font="roboto 14", bg="#FFFFFF", width=20)
        x.place(x=142, y=60, height=40)
        self.cur.execute("select product_cat from products")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
        x.set_completion_list(a)
        Entry(self.formframe, textvariable=self.itemeditwholepricev, font="roboto 14",
              bg="#FFFFFF", width=20).place(x=142, y=120, height=40)
        Entry(self.formframe, textvariable=self.itemeditsellpricev, font="roboto 14",
              bg="#FFFFFF", width=20).place(x=142, y=180, height=40)
        Entry(self.formframe, textvariable=self.itemeditstockv, font="roboto 14",
              bg="#FFFFFF", width=20).place(x=142, y=240, height=40)

        Entry(self.formframe, textvariable=self.itemeditexpv, font="roboto 14",
              bg="#FFFFFF", width=20).place(x=142, y=300, height=40)

        Button(self.formframe, text="Add item", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.insertitem).place(x=5, y=380)
        Button(self.formframe, text="Edit", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.changeprodtable).place(x=125, y=380)
        Button(self.formframe, text="Remove Item", font="robot 10 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.delproduct).place(x=255, y=380)
        Label(self.formframe, text='Total Stock:',
              font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=440)
        Label(self.formframe, text='Total CP:',
              font="roboto 14 bold", bg="#FFFFFF").place(x=150, y=440)
        Label(self.formframe, text='Total SP:',
              font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=480)
        Label(self.formframe, text='Gross Profit:',
              font="roboto 14 bold", bg="#FFFFFF").place(x=200, y=480)

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

        self.totallable = Label(
            self.formframe, text=self.total_count, bg="#ffffff", anchor="center")
        self.totallable.config(font="Roboto 15 bold", fg="#64d979")
        self.totallable.place(x=90, y=440)

        self.totallable = Label(
            self.formframe, text=self.total_cost, bg="#ffffff", anchor="center")
        self.totallable.config(font="Roboto 15 bold", fg="#64d979")
        self.totallable.place(x=220, y=440)

        self.totallable = Label(
            self.formframe, text=self.total_selling, bg="#ffffff", anchor="center")
        self.totallable.config(font="Roboto 15 bold", fg="#64d979")
        self.totallable.place(x=70, y=480)

        self.totallable = Label(
            self.formframe, text=self.total_gross, bg="#ffffff", anchor="center")
        self.totallable.config(font="Roboto 15 bold", fg="#64d979")
        self.totallable.place(x=300, y=480)

        self.cond = 1
        self.mainsearch(1)

    # SEARCH FRAME FOR BOTH USER AND PRODUCT TABLE

    def mainsearch(self, f):
        self.searchvar.set('')
        if (f == 1):
            self.searchframe.config(width=720)
            self.searchframe.place(x=575, y=245)
            self.searchbut.config(
                text="Search Drug", command=self.searchprod)
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar, width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select product_name from products")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
            self.resetbut.config(command=self.resetprodtabel)
            self.resetbut.place(x=460, y=22, height=37)
        elif(f == 0):
            self.searchframe.place(x=661, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchuser)
            self.searchbut.config(text="Search Username")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.resetusertable)
            self.resetbut.place(x=415, y=23)
            self.cur.execute("select username from users")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
        else:
            self.searchframe.place(x=138, y=245)
            self.searchframe.config(width=720)
            self.searchbut.config(command=self.searchinvoice)
            self.searchbut.config(text="Search Date.")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.buildsalestable)
            self.resetbut.place(x=415, y=23)
            self.cur.execute("select Date from sales")
            li = self.cur.fetchall()
            a = []
           # print(li)
            for i in range(0, len(li)):
                if(a.count(str(li[i][0])) == 0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)

    # Overview tab
    def overview(self):
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place(self.itemframeinfo)

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

        Label(self.itemframe, text="Summary of Total Stock", font="Roboto 14 bold", bg="#ffffff").grid(
            row=0, column=0, pady=15, sticky="w")
        Label(self.itemframe, text="Total Stock Price", font="Roboto 14 bold", bg="#ffffff").grid(
            row=1, column=0, pady=15, sticky="w")
        Button(self.itemframe, text="Expiring within 6months", font="Roboto 14 bold", bg="#ffffff", command=self.expireitems).grid(
            row=2, column=0, pady=15, sticky="w")
        Button(self.itemframe, text="Summary of Finished Item", font="Roboto 14 bold", bg="#ffffff", command=self.finishitem).grid(
            row=3, column=0, pady=15, sticky="w")

        Label(self.itemframe, width=40, text=self.total_count, font="roboto 20 bold",
              bg="#ffffff", fg="#64d979").grid(row=0, column=1, pady=15, padx=10, ipady=3)

        Label(self.itemframe, width=40, text=self.total_selling, font="roboto 20 bold",
              bg="#ffffff", fg="#64d979").grid(row=1, column=1, pady=15, padx=10, ipady=3)

        Label(self.itemframe, width=40, text=self.total_countdate, font="roboto 20 bold",
              bg="#ffffff", fg="#64d979").grid(row=2, column=1, pady=15, padx=10, ipady=3)

        Label(self.itemframe, width=40, text=self.finishit, font="roboto 20 bold",
              bg="#ffffff", fg="#64d979").grid(row=3, column=1, pady=15, padx=10, ipady=3)

#
    def expireitems(self):
        self.mainw = Toplevel(bg="#FFFFFF")
        self.mainw.geometry("750x550")
        self.mainw.title("Items Are About To expire")
        self.mainw.resizable(1, 1)

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
        self.expiretab()

    def exir_btn(self):
        self.mainw.withdraw()
        self.mainw.update()

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
        # elif self.newitemcat.get() == '' or self.newitemwprice.get() == '' or self.newitemwprice.get() or self.newitemstock.get() == '':
        #     messagebox.showerror("Error", "Please Fill All Fields")
        #     return

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

    # BUILD USER TABLE

    def buildusertable(self):
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place(self.formframe1info)
        self.tableframe1.place(self.tableframe1info)
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Username", "Password", "Account Type"),
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
            Label(self.formframe1, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(
                x=0, y=va)
            va += 70
        Entry(self.formframe1, textvariable=self.usernamedit, font="roboto 14",
              bg="#FFFFFF", width=25, state='readonly').place(x=162, y=105, height=40)
        Entry(self.formframe1, textvariable=self.passwordedit, font="roboto 14",
              bg="#FFFFFF", width=25).place(x=162, y=175, height=40)
        profiles = mycombobox(self.formframe1, font="robot 14",
                              width=23, textvariable=self.accedit)
        profiles.place(x=162, y=245, height=40)
        profiles.set_completion_list(['ADMIN', 'USER'])
        Button(self.formframe1, text="Create a User", font="robot 12 bold", bg="#FFFFFF", bd=5, width=12, height=2,
               command=self.adduser).place(x=0, y=10)
        Button(self.formframe1, text="Update", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.changeusertable).place(x=145, y=381)
        Button(self.formframe1, text="Remove", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.deluser).place(x=345, y=381)

        self.mainsearch(0)

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

    # BUILD SALES TABLE
    def buildsalestable(self):
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe1.place(x=1130, y=315, anchor=NE)
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Trans_id", "Product Name",
                                                            'Quantity', 'Total Price', 'Time', 'Date', 'Payment Method'), selectmode="browse", height=16,
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
        self.viewbut = Button(self.searchframe, text="View Today's Sales", font="roboto 10",
                              bd=5, width=14, bg="#FFFFFF", command=self.makeprint).place(x=555, y=25)
        self.getsales()
        self.mainsearch(2)
        self.totalsales = Label(
            self.tableframe1, text="Total Sales", font="roboto 14 bold").place(x=0, y=400)

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

    def onclick(self, event):
        if (self.itemeditv.get() == "eg: EFPAC"):
            self.entry1.delete(0, "end")
