
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


class splash:
    def __init__(self):
        self.splashminw = Tk()
        self.splashminw.title("About")
        width = 1000
        height = 700
        self.splashminw.config(bg="#096e5b")
        screen_width = self.splashminw.winfo_screenwidth()
        screen_height = self.splashminw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.splashminw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.splashminw.resizable(0, 0)
        path = "images/prince.jpg"
        img = ImageTk.PhotoImage(Image.open(path).resize((400, 400)))
        main = LabelFrame(self.splashminw, width=890,
                          height=560, bg="snow", relief="sunken")
        main.place(x=55, y=70)
        photoframe = LabelFrame(
            main, width=420, height=444, bg="snow", relief="raised")
        pic = Label(photoframe, image=img)
        pic.place(x=4, y=4)
        photoframe.place(x=10, y=100)
        Label(main, text="Sales And Inventory Management System",
              font="Times 32 bold", fg="#0dd932", bg="snow").place(x=45, y=10)
        Label(main, text="Price Care Pharmacy", font="Times 32 bold", fg="#0dd932",
              bg="snow").place(x=450, y=160)
        Label(main, text="Near Zongo Market",
              font="roboto 16 bold", bg="snow").place(x=445+5, y=260)
        Label(main, text="Tel: +233-548774173, +233-544678616 ", font="roboto 16 bold",
              bg="snow").place(x=450, y=310)
        Label(main, text="Email: princecarepharm@yahoo.com",
              font="roboto 16 bold", bg="snow").place(x=445+5, y=360)
        Label(main, text="P. O. BOX AF 10, KOFORIDUA", font="roboto 16 bold",
              bg="snow").place(x=445+5, y=410)
        pic.bind('<Motion>', lambda event: self.splashminw.destroy())
       # self.splashminw.after(10000,lambda :self.splashminw.destroy())
        self.splashminw.mainloop()

      # P. O. BOX AF 10, KOFORIDUA -   Tel: +233-548774173, +233-544678616    Email: princecarepharm@yahoo.com
