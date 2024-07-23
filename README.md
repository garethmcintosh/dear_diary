# dear_diary
This Python script allows you to create an encrypted diary entry for each day and read existing diary entries for a specific date. The diary entries are encrypted using the Fernet encryption scheme from the cryptography library. To use this script, follow the instructions below.

## Requirements
* Python 3.x
* cryptography library

## Usage
Make sure you have Python installed on your system. If not, you can download it from the official Python website (https://www.python.org/downloads/).

Install the required cryptography library using the following command:
```pip install cryptography```

Run the script using the following command:
```python encrypted_diary.py```

Follow the prompts to create new diary entries or read existing ones.

## How it works
1. When the script is executed, it checks for the existence of a key file (key.key). If the file doesn't exist, a new key is generated and saved in key.key. If the file already exists, the key is read from it.

2. The script prompts the user to create a new diary entry or read an existing one. To create a new entry, the user is asked for the content of the diary entry for the current date. If an entry for the current date already exists, the user can choose to override it.

3. The diary entry is then encrypted using the Fernet key.

4. The encrypted entry is saved to a file with the current date as the filename (e.g., 2023-07-28.txt).

5. To read an existing diary entry, the user is prompted to enter a specific date (in the format YYYY-MM-DD). The script then tries to find and decrypt the corresponding entry.

## Note
* The diary entries are saved in a directory named diary within the same directory where the script is located. If the diary directory doesn't exist, it will be created automatically.

* The key used for encryption and decryption is stored in the key.key file. Do not share or delete this file if you want to access your encrypted entries in the future. Losing the key may result in permanent data loss.

* If you forget your encryption key, there is no way to recover the data encrypted with it. Make sure to keep a backup of the key.key file or the data itself in case you need it later.

* This script is intended for personal purposes and should not be used for any sensitive or critical data storage without proper security measures and backups.
