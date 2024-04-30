import os
from cryptography.fernet import Fernet
from pathlib import Path
from colorama import Fore
from getpass import getpass
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize global variables
log_data = []
dir_path = Path.cwd()
essentials_dir = "essentials"
key_file = "e_key.key"
log_file = "log.txt"
dev_logs_file = "dev_logs.txt"
email_address = "srijanbandaru@gmail.com"

def log(message):
    # Log messages with timestamps
    log_data.append(f"{datetime.now()} - {message}")
    print(Fore.WHITE + f"[LOG] {message}")

def create_encryption_key(key_file):
    # Generate and save a new encryption key
    key = Fernet.generate_key()
    with open(os.path.join(essentials_dir, key_file), "wb") as key_file:
        key_file.write(key)
    log("New encryption key generated and saved")

def encrypt_file(file_path, key):
    # Encrypt a single file
    try:
        with open(file_path, "rb") as file:
            content = file.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(file_path, "wb") as file:
            file.write(encrypted_content)
        log(f"File encrypted: {file_path}")
    except Exception as e:
        log(f"Error encrypting file {file_path}: {e}")

def encrypt_directory(directory_path, key):
    # Encrypt all files in a directory recursively
    try:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                encrypt_file(file_path, key)
    except Exception as e:
        log(f"Error encrypting directory {directory_path}: {e}")

def run_debugging_sequence():
    # Run a debugging sequence by encrypting a temporary file
    try:
        temp_file_path = "debug_temp.txt"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(b"This is a temporary file for debugging purposes.")
        log(f"Temporary file created: {temp_file_path}")

        # Encrypt the temporary file
        key = load_encryption_key(key_file)
        encrypt_file(temp_file_path, key)

        # Cleanup: delete the temporary file
        os.remove(temp_file_path)
        log(f"Temporary file deleted: {temp_file_path}")

    except Exception as e:
        log(f"Error running debugging sequence: {e}")

def load_encryption_key(key_file):
    # Load encryption key from file
    key_path = os.path.join(essentials_dir, key_file)
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    return key

def update_log_file(log_file):
    # Update log file with latest log messages
    log_path = os.path.join(essentials_dir, log_file)
    with open(log_path, "a") as log_file:
        for message in log_data:
            log_file.write(f"{message}\n")
    log("Log file updated")

def refresh_files():
    print(Fore.YELLOW + "[!] Refreshing files in the current folder...")
    dir_file()

def open_folder(folder_name):
    print(Fore.YELLOW + f"[!] Opening folder: {folder_name}")
    chdr(folder_name)

def go_back():
    print(Fore.YELLOW + "[!] Going back to the previous folder...")
    pr_temp = True
    chdr()
    pr_temp = False

def update_dev_logs(message):
    # Update dev logs with the latest activities
    dev_logs_path = os.path.join(essentials_dir, dev_logs_file)
    with open(dev_logs_path, "a") as dev_logs:
        dev_logs.write(f"{message}\n")
    log("Dev logs updated")

def send_email(subject, message):
    # Send an email with the provided subject and message
    try:
        email_password = 'icix fmln zbpr xfsp'
        email_address = "srijanbandaru@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, email_address, text)
        server.quit()
        log("Email sent successfully")
    except Exception as e:
        log(f"Error sending email: {e}")

def encrypt_selected_directory():
    # Encrypt a selected directory
    try:
        dir_name = input("Enter the directory name to encrypt: ")
        directory_path = os.path.join(dir_path, dir_name)
        if os.path.exists(directory_path):
            key = load_encryption_key(key_file)
            encrypt_directory(directory_path, key)
            log(f"Directory '{dir_name}' encrypted successfully")
        else:
            log(f"Directory '{dir_name}' not found")
    except Exception as e:
        log(f"Error encrypting directory: {e}")

def main():
    try:
        # Create essentials directory if it doesn't exist
        os.makedirs(essentials_dir, exist_ok=True)

        # Load or create encryption key
        key_path = os.path.join(essentials_dir, key_file)
        if not os.path.exists(key_path):
            create_encryption_key(key_file)
        key = load_encryption_key(key_file)

        # Request username and password
        username = input("Enter username: ")
        password = getpass("Enter password: ")

        # Perform authentication
        if username == "root" and password == "root":
            print(Fore.GREEN + "Authentication successful!")
            log("User authenticated successfully")

            # Display elevated status options
            print(Fore.YELLOW + "Elevated status options:")
            print(Fore.YELLOW + "1. Run debugging sequence")
            print(Fore.YELLOW + "2. Send encryption key for dev logs via email")
            option = input("Enter option: ")

            # Perform selected operation
            if option == "1":
                run_debugging_sequence()
            elif option == "2":
                dev_logs_key = load_encryption_key(key_file)
                send_email("Dev Logs Encryption Key", dev_logs_key.decode())
                log("Encryption key for dev logs sent via email")
            else:
                log(f"Invalid option: {option}")

        else:
            print(Fore.RED + "Authentication failed! Please try again.")
            log("Authentication failed")

        # Continue with normal code execution
        if option != "1":  # Skip if debugging sequence was chosen
            # Perform selected operation
            print(Fore.WHITE + "\t \t \t E.N.C.R.Y.P.T.E.R")
            print(Fore.WHITE + "-------------------------------------------------------------------------")
            print(Fore.YELLOW + "Choose an option:")
            print(Fore.YELLOW + "1. Encrypt all files in the current directory")
            print(Fore.YELLOW + "2. Encrypt all files in the current directory and subdirectories")
            print(Fore.YELLOW + "3. Encrypt a specific file")
            print(Fore.YELLOW + "4. Encrypt a selected directory")
            option = input("Enter option: ")

            if option == "1":
                encrypt_directory(dir_path, key)
            elif option == "2":
                encrypt_directory(dir_path, key)
            elif option == "3":
                file_name = input("Enter file name: ")
                file_path = os.path.join(dir_path, file_name)
                if os.path.exists(file_path):
                    encrypt_file(file_path, key)
                else:
                    log(f"File not found: {file_path}")
            elif option == "3":
                encrypt_selected_directory()
            elif option == "5":
                main()  # Allow user to go back to the main menu
            else:
                log(f"Invalid option: {option}")

        # Update log file and dev logs
        update_log_file(log_file)
        update_dev_logs("\n".join(log_data))

        # Encrypt and send dev logs via email
        dev_logs_key = load_encryption_key(key_file)
        encrypt_file(os.path.join(essentials_dir, dev_logs_file), dev_logs_key)
        send_email("Dev Logs", "Please find attached the encrypted dev logs.")

    except KeyboardInterrupt:
        log("Operation cancelled by user")
    except Exception as e:
        log(f"Error: {e}")

if __name__ == "__main__":
    main()
