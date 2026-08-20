# Welcome to Embra!

import sys

passwords_db = {}
users_db = {}

def add():
    print("Add page...")
    # Implementation for adding items

def delete():
    print("Delete page...")
    # Implementation for deleting items

def show_passwords():
    print("Passwords page...")
    # Implementation for showing passwords

print("Welcome to Embra!")

options = ["1. Login", "2. Register", "3. Exit"]
for option in options:
    print(option)

choice = input("Please select an option: ")

while True:
    if choice == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username and password:
            print(f"Hello, {username}!")
            break
        else:
            print("Invalid username or password. Please try again.")
    elif choice == "2":
        print("Registration page...")
        break
    elif choice == "3":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid option. Please try again.")

    choice = input("Please select an option: ")

options = ["1. Add", "2. Delete", "3. Show Passwords", "4. Exit"]
for option in options:
    print(option)

choice = input("Please select an option: ")

while True:
    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        show_passwords()
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid option. Please try again.")

    choice = input("Please select an option: ")