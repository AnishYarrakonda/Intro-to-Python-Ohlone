# returns text for each lab
# description: same as lab 1
from datetime import datetime

def print_me_first(lab_info, program_name):
    """
    Returns initial program and lab information as a string.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"Name         : {lab_info}\n"
        f"Program      : {program_name}\n"
        f"Current Time : {current_time}\n"
    )