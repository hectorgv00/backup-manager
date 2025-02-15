import os
import shutil
from datetime import datetime

def create_backup(source_folder, target_folder):
    """Creates a backup of the source folder inside the target _ folder with a timest
Args:
source folder (str): The path of the folder to back up.
target _ folder (str): The path where backups will be stored.
"""
    try:
    # Ensure the source folder exists
        if not os.path.exists(source_folder):
            print(f"Error: La carpeta de origen no existe: {source_folder}")
            return
    
        # Ensure the target folder exists; i f not, create it
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"Carpeta de destino creada: {target_folder}")
        else:
            print(f"Carpeta de destino existente: {target_folder}")
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_subfolder = os.path.join(target_folder, timestamp)

        # Create a subfolder in the target folder with the timestamp
        os.makedirs(backup_subfolder)
        print(f"Subcarpeta de copia de seguridad creada: {backup_subfolder}")

        # Define destination folder
        destination = os.path.join(backup_subfolder, os.path.basename(source_folder))

        # Copy the source folder to the destination folder
        shutil.copytree(source_folder, destination)
        print(f"Copia de seguridad creada en: {destination}")
    except Exception as e:
        print(f"Error: {e}")
    
    if __name__ == "__main__":
        source_folder = "/var/www/html"
        target_folder = "/home/Backups"
        create_backup(source_folder, target_folder)
        print("Backup completed")