import os 
import shutil

path = input("Enter your path: ").strip().replace('"','')

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if os.path.isdir(full_path):
        continue
    filename, extension = os.path.splitext(file)

    if extension == "":
        continue
    extension = extension[1:]

    folder_path = os.path.join(path, extension)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(full_path, os.path.join(folder_path, file))