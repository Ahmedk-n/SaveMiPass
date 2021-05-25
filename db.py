import sqlite3
from generate_pass import making_pass
connection = sqlite3.connect('userData.db')
cursor = connection.cursor()
run = input(">")

def createDB():
    try:
        cursor.execute('''CREATE TABLE userData(apps text, usernames text, emails text, passwords text)''')

    except:
        pass

""" table """
"""
# Adding Data
# cursor.execute("INSERT INTO userData VALUES ('Facebook', 'RTxNINJA', 'rtexamplemail@gmail.com', '1234zx')")
# connection.commit()
"""
"""table """

# adding new password
def add_new():
    x = input("App name: ") 
    y =input ("User-name :")
    z = input("Enter the e-mail : ")
    print ("This is your password : " )
    making_pass() 
    print("Paste the password please.")
    l = input("Enter the password u want to save : ")

    cursor.execute(f"INSERT INTO userData VALUES ('{x}', '{y}', '{z}', '{l}')")
    connection.commit()
    print("Added succesfully !")

# retrieve a password                        
def get_password():
    website_search_input = input ("Website name\n :")
    appSelect = cursor.execute("SELECT apps FROM userData")
    passwordsColumn = cursor.execute(f"SELECT passwords FROM userData WHERE apps = '{website_search_input}' ")
    print("The password is : ")
    for row in passwordsColumn:
        retrieved = print(row[0])
    
# getting username connected to an app
def get_userName():
    UserNameSearchInput = input("Website name \n:")
    Usernamescolumn = cursor.execute(f"SELECT usernames FROM userData WHERE apps = '{UserNameSearchInput}'")
    for row in Usernamescolumn :
        print(row[0])

# getting e-mails connected to a website
def get_mail():
    MailSearchInput = input("Website name\n:")
    Mailcolumn = cursor.execute(f"SELECT usernames FROM userData WHERE apps = '{MailSearchInput}'")
    for row in Mailcolumn :
        print(row[0])

# get all websites connected to mail 
def get_websiteMail():
    EmailSearchInput = input("E-mail \n:")
    WebsitesEmailcolumn = cursor.execute(f"SELECT apps FROM userData WHERE emails = '{EmailSearchInput}'")
    for row in WebsitesEmailcolumn :
        print(row[0])

# deleting records 
def delete_item ():
    print("Note:This is permanent!")
    deleteName = input("Website name : ")
    connection.execute(f"""DELETE FROM userData WHERE apps = '{deleteName}' """)
    connection.commit()
    print('Deleted succesfully ')