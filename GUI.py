from tkinter import *
from Authentication import *

def login_validation():
    uname_input = username.get()
    pass_input = password.get()
    login(uname_input, pass_input)
    
#Creating the user authentication screen
def login_form():
    global login_screen
    login_screen = Tk()
    login_screen.title("Two Up")
    login_screen.iconbitmap("ANZAC_logo.ico")
    login_screen.geometry("800x450")
    login_screen.configure(bg="#EFE0B9")

    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    
#Intro message
    Label(login_screen,width="300", text="For returning users enter login details then click \"Login\", new users click \"Register\"",
    bg="#123907",fg="#EFE0B9").pack()
    
#Username elements
    Label(login_screen, text="Username * ", bg="#EFE0B9").place(x=310,y=100)
    Entry(login_screen, textvariable=username, bg="#E4B04A").place(x=390,y=100)
    
#Password elements
    Label(login_screen, text="Password * ", bg="#EFE0B9").place(x=310,y=150)
    Entry(login_screen, textvariable=password ,show="*", bg="#E4B04A").place(x=390,y=150)
    
    Label(login_screen, text="",textvariable=message, bg="#EFE0B9", fg="#EFE0B9").place(x=400,y=180)
    
#Login Button
    Button(login_screen, text="Login", width=10, height=1,
    bg="#B7521E", fg="#EFE0B9", command=login).place(x=320,y=200)

#Register Button
    Button(login_screen, text="Register", width=10, height=1,
    bg="#B7521E", fg="#EFE0B9", command=login).place(x=415,y=200)

    login_screen.mainloop()
    
def font_options(option_pick):
    print(f"Selected option: {option_pick}")

#Creating the gameplay screen
def game_screen():

#Switching from login screen to game screen
    global login_screen
    login_screen.destroy()
    two_up_screen = Tk()

#Setup of game screen window is same as login window
    two_up_screen.title("Two Up")
    two_up_screen.iconbitmap("ANZAC_logo.ico")
    two_up_screen.geometry("800x450")
    two_up_screen.configure(bg="#EFE0B9")

#Drop-down menu for changing font sizes
    label_font = Label(two_up_screen, text="Font Size", bg="#EFE0B9")
    label_font.pack()
    font_size = ["Small", "Medium", "Large"]
    menu_01 = StringVar(two_up_screen)
    menu_01.set(font_size[0])
    font_menu = OptionMenu(two_up_screen, menu_01, *font_size, command= lambda x: font_options(menu_01.get()))
    font_menu.pack()
    
    two_up_screen.mainloop()

