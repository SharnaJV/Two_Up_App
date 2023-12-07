import mysql.connector

# global message;
# global username
# global password

def db_connect():
    db_config = {
        "host": "127.0.0.1",
        "user": "root",
        "password" : "Power2thePeopleWho8",
        "database" : "twoupapp"
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

    connection = db_connect()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM userlogins WHERE username_login = %s AND password_login = %s"
        cursor.execute(query,(username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            print("Login Success")
            return True        
        else:
            print("Wrong username and/or password!")
            return False

def reg_user(username, password, email, first_name, last_name, employee_id):
    connection = db_connect()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO userlogins (username_login, password_login, email_login, first_name, last_name, employee_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (username, password, email, first_name, last_name, employee_id)
        
        try:
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    else:
        return False