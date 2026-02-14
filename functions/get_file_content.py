import os

def get_file_content(working_directory, file_path):
    
    try:
        cd = os.path
        MAX_CHARS = 10000


        working_dir_abs = cd.abspath(working_directory)
        target_file = cd.normpath(cd.join(working_dir_abs, file_path))
    except (NotADirectoryError) as e:
        print(f"Error reading directory: {e}")
        return f"Error reading directory: {e}"
    print(target_file)
    if not cd.isfile(target_file):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return f'Error: File not found or is not a regular file: "{file_path}"'

    valid_target_file = cd.commonpath([working_dir_abs, target_file]) == working_dir_abs
    
    if not valid_target_file:
        print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(MAX_CHARS + 1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        print(content)


        return content
    
    except (FileNotFoundError, PermissionError, NotADirectoryError) as e:
        print(f"Error reading file: {e}")
        return f"Error reading file: {e}"

