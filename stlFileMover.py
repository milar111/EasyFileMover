import os
import shutil

def move_stl_files(src_folder, dest_folder):
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)


    files = os.listdir(src_folder)

    for file in files:
        if file.endswith(".stl"):
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)

            # Move the file
            shutil.move(src_path, dest_path)
            print(f"Moved: {file}")

if __name__ == "__main__":
    
    source_folder = "path/to/your/downloads"
    destination_folder = "path/to/your/destination/folder"

    move_stl_files(source_folder, destination_folder)
