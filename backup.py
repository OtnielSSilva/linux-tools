import shutil
import os

source_dirs = [
    "/home/otniel/Documentos",
    "/home/otniel/Imagens",
    "/home/otniel/Vídeos",
    "/home/otniel/Músicas",
    "/home/otniel/Downloads",
    "/home/otniel/Área de trabalho",
]

backup_dir = "/home/otniel/backup"

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)


def backup_directories(source_dirs, backup_dir):
    for source in source_dirs:
        base_name = os.path.basename(source)
        destination = os.path.join(backup_dir, base_name)
        try:
            shutil.copytree(source, destination)
            print(f"Successfully backed up {source} to {destination}")
        except Exception as e:
            print(f"Failed to backup {source}: {e}")


backup_directories(source_dirs, backup_dir)
