from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import time

root = Tk()
root.geometry("300x160")
root.title("Movie Frenzy")
clock = Label(root, font = ("Helvetica", 9, "bold"))
clock.pack(side = BOTTOM)

#movie_list = []

def tick():
    time1 = time.strftime("%H:%M:%S")
    clock.config(text = time1)
    clock.after(200, tick)

#def view_username():
#    username = Label(root, text = "Your Name.",font = ("Helvetica", 15, "bold")).place(x = 5, y = 5)
#    balance = Label(root, text = "Your Balance.", font = ("Helvetica", 15, "bold")).place(x = 5, y = 35)

#def view_movie():
#    #name_movie = Label()
#    path = "C:/Gambar/frozen.jpg"
#    img = Image.open(path)
#    img = img.resize((150, 200), Image.ANTIALIAS)
#    img = ImageTk.PhotoImage(img)
#    panelImg = Label(root, image=img)
#    panelImg.image = img
#    panelImg.pack(side = RIGHT)

#def view_price():
#    label_price = Label(root, text = "Movie Price.", font = ("Helvetica", 13, "bold")).place(x = 275, y = 235)
#    buttonRight = Button(root, text = ">").place(x = 375, y = 235)
#    buttonLeft = Button(root, text = "<").place(x = 250, y = 235) 

#def nama_film():
#    label_name = Label(root, text = "Frozen 2", font = ("Helvetica", 13, "bold")).place(x = 285, y = 5)

#def categories():
#    button_listmovie = Button(root, text = "List Movie").place(x = 10, y = 100)
#    button_sewa = Button(root, text = "My Rented Movie").place(x = 10, y = 150)

#def admin():
#    button_addmov = Button(root, text = "Add Movie").place(x = 10, y = 100)
#    button_customer = Button(root, text = "List Customer").place(x = 10, y= 150)

#def logout():
    #logout = Button(root, text = "Log Out", bg = "red").place(x = 10, y = 260)

def login():
    label_name2 = Label(root, text = "Username :").place(x = 5, y = 25)
    label_name1 = Label(root, text = "Password  :").place(x = 5, y = 50)
    getname = Entry(root).place(x = 70, y = 25)
    getname1 = Entry(root).place(x = 70, y = 50)
    path = "C:/Users/User/Desktop/web tugas01/RENTAL FILM/logo.png"
    img = Image.open(path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panelImg = Label(root, image=img)
    panelImg.image = img
    panelImg.pack(side = RIGHT)
    okButton = Button(root, text = "Login", bg = "green").place(x = 150 , y = 90)
    oButton = Button(root, text = "Register", bg = "yellow").place(x = 60 , y = 90)

def register():
    label = Label(root, text = "Register", font = ("Helvetica", 10, "bold")).place(x = 5, y = 0)
    label_name1 = Label(root, text = "First Name :").place(x = 5, y = 25)
    label_name2 = Label(root, text = "Last Name  :").place(x = 5, y = 50)
    label_name3 = Label(root, text = "Username   :").place(x = 5, y = 75)
    label_name4 = Label(root, text = "Password    :").place(x = 5, y = 100)
    getname = Entry(root).place(x = 75, y = 25)
    getname1 = Entry(root).place(x = 75, y = 50)
    getname2 = Entry(root).place(x = 75, y = 75)
    getname3 = Entry(root).place(x = 75, y = 100)
    okButton = Button(root, text = "Sign Up", bg = "yellow").place(x = 150 , y = 125)
    path = "C:/Users/User/Desktop/web tugas01/RENTAL FILM/logo.png"
    img = Image.open(path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panelImg = Label(root, image=img)
    panelImg.image = img
    panelImg.pack(side = RIGHT)


#tick()
register()
#view_username()
#view_movie()
#view_price()
#nama_film()
#categories()
#login()
#admin()

root.mainloop()
