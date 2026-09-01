import os

# Specify the directory path
directory_path = '' # Current directory, or you can use an absolute path

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")