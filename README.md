# FileGuard

## Introduction

FileGuard is a simple File Integrity Monitoring Tool developed using Python. It monitors files inside a selected folder by generating SHA-256 hashes and compares them with previously stored hashes to identify any changes.

This project was developed as part of my Cyber Security Internship to understand file integrity verification and basic security monitoring concepts.

## Features

* Generate SHA-256 hash for files
* Detect newly added files
* Detect modified files
* Detect deleted files
* Maintain scan history
* Display scan summary
* Simple menu-driven interface

## Technologies Used

* Python
* hashlib
* json
* os
* datetime
* time

## Project Structure

```text
FileGuard/
│
├── database/
│   └── hashes.json
│
├── logs/
│   └── history.log
│
├── hashing.py
├── database.py
├── alerts.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python main.py
```

4. Select **Scan Folder** from the menu.
5. Enter the folder path that you want to monitor.

## Sample Output

```
========================================
          FileGuard v1.0
========================================

1. Scan Folder
2. View Scan History
3. Exit

Enter your choice: 1

[NEW FILE] test.txt

========================================
            Scan Summary
========================================
Total Files Scanned : 3
New Files           : 1
Modified Files      : 0
Deleted Files       : 0
Unchanged Files     : 2
========================================
```

## Future Scope

* Real-time monitoring
* Email notifications
* PDF report generation
* Graphical User Interface (GUI)

## Author

Developed by **Abhidha Joshi** as part of a Cyber Security Internship.
