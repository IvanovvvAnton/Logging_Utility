LOG_DIR = "logs"
DATES_DIR = os.path.join(LOG_DIR, "dates")
BACKUP_DIR = os.path.join(LOG_DIR, "backup_logs")

CONSOLE_LOG = os.path.join(LOG_DIR, "console_logs.txt")
LOGIN_FILE = os.path.join(LOG_DIR, "login_logs.txt")
WORK_LOGS = os.path.join(LOG_DIR, "server_logs.txt")
USERS_LOG = os.path.join(LOG_DIR, "users_logs.txt")
BACKUP_DATE_FILE = os.path.join(DATES_DIR, "backup_date.txt")

LOG_FILES = {
    "users_logs": USERS_LOG,
    "login_logs": LOGIN_FILE,
    "server_logs": WORK_LOGS,
    "console_logs": CONSOLE_LOG
}

def create_log_dirs():
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(DATES_DIR, exist_ok=True)

create_log_dirs()

def log_event(log_file, log_entry):
    access_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    full_log_entry = f"{access_time} | {log_entry}\n"
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(full_log_entry)

def log_to_login(event_type, details):
    log_event(LOGIN_FILE, f"Событие: {event_type} | {details}")

def log_to_work(event_type, details):
    log_event(WORK_LOGS, f"Событие: {event_type} | Детали: {details}")

def log_to_console(message):
    log_event(CONSOLE_LOG, f"Событие: Консоль | {message}")

def log_to_users(full_name, event_type):
    log_event(USERS_LOG, f"Событие: {event_type} | Пользователь: {full_name}")

def check_and_backup_logs():
    os.makedirs(BACKUP_DIR, exist_ok=True) 
    os.makedirs(os.path.dirname(BACKUP_DATE_FILE), exist_ok=True) 

    current_time = datetime.now()

    if not os.path.exists(BACKUP_DATE_FILE):
        with open(BACKUP_DATE_FILE, "w", encoding="utf-8") as f:
            f.write(current_time.strftime("%d-%m-%Y %H:%M:%S"))
        print("Файл backup_date.txt создан с текущей датой и временем.")
        return  

    last_backup_date = None
    with open(BACKUP_DATE_FILE, "r", encoding="utf-8") as f:
        last_backup_date_str = f.read().strip()
        if last_backup_date_str:
            try:
                last_backup_date = datetime.strptime(last_backup_date_str, "%d-%m-%Y %H:%M:%S")
            except ValueError:
                last_backup_date = None

    if last_backup_date and current_time >= last_backup_date + timedelta(days=30):
        for log_name, log_path in LOG_FILES.items():
            backup_filename = f"{BACKUP_DIR}/{log_name}_{current_time.strftime('%d-%m-%Y %H:%M:%S')}.txt"
            os.rename(log_path, backup_filename) 
            open(log_path, "w").close() 
            print(f"Создан резервный лог: {backup_filename}")

        with open(BACKUP_DATE_FILE, "w", encoding="utf-8") as f:
            f.write(current_time.strftime("%d-%m-%Y %H:%M:%S"))
    else:
        print("Бэкап не требуется, 30 дней еще не прошло.")

check_and_backup_logs()
