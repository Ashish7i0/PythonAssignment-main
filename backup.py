import os
import sys
import shutil
from datetime import datetime

def files_backup(source_dir, dest_dir):
    try:
        # Check whether the source directory exists or not
        if not os.path.exists(source_dir):
            print(f"The source directory '{source_dir}' doesn't exist! Please provide a valid source directory")
            return

        # Create whether the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)

        # Iterating through all the files in the source directory
        for file in os.listdir(source_dir):
            source_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)

            # Append timestamp to the destination file name if it already exists
            if os.path.exists(dest_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                base_name, ext = os.path.splitext(file)
                backup_file = f"{base_name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, backup_file)

            # Copying the file
            shutil.copy2(source_path, dest_path)
            print(f"Copied '{file}' to '{dest_path}'")

        print("Backup of all the files completed successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please input the source and destination path of the files you wish to backup in the format:")
        print("python backup.py /path/to/source /path/to/destination")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        files_backup(source_directory, destination_directory)
