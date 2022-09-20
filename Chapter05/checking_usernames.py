current_users = ['admin', 'tom', 'Zach', 'oliver', 'david']
new_users = ['Tom', 'oliver', 'lily', 'lucy', 'bell']
current_users_lower = [username.lower() for username in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print("You need to enter a new username")
    else:
        print("The username is available.")