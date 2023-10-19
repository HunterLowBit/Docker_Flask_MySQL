import os

if not os.path.isfile("funcionarios.db"):
    os.system("python db.py")

import shutil
import datetime

if os.path.isfile("funcionarios.db"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = os.path.join("backup", f"funcionarios_{timestamp}.db")
    shutil.copyfile("funcionarios.db", backup_filename)
