import os

def load_db_auth():
    # Specify the path to your ".db_auth" file
    auth_file_path = ".db_auth"

    # Check if the file exists
    if not os.path.exists(auth_file_path):
        print("Error: The .db_auth file does not exist.")
        return None, None

    # Read the contents of the file
    with open(auth_file_path, 'r') as file:
        lines = file.readlines()

    # Extract username and password
    username = None
    password = None
    for line in lines:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key = parts[0].strip().lower()
            value = parts[1].strip()
            if key == 'db_user':
                username = value
            elif key == 'db_pass':
                password = value

    return username, password

"""
# Example usage
db_username, db_password = load_db_auth()

if db_username and db_password:
    print("Username:", db_username)
    print("Password:", db_password)
    # Now you can use db_username and db_password in your script
else:
    print("Failed to load database authentication information.")

"""