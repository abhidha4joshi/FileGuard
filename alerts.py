from datetime import datetime

LOG_FILE = "logs/history.log"


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    print(log_message)

    with open(LOG_FILE, "a") as file:
        file.write(log_message + "\n")


def show_history():
    try:
        with open(LOG_FILE, "r") as file:
            print("\n========== Scan History ==========\n")
            print(file.read())
    except FileNotFoundError:
        print("No scan history found.")