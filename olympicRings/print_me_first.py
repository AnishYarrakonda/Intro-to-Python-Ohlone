from datetime import datetime

def print_me_first(lab_info, program_name):
    """
    Prints initial program and lab information including current time.

    Args:
        lab_info (str): Information about the lab or assignment (e.g., "CNET-142 Lab 1 Print Me First - Anish Yarrakonda").
        program_name (str): The name of the Python file (e.g., "print_me_first.py").
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = ""
    msg += f"\nName         : {lab_info}"
    msg += f"\nProgram      : {program_name}"
    msg += f"\nCurrent Time : {current_time}\n"

    return msg

if __name__ == '__main__':
    print(print_me_first(
        lab_info="CNET-142 Lab 1 Print Me First - Anish Yarrakonda",
        program_name="print_me_first"))