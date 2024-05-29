from cryptography.fernet import Fernet

master_pwd = input("What is your master password? ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, ", password:", passw)


def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("Would you like to view an exisiting password or add a new password (View, Add), press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue
