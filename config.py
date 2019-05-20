from pathlib import Path

EMAIL_ADDRESS = ""
PASSWORD = ""


# bot.johannessen@gmail.com
# kiqzo4-nybFek-muwjeq

def init():
    ip_file_exists = Path('email_login.txt')

    if ip_file_exists.is_file():
        f = open("email_login.txt", "r")
        global EMAIL_ADDRESS
        EMAIL_ADDRESS = f.readline()
        global PASSWORD
        PASSWORD = f.readline()
        f.close()
    else:
        print("Email not configured yet")
        f = open("email_login.txt", "w")
        f.write(input("Enter email adr: ") + "\n")
        f.write(input("Enter password: "))
        f.close()
        init()
