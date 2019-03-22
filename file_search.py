import os
import shutil


def list_files(search_dir, dest_dir):
    result = []
    error = []
    for root, dirs, files in os.walk(search_dir):
        for name in files:
            if 'exit' in name.lower():  # search filename with 'exit'
                try:
                    result.append(os.path.join(root, name))  # append file names
                    shutil.copy(os.path.join(root, name), dest_dir)  # copy file to destination folder
                except FileNotFoundError:  # in case the file name is too long
                    error.append(os.path.join(root, name))  # collect failed ones to view later
                    pass
    return result, error


if __name__ == '__main__':
    path = r'T:\files'  # map a new drive is helpful to resolve file name too long issue if needed
    dest = r'c:\exit_forms'
    os.makedirs(dest, exist_ok=True)  # create destination folder if not already exist

    print('starting...')
    result, error = list_files(search_dir=path, dest_dir=dest)
    print('completed')
