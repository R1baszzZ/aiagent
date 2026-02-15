import os

def write_file(working_directory, file_path, content):
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
    # validation end -------------------------------------------------------------


    parent_dir = os.path.dirname(target_file)

    os.makedirs(parent_dir, exist_ok=True)

    try:    
        with open(target_file, "w") as f:
            content = f.write(content)
            print(f'Successfully wrote to "{file_path}" ({content} characters written)')
            return content
    except (FileNotFoundError, PermissionError, NotADirectoryError) as e:
        print(f"Error writting file: {e}")
        return f"Error writting file: {e}"
    
    
