import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    # validation start -----------------------------------------------------------
    try:
        cd = os.path

        working_dir_abs = cd.abspath(working_directory)

        target_file = cd.normpath(cd.join(working_dir_abs, file_path))
        
        
    except (NotADirectoryError) as e:
        print(f"Error reading directory: {e}")
        return f"Error reading directory: {e}"
    
    if not cd.isfile(target_file):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return f'Error: File not found or is not a regular file: "{file_path}"'
 
    valid_target_file = cd.commonpath([working_dir_abs, target_file]) == working_dir_abs
    
    if not valid_target_file:
        print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    str_file_path = []
    for char in file_path:
        str_file_path.append(char)
    
    extension_py = ''.join(str_file_path[-3:])
    if ".py" != extension_py:
        
        return f'Error: "{file_path}" is not a Python file'

    # validation end -------------------------------------------------------------

    # creating list of commands inputed
    command = ["python", target_file]

    # checking for any argument parsed
    if args != None:
        command.extend(args)

    # run subprocess and storing CompletedProccess to a variable
    try:
        completed_process_output = subprocess.run(command, stdout=True, stderr=True, timeout=30, text=True)
        
        if completed_process_output.returncode != 0:
            return f"{completed_process_output}\nProcess exited with code X"
        elif completed_process_output.stdout == '' and completed_process_output.stderr == '':
            return f"{completed_process_output}\nNo output produced"
        else:
            return f""
    except Exception as e:
        return f"Error: executing Python file: {e}"

    print(completed_process_output.returncode)

run_python_file("calculator", "main.py")

run_python_file("calculator", "main.py", ["3 + 5"])

run_python_file("calculator", "tests.py")

run_python_file("calculator", "../main.py")

run_python_file("calculator", "nonexistent.py")

run_python_file("calculator", "lorem.txt")