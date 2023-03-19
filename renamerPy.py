import os

folder_path = "/path/to/folder/" # replace with the path to your folder
counter = 1

for filename in sorted(os.listdir(folder_path)):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_extension = os.path.splitext(filename)[1]
        new_filename = str(counter).zfill(4) + file_extension
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        counter += 1