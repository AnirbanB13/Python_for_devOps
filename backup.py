import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar', source)

source = r"C:\Users\anirb\OneDrive\Desktop\Abhirup\Python_for_devOps"
destination = r"C:\Users\anirb\OneDrive\Desktop\Abhirup\Python_for_devOps\backups"

backup_files(source, destination)
