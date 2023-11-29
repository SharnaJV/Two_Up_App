from tkinter import *
#defining login function
def login():
#getting form data
    uname=username.get()
    pwd=password.get()
#applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
        if uname=="abcd@gmail.com" and pwd=="abc123":
            message.set("Login success")
        else:
            message.set("Wrong username or password!!!")
#defining loginform function

def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Two Up")
    login_screen.iconbitmap("ANZAC_logo.ico")
    #setting height and width of screen
    login_screen.geometry("600x450")
    login_screen.configure(bg="#EFE0B9")
    #declaring variable
    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below",
    bg="#123907",fg="#EFE0B9").pack()
    #Username Label
    Label(login_screen, text="Username * ", bg="#EFE0B9").place(x=210,y=100)
    #Username textbox
    Entry(login_screen, textvariable=username, bg="#E4B04A").place(x=290,y=100)
    #Password Label
    Label(login_screen, text="Password * ", bg="#EFE0B9").place(x=210,y=150)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*", bg="#E4B04A").place(x=290,y=150)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message, bg="#EFE0B9", fg="#EFE0B9").place(x=300,y=180)
    #Login button
    Button(login_screen, text="Login", width=10, height=1,
    bg="#B7521E", fg="#EFE0B9", command=login).place(x=220,y=200)

    Button(login_screen, text="Register", width=10, height=1,
    bg="#B7521E", fg="#EFE0B9", command=login).place(x=315,y=200)
    login_screen.mainloop()
    #calling function Loginform
Loginform()