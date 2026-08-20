import sys

passwords_db = {}
users_db = {}

def add():
    print("Add password page...")


def delete():
    print("Delete password page...")


def show_passwords():
    print("Showing passwords...")

def login():
    while True:
        try:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            if not username or not password:
                raise ValueError("Username and password cannot be empty.")

            print(f"Hello, {username}!")
            return

        except ValueError as error:
            print(f"Error: {error}")

def register():
    print("Registration page...")

def authentication_menu():
    while True:
        print("\nWelcome to Embra!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        try:
            choice = input("Please select an option: ")

            if choice == "1":
                login()
                return

            elif choice == "2":
                register()
                return

            elif choice == "3":
                print("Exiting...")
                sys.exit()

            else:
                raise ValueError("Invalid option.")

        except ValueError as error:
            print(f"Error: {error}")

def password_menu():
    while True:
        print("\nEmbra Password Manager")
        print("1. Add")
        print("2. Delete")
        print("3. Show Passwords")
        print("4. Exit")

        try:
            choice = input("Please select an option: ")

            if choice == "1":
                add()

            elif choice == "2":
                delete()

            elif choice == "3":
                show_passwords()

            elif choice == "4":
                print("Exiting...")
                sys.exit()
            else:
                raise ValueError("Invalid option.")

        except ValueError as error:
            print(f"Error: {error}")

def main():
    print("Welcome to Embra!")

    try:
        authentication_menu()
        password_menu()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    except Exception as error:
        print(f"Unexpected error: {error}")

if __name__ == "__main__":
    main()