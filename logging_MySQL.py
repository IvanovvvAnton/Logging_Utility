LOG_DIR = "logs"
DATES_DIR = os.path.join(LOG_DIR, "dates")
BACKUP_DIR = os.path.join(LOG_DIR, "backup_logs")

USERS_LOG = os.path.join(LOG_DIR, "users_logs.txt")
CONSOLE_LOG = os.path.join(LOG_DIR, "console_logs.txt")
WORK_LOG = os.path.join(LOG_DIR, "server_logs.txt")
LOGIN_LOG = os.path.join(LOG_DIR, "login_logs.txt")
BACKUP_DATE_FILE = os.path.join(DATES_DIR, "backup_date.txt")

LOG_FILES = {
    "users_logs": USERS_LOG,
    "console_logs": CONSOLE_LOG,
    "server_logs": WORK_LOG,
    "login_logs": LOGIN_LOG
}

def create_log_dirs():
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(DATES_DIR, exist_ok=True)

create_log_dirs()

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
            os.makedirs(BACKUP_DIR, exist_ok=True)  

            for log_name, log_path in LOG_FILES.items():
                if os.path.exists(log_path):  
                    backup_filename = os.path.join(BACKUP_DIR, f"{log_name}_{current_time.strftime('%d-%m-%Y_%H-%M-%S')}.txt")
                    os.rename(log_path, backup_filename)  
                    open(log_path, "w").close()  
                    print(f"Создан резервный лог: {backup_filename}")

           
            with open(BACKUP_DATE_FILE, "w", encoding="utf-8") as backup_file:
                backup_file.write(current_time.strftime("%d-%m-%Y %H:%M:%S"))

        else:
            print("Бэкап не требуется, 30 дней еще не прошло.")


check_and_backup_logs()
