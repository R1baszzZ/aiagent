import os

def get_files_info(working_directory, directory="."):
    cd = os.path

    working_dir_abs = cd.abspath(working_directory)
    target_dir = cd.normpath(cd.join(working_dir_abs, directory))

    if not cd.isdir(target_dir):
        raise Exception(f'Error: "{directory}" is not a directory')

    valid_target_dir = cd.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        raise Exception(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )


    try:
        files_dir = os.listdir(target_dir)
    except (FileNotFoundError, PermissionError, NotADirectoryError) as e:
        print(f"Error reading directory: {e}")
        return
    
    if directory == '.':
        directory = 'current'
    print(f"Result for {directory} directory:")
    for file in files_dir:
        try:
            full_path = cd.join(target_dir, file)

            isdir = cd.isdir(full_path)
            file_size = cd.getsize(full_path)


            print(f"- {file}: file_size={file_size} bytes, is_dir={isdir}")

        except (FileNotFoundError, PermissionError, OSError) as e:
            print(f"Error reading file '{file}': {e}")