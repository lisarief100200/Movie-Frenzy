from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk
from cassandra.cluster import Cluster
import time

def start():
    global root
    root = Tk()
    app = View(root)

class Model:
    def __init__(self):
        self.cluster = cluster

    def list_customer():
        print("Please Wait...")
        print("Reaching Cassandra...")
        print("Make Sure You're Connecting to Cassandra")
        print("===========================================")
        print("")
        cluster = Cluster(['127.0.0.1'], port=9042)
        session = cluster.connect()

class Controller:
    global username_admin, password_admin, username, password
    username_admin = ("admin")
    password_admin = ("admin")

    username = ("user")
    password = ("user")

    def __init__(self):
        self.home_admin = View.home_admin(home)
        self.home_user = View.home_user(home)
        
    def list_movie():
        print("===========================================")
        action = ["I Am Legend", "Lucy", "World War Z", "IP Man", "Inception", "Deadpool"]
        print("GENRE : ACTION")
        for title in action:
            print(title)
        print("")
        animation = ["Coco", "Frozen 2", "Toy Story 3", "Moana", "Zootopia", "Finding Dory"]
        print("GENRE : ANIMATION")
        for title in animation:
            print(title)
        print("")
        horror = ["Pengabdi Setan", "Hereditary", "A Quiet Place", "The Grudge", "Us", "Midsommar"]
        print("GENRE : HORROR")
        for title in horror:
            print(title)
        print("")
        comedy = ["The Hangover", "Spy", "We're The Millers", "22 Jumpstreet", "Cek Toko Sebelah", "Orang Kaya Baru"]
        print("GENRE : COMEDY")
        for title in comedy:
            print(title)
        print("===========================================")
    
    def verify_login():
        print("Trying to login...")
        if get_username.get() == username_admin and get_password.get() == password_admin:
            messagebox.showinfo("Movie Frenzy", "Login Successful as an Admin!", icon = "info")
            return View.home_admin(root)
        elif get_username.get() in username and get_password.get() in password:
            messagebox.showinfo("Movie Frenzy", "Login Successful!", icon = "info")
            return View.home_user(root)
        else:
            messagebox.showinfo("Movie Frenzy", "Please enter valid infomation!", icon = "warning")

    def check_regis():
        print("Trying to register...")

        if get_username_regis.get() != username:
            messagebox.showinfo("Movie Frenzy", "Registration Completed Successfully", icon = "info")
            print(get_username_regis.get())
            window.destroy()
        else:
            messagebox.showinfo("Movie Frenzy", "Register Failed", icon = "warning") 

    def view_list():
        # View List
        genre_action = ["I Am Legend", "Lucy", "World War Z", "IP Man", "Inception", "Deadpool"]
        genre_animation = ["Coco", "Frozen 2", "Toy Story 3", "Moana", "Zootopia", "Finding Dory"]
        genre_horror = ["Pengabdi Setan", "Hereditary", "A Quiet Place", "The Grudge", "Us", "Midsommar"]
        genre_comedy = ["The Hangover", "Spy", "We're The Millers", "22 Jumpstreet", "Cek Toko Sebelah", "Orang Kaya Baru"]
        
        if genreCombo.get() == "Action":
            return View.genre_action(home)

        if genreCombo.get() == "Animation":
            return View.genre_animation(home)

        if genreCombo.get() == "Horror":
            return View.genre_horror(home)

        if genreCombo.get() == "Comedy":
            return View.genre_comedy(home)

    def list_cust_rented_movie():
        print("List Film Yang Disewa :")
        for i in cust_rented_movie:
            print("- ", i)
        print("")

    def rented_movie():
        global balance
        if balance >= 5000:
            print("===========================================")
            if movieCombo.get() in cust_rented_movie:
                print("GAGAL, Film", movieCombo.get(), "Sudah Disewa!")
                print("===========================================")
            else:
                print("BERHASIL, Film ",movieCombo.get(), " Berhasil Disewa!")
                cust_rented_movie.append(movieCombo.get())
                balance = balance - 5000
                print("===========================================")
        else:
            print("Maaf, Saldo Anda Tidak Cukup")
        print("Saldo Sekarang : Rp.", balance)
        print("")

    def return_movie_():
        if return_Combo.get() in cust_rented_movie:
            cust_rented_movie.remove(return_Combo.get())
            print("Film ", return_Combo.get(), " telah dikembalikan!")
            print("")
        else:
            pass
        print("List Film Yang Disewa :")
        for i in cust_rented_movie:
            print("- ", i)
        print("")
    
    def return_movie():
        global return_Combo
        
        return_Combo = tkinter.ttk.Combobox(home, width=15, values = list(cust_rented_movie), state="readonly")
        return_Combo.set("SELECT MOVIE :")
        return_buttonCombobox = tkinter.ttk.Button(home, text = "Return", command = Controller.return_movie_)
        return_Combo.place(x = 10, y = 300)
        return_buttonCombobox.place(x = 150, y = 300)

    def add_movie():
        print("ADD MOVIE")

class View:
    global home
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Frenzy")
        self.root.geometry("300x200")
        self.login = View.login(self)

    def login(self):
        global get_username, get_password
        
        # Username & Password
        self.label_username = Label(root, text = "Username:")
        self.get_username = Entry(root)
        self.label_password = Label(root, text = "Password:")
        self.get_password = Entry(root, show = "*")

        get_username = self.get_username 
        get_password = self.get_password  

        # Login & Register Button
        self.loginButton = Button(self.root, text = "Login", command = Controller.verify_login, bg = "green")
        self.registerButton = Button(self.root, text = "Register", command = self.goto_register, bg = "yellow")

        self.space_between1 = Label(root, text = "")
        self.space_between2 = Label(root, text = "", font = ("Helvetica", 5, "bold"))

        # Show Clock
        self.clock = Label(self.root, font = ("Helvetica", 9, "bold"))
        self.time1 = time.strftime("%H:%M")
        self.clock.config(text = self.time1)
        self.clock.after(200)
    
        # Show Image
        self.path = "C:/Users/User/Desktop/LISA/web tugas01/RENTAL FILM/logo.png"
        self.img = Image.open(self.path)
        self.img = self.img.resize((150, 150), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panelImg = Label(root, image=self.img)
        self.panelImg.image = self.img
        self.panelImg.pack(side = RIGHT)

        self.label_username.pack()
        self.get_username.pack()
        self.label_password.pack()
        self.get_password.pack()
        self.space_between1.pack()
        self.loginButton.pack()
        self.space_between2.pack()
        self.registerButton.pack()
        self.clock.pack(side = BOTTOM)

    def goto_register(self):
        global get_first_name, get_last_name, get_username_regis, get_password_regis, window
        
        # Register Window
        self.window = Tk()
        self.window.title("Movie Frenzy")
        self.window.geometry("390x210")
        self.label_regis = Label(self.window, text = "Register", font = ("Helvetica", 15, "bold")).place(x = 5, y = 0)
        self.label_first_name = Label(self.window, text = "First Name  :").place(x = 60, y = 40)
        self.get_first_name = Entry(self.window)
        self.label_last_name = Label(self.window, text = "Last Name  :").place(x = 60, y = 72)
        self.get_last_name = Entry(self.window)
        self.label_username_regis = Label(self.window, text="Username   :").place(x = 60, y = 104)
        self.get_username_regis = Entry(self.window)
        self.label_password_regis = Label(self.window, text="Password    :").place(x = 60, y = 136)
        self.get_password_regis = Entry(self.window, show="*")
        self.go_register = Button(self.window, text = "Register", command = Controller.check_regis, bg = "yellow")

        # Space
        self.space_between3 = Label(self.window, text = "")
        self.space_between4 = Label(self.window, text = "")
        self.space_between5 = Label(self.window, text = "", font = ("Helvetica", 5, "bold"))
        self.space_between6 = Label(self.window, text = "", font = ("Helvetica", 5, "bold"))
        self.space_between7 = Label(self.window, text = "", font = ("Helvetica", 5, "bold"))
        self.space_between8 = Label(self.window, text = "", font = ("Helvetica", 5, "bold"))

        get_first_name = self.get_first_name
        get_last_name = self.get_last_name
        get_username_regis = self.get_username_regis
        get_password_regis = self.get_password_regis
        window = self.window

        # PACK REGISTER
        self.space_between3.pack()
        self.space_between4.pack()
        self.get_first_name.pack()
        self.space_between5.pack()
        self.get_last_name.pack()
        self.space_between6.pack()
        self.get_username_regis.pack()
        self.space_between7.pack()
        self.get_password_regis.pack()
        self.space_between8.pack(side = BOTTOM)
        self.go_register.pack(side = BOTTOM)

    def home_admin(self):
        root.destroy()
        self.home = Tk()
        self.home.title("Movie Frenzy")
        self.home.geometry("300x275")

        self.balance = 250000

        # Label Home Admin
        self.label_home_username = Label(self.home, text = "Hi, Admin", font = ("Helvetica", 15, "bold")).place(x = 5, y = 0)
        self.label_home_balance = Label(self.home, text = "Your Balance : Rp.", font = ("Helvetica", 12, "bold")).place(x = 5, y = 35)
        self._home_balance = Label(self.home, text = int(self.balance), font = ("Helvetica", 12, "bold")).place(x = 150, y = 35)

        # Label Home Admin
        self.clock = Label(self.home, font = ("Helvetica", 15, "bold"))
        self.time1 = time.strftime("%H:%M")
        self.clock.config(text = self.time1)
        self.clock.after(200)
        self.clock.pack(side = BOTTOM)

        # Button
        self.list_movieButton = Button(self.home, text = "List Movie", command = Controller.list_movie).place(x = 10, y = 100)
        self.list_customerButton = Button (self.home, text = "List Costumer", command = Model.list_customer).place(x = 10, y = 150)
        self.add_movieButton = Button (self.home, text = "Add Movie", command = Model.list_customer).place(x = 10, y = 200)

        # Button Logout
        self.logout = Button(self.home, text = "Log Out", bg = "red", font = ("Helvetica", 10, "bold")).place(x = 225, y = 225)

    def home_user(self):
        global home, genreCombo, cust_rented_movie, balance
        root.destroy()
        self.home = Tk()
        self.home.title("Movie Frenzy")
        self.home.geometry("500x375")

        self.balance = 250000

        # Label Home User
        self.label_home_username = Label(self.home, text = "Hi, User", font = ("Helvetica", 15, "bold")).place(x = 5, y = 0)
        self.label_home_balance = Label(self.home, text = "Your Balance : Rp.", font = ("Helvetica", 12, "bold")).place(x = 5, y = 35)
        self.home_balance = Label(self.home, text = int(self.balance), font = ("Helvetica", 12, "bold")).place(x = 150, y = 35)

        # Label Home Admin
        self.clock = Label(self.home, font = ("Helvetica", 15, "bold"))
        self.time1 = time.strftime("%H:%M")
        self.clock.config(text = self.time1)
        self.clock.after(200)
        self.clock.pack(side = BOTTOM)

        self.cust_rented_movie = []

        # Button
        self.label = Label(self.home, text = "Choose Genre Film.", font = ("Helvetica", 10, "bold")).place(x = 8, y = 75)
        self.list_movieButton = Button(self.home, text = "List Movie", command = Controller.list_movie).place(x = 10, y = 150)
        self.list_costumerButton = Button(self.home, text = "My Rented Movie", command = Controller.list_cust_rented_movie).place(x = 10, y = 200)
        self.list_return_movie = Button(self.home, text = "Return Movie", bg = "orange", font = ("Helvetica", 10, "bold"), command = Controller.return_movie).place(x = 10, y = 250)

        genre = ["Action", "Animation", "Horror", "Comedy"]

        # Pilih Genre
        self.genreCombo = tkinter.ttk.Combobox(self.home, width=15, values = list(genre), state="readonly")
        self.genreCombo.set("SELECT GENRE :")
        self.buttonCombobox = tkinter.ttk.Button(self.home, text = "Find", command = Controller.view_list)
        self.genreCombo.place(x = 10, y = 100)
        self.buttonCombobox.place(x = 150, y = 98)

        genreCombo = self.genreCombo
        home = self.home
        cust_rented_movie = self.cust_rented_movie
        balance = self.balance

        # Button Logout
        logout = Button(self.home, text = "Log Out", bg = "red", font = ("Helvetica", 10, "bold")).place(x = 430, y = 340)

    def genre_action(self):
        global movieCombo
        action = ["I Am Legend", "Lucy", "World War Z", "IP Man", "Inception", "Deadpool"]

        self.movieCombo = tkinter.ttk.Combobox(home, width=15, values=list(action), state="readonly")
        self.movieCombo.set("SELECT MOVIE")
        self.buttonCombobox_movie = tkinter.ttk.Button(home, text = "Rent!", command = Controller.rented_movie)
        self.movieCombo.place(x = 250, y = 100)
        self.buttonCombobox_movie.place(x = 390, y = 98)

        movieCombo = self.movieCombo

    def genre_animation(self):
        global movieCombo
        animation = ["Coco", "Frozen 2", "Toy Story 3", "Moana", "Zootopia", "Finding Dory"]

        self.movieCombo = tkinter.ttk.Combobox(home, width=15, values=list(animation), state="readonly")
        self.movieCombo.set("SELECT MOVIE")
        self.buttonCombobox_movie = tkinter.ttk.Button(home, text = "Rent!", command = Controller.rented_movie)
        self.movieCombo.place(x = 250, y = 100)
        self.buttonCombobox_movie.place(x = 390, y = 98)

        movieCombo = self.movieCombo

    def genre_horror(self):
        global movieCombo
        horror = ["Pengabdi Setan", "Hereditary", "A Quiet Place", "The Grudge", "Us", "Midsommar"]

        self.movieCombo = tkinter.ttk.Combobox(home, width=15, values=list(horror), state="readonly")
        self.movieCombo.set("SELECT MOVIE")
        self.buttonCombobox_movie = tkinter.ttk.Button(home, text = "Rent!", command = Controller.rented_movie)
        self.movieCombo.place(x = 250, y = 100)
        self.buttonCombobox_movie.place(x = 390, y = 98)

        movieCombo = self.movieCombo

    def genre_comedy(self):
        global movieCombo
        comedy = ["The Hangover", "Spy", "We're The Millers", "22 Jumpstreet", "Cek Toko Sebelah", "Orang Kaya Baru"]

        self.movieCombo = tkinter.ttk.Combobox(home, width=15, values=list(comedy), state="readonly")
        self.movieCombo.set("SELECT MOVIE")
        self.buttonCombobox_movie = tkinter.ttk.Button(home, text = "Rent!", command = Controller.rented_movie)
        self.movieCombo.place(x = 250, y = 100)
        self.buttonCombobox_movie.place(x = 390, y = 98)

        movieCombo = self.movieCombo

    
if __name__ == '__main__':
    start()
