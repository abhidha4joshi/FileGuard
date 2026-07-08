import os
import time

from hashing import calculate_hash
from database import load_hashes, save_hashes
from alerts import log_alert, show_history


def scan_folder(folder_path):
    start_time = time.time()

    old_hashes = load_hashes()
    new_hashes = {}

    total_files = 0
    new_files = 0
    modified_files = 0
    deleted_files = 0
    unchanged_files = 0

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)
            total_files += 1

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            new_hashes[file_path] = file_hash

            if file_path not in old_hashes:
                log_alert(f"[NEW FILE] {file_path}")
                new_files += 1

            elif old_hashes[file_path] != file_hash:
                log_alert(f"[MODIFIED] {file_path}")
                modified_files += 1

            else:
                log_alert(f"[NO CHANGE] {file_path}")
                unchanged_files += 1

    for file_path in old_hashes:
        if file_path not in new_hashes:
            log_alert(f"[DELETED] {file_path}")
            deleted_files += 1

    save_hashes(new_hashes)

    end_time = time.time()

    print("\n========================================")
    print("            Scan Summary")
    print("========================================")
    print(f"Total Files Scanned : {total_files}")
    print(f"New Files           : {new_files}")
    print(f"Modified Files      : {modified_files}")
    print(f"Deleted Files       : {deleted_files}")
    print(f"Unchanged Files     : {unchanged_files}")
    print(f"Scan Time           : {end_time-start_time:.2f} seconds")
    print("========================================")


while True:

    print("\n========================================")
    print("          FileGuard v1.0")
    print("========================================")
    print("1. Scan Folder")
    print("2. View Scan History")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        folder = input("Enter folder path: ").strip()
        scan_folder(folder)

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("Thank you for using FileGuard!")
        break

    else:
        print("Invalid choice. Please try again.")