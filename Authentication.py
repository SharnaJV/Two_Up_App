import mysql.connector

global message;
global username
global password

def db_connect():
    db_config = {
        "host": "127.0.0.1",
        "user": "root@localhost",
        "password" : "Power2thePeopleWho8",
        "database" : "Two Up App"
    }
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
#Defining login function
def login(username, password):
    uname=username.get()
    pwd=password.get()

    if uname=='' or pwd=='':
        message.set("Username and/or password has not been entered!")
    else:
        connection = db_connect()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM twoupapp WHERE username_login = %s AND password_login = %s"
            cursor.execute(query,(uname, pwd))
            user = cursor.fetchone()

            if user and user[1] == pwd:
                message.set("Login Success")
                print("Login Success")
                game_screen()           
            else:
                message.set("Wrong username and/or password!")

            cursor.close()
            connection.close()
        else:
            message.set("Failed to connect to database")
