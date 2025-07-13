import json
while True:
    new_user = input("Are you a new user? (yes/no): ").rstrip().lower()
    if new_user == "yes":
        try:
            with open("database.json", "r") as database:
                data = json.load(database)
        except FileNotFoundError:
            data = {}
            username = input("Enter your username: ").rstrip()
            password = input("Enter your password: ").rstrip()
            data[f"{username}"] = password
            with open("database.json", "w") as database:
                json.dump(data, database)
            with open(f"{username}.txt", "a") as user_file:
                user_file.write("")
        else:
            username = input("Enter your username: ").rstrip()
            password = input("Enter your password: ").rstrip()
            data[f"{username}"] = password
            with open("database.json", "w") as database:
                json.dump(data, database)
            with open(f"{username}.txt", "a") as user_file:
                user_file.write("")
        print("Thank you for registering yourself!")
    elif new_user == "no":
        try:
            with open("database.json", "r") as database:
                data = json.load(database)
        except FileNotFoundError:
            print("No users found. Please register first.")
            continue
        else:
            username = input("Enter your username: ").rstrip()
            password = input("Enter your password: ").rstrip()
            if username in data.keys() and data[username] == password:
                print(f"Welcome back, {username}!")
                with open(f"{username}.txt", "r") as user_file:
                    user_data = user_file.read()
                    print(f"Your data:\n{user_data.rstrip()}")
                    print("You can now add or modify your data.")
                    modified_data = input("Enter your data to save: ").rstrip()
                    user_data += f"{modified_data}\n"
                with open(f"{username}.txt", "a") as user_file:
                    user_file.write(str(user_data))
            else:
                print("Invalid username or password.")