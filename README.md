# Logging_Utility

## 📋 Table of Contents

### 📜 Logging for Monitoring Panel
1. [📂 Directory Structure](#-1-creating-log-directories)
2. [🗂️ Log File Structure](#-2-structure-of-log-files)
3. [📝 Universal Logging Function](#-3-universal-logging-function)
4. [🔏 Specialized Logging Functions](#-4-functions-for-writing-to-various-logs)
5. [💾 Log Backup System](#-5-backup-logs)
6. [🕒 Backup Date Tracking](#-6-updating-the-date-of-the-last-backup)
7. [Implementation File](#implementation-file)

### 📜 Logging for WebInterface_MySQL
1. [📁 Directory Organization](#-1-log-directories)
2. [📝 Log File Types](#-2-structure-of-log-files)
3. [💾 Backup Mechanism](#-3-backup-logs)
4. [⏳ Backup Date Management](#-4-updating-the-date-of-the-last-backup)
5. [Database Integration](#database-integration)

### 📌 Conclusion

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

## 📜 Logging for WebInterface_MySQL

Logging is an important part of the monitoring system, as it allows you to track all events and actions taking place in the system. In this part of the system, the necessary directories and files are created to store logs, and a log backup mechanism is implemented, which ensures data security and prevents data loss.

### 📁 1. Log directories

The system creates several key directories for convenient log storage.:

- LOG_DIR: This is the main directory for storing all logs, where all files related to logging will be located.

- DATES_DIR: A special directory designed to store information about the date of the last backup.

- BACKUP_DIR: A directory for storing backup copies of logs.

Creating these directories ensures that all data is properly organized and available for future reference.

### 📝 2. Structure of log files

Logging is organized in such a way that each type of event is recorded in a separate log file. The following files are used for this:

- USERS_LOG: A log that records the actions of system users (for example, logging in, logging out, and making changes).

- CONSOLE_LOG: A console message log containing system and administrative notifications.

- WORK_LOG: The server's operation log, which records general events and errors related to the functioning of the system.

- LOGIN_LOG: The log of authorizations, which contains information about login attempts, successful and unsuccessful.

This structure allows you to quickly find the necessary information and facilitates the analysis of events in various aspects of the system.

### 💾 3. Backup logs

An important part of the system is log backup, which helps to avoid data loss in case of failures or other unforeseen situations. For this purpose, a function is provided that checks whether a certain amount of time has passed (for example, 30 days) since the last backup. If the deadline has passed, the system automatically creates backups of all logs, moving them to a special folder for backups and clearing the source files. This ensures that the old data will not interfere with the new logging and that all data will be archived.

### ⏳ 4. Updating the date of the last backup

After performing the backup, the system updates the date of the last backup in a special file. This allows you to accurately track when the last backup was made and avoid unnecessary repetition. This mechanism helps to control backup processes and keep data up-to-date.

[The logging code is located in a separate file. logging_MySQL.py](logging_MySQL.py)

This is responsible for integrating the system with the MySQL database. This file implements the logic for sending event data, such as user actions or system errors, directly to the database. This allows logs to be stored and processed centrally, improving information availability and providing a convenient way for further analysis and monitoring.

## 📌 Conclusion

The logging system described in this project is an effective solution for monitoring and managing events in the system. It provides centralized storage, processing, and backup of logs, which contributes to the reliability, security, and convenience of data analysis.

The creation of specialized directories for storing logs and backups allows you to organize the data structure and ensure their safety. Logging is divided into several types of files, which helps to track various types of events, such as user actions, system events, and errors. This simplifies the search and analysis of data, as well as increases the transparency of the system.

In addition, integration with the MySQL database, implemented in a separate file logging_MySQL.py , allows centralized storage of all logs, improving the availability of information for further analysis and monitoring. This approach to logging makes it easy to scale the system and improves the processing of large amounts of data.

The log backup process is regularly updated to help prevent data loss and keep information up-to-date. Updating the date of the last backup in the file allows you to control the frequency of backups and keep logs up to date.

Thus, this logging and backup system not only ensures reliable data storage, but also guarantees their security, improving the capabilities for monitoring and analyzing the system.
