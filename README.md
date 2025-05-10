# Logging_Utility

## 📜 Logging for Monitoring Panel

Logging function designed for the system's dashboard. It provides collection, storage, and management of logs of various types of events occurring in the system, such as user authorization, system events, console messages, and user actions. Logging is performed in specially organized files, which allows you to effectively monitor and analyze the operation of the system. Backup of logs is also provided, which guarantees the safety of data and allows you to regularly update log files to prevent them from overflowing.

The logging system consists of several parts:

- Creating log directories is used to organize the structure of log file storage.

- Recording events in logs — using a universal function to add records to various files.

- Log backup is used to create backups and update old logs on a regular basis.

To organize logging and backup in the project, a set of functions and variables has been developed that are responsible for creating and storing log files, as well as for regularly updating and backing them up.

### 📂 1. Creating log directories

To ensure normal operation with logs, several directories are created. The main directory for logs is logs. Subdirectories are created inside this directory to store backups (backup_logs) and data about the time of the last backup (dates). If the specified directories do not exist yet, they are created using the os.makedirs function.

### 🗂️ 2. Structure of log files

Logs are divided into categories, and a separate log file is created for each category. These files store information about various events in the system.:

- console_logs.txt — for entries related to console messages.

- login_logs.txt — for events related to authorization processes.

- server_logs.txt — for server operation and various system events.

- users_logs.txt — to record user actions, such as inputs or outputs.

Each of these log files is added to the LOG_FILES dictionary, which facilitates further work with them in the code.

### 📝 3. Universal logging function

The log_event function is used to write events to log files. It accepts two parameters: the path to the log file and the entry to add. Each log entry includes a timestamp and a description of the event. Logging is implemented in such a way that records are added to the end of the file without overwriting existing data.

### 🔏 4. Functions for writing to various logs

Based on the universal logging function, specialized functions for writing to different files were implemented.:

- log_to_login — for recording events related to user authorization.

- log_to_work — for recording system and server events.

- log_to_console — for entries related to console messages.

- log_to_users — for recording user actions.

These functions provide convenient addition of logs to the corresponding files, which helps to organize information and simplify further work with logs.

### 💾 5. Backup logs

Backup is provided to prevent data loss and to keep logs up-to-date. To do this, the check_and_backup_logs function is implemented, which checks whether 30 days have passed since the last backup, and if so, creates backups of all logs. The logs are moved to the backup_logs folder, and then new empty files are created for future use.

A file is used to track the time of the last backup. backup_date.txt . It stores the date and time of the last backup, which allows you to control the frequency of backups.

### 🕒 6. Updating the date of the last backup

After the backup has been performed, the date in the file is backup_date.txt It is updated so that the next time you start, you can compare the current date with the last one and determine whether you need to backup again.

This process allows you to keep up-to-date logs in the system, avoid file overflow, and ensure data security in the event of a system failure.

[The functionality described above is implemented in the logging_panel.py file](logging_panel.py)

This file is responsible for handling all logging and backup processes in the project. It ensures proper storage, management, and backup of log files, providing a reliable method for tracking system events, user actions, and authorization processes. The backup mechanism ensures that logs are periodically saved, preventing data loss and keeping the system’s logs organized and manageable.
