from datetime import datetime

def print_me_first(lab_info, program_name):
    """
    Prints initial program and lab information including current time.

    Args:
        lab_info (str): Information about the lab or assignment (e.g., "CNET-142 Lab 1 Print Me First - Anish Yarrakonda").
        program_name (str): The name of the Python file (e.g., "print_me_first.py").
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nName         : {lab_info}")
    print(f"Program      : {program_name}")
    print(f"Current Time : {current_time}\n")