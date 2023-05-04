import os
import datetime
from cryptography.fernet import Fernet

# Check if the key file exists, and create one if it doesn't
def create_key():
    key_filename = "key.key"
    if not os.path.exists(key_filename):
        key = Fernet.generate_key()
        with open(key_filename, "wb") as f:
            f.write(key)
    else:
        with open(key_filename, "rb") as f:
            key = f.read()
    return Fernet(key)

def get_today_date():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")

# Create a directory for the diary files if it does not exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def check_entry_exists(today, directory):
    filename = os.path.join(directory, f"{today}.txt")
    if os.path.exists(filename):
        return True
    else:
        return False

# Prompt the user for their diary entry
def get_entry():
    return input("What did you do today?\n")

# Encrypt the entry
def encrypt_entry(fernet, entry):
    return fernet.encrypt(entry.encode())

# Write the encrypted entry to a file with the current date as the filename
def save_entry(today, directory, encrypted_entry):
    filename = os.path.join(directory, f"{today}.txt")
    with open(filename, "wb") as f:
        f.write(encrypted_entry)
    print(f"Your encrypted diary entry for {today} has been saved.")

# Read diary entries
def read_entry(fernet, directory):
    date_str = input("Enter the date of the diary entry you want to read (YYYY-MM-DD): ")
    filename = os.path.join(directory, f"{date_str}.txt")
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            encrypted_entry = f.read()
        entry = fernet.decrypt(encrypted_entry).decode()
        print(f"Diary entry for {date_str}:")
        print(entry)
    else:
        print(f"No diary entry found for {date_str}.")

def main():
    # Initialize Fernet object
    fernet = create_key()

    # Create diary directory if it doesn't exist
    create_directory("diary")

    while True:
        choice = input("Enter '1' to create a new diary entry, '2' to read an existing entry, or '3' to exit: ")
        if choice == '1':
            # Get today's date
            today = get_today_date()

            # Check if an entry for today already exists
            if check_entry_exists(today, "diary"):
                entry = input("You have already entered a diary entry for today. Enter 47 to override or press any other key to continue.\n")
                if entry != "47":
                    continue

            # Prompt the user for their diary entry
            entry = f"--- {today} ---\n\n" + get_entry() + "\n\n\nDear diary, what a day it's been\nDear diary, it's been just like a dream\n---"

            # Encrypt the entry
            encrypted_entry = encrypt_entry(fernet, entry)

            # Write the encrypted entry to a file with the current date as the filename
            save_entry(today, "diary", encrypted_entry)

        elif choice == '2':
            read_entry(fernet, "diary")

        elif choice == '3':
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
