import os
import datetime

def run_command(command):
    return os.system(command)

run_command("systeminfo")
run_command("date")