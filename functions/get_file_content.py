def get_file_content(working_directory, file_path):
    cd = os.path
    
    working_dir_abs = cd.abspath(working_directory)
    target_file = cd.normpath(cd.join(working_dir_abs, directory))

    if not cd.isfile(target_file):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return f'Error: File not found or is not a regular file: "{file_path}"'

    valid_target_fie = cd.commonpath([working_dir_abs, target_file]) == working_dir_abs
    
    if not valid_target_file:
        print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'



