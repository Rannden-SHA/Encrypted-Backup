import os
import uuid
import json
from cryptography.fernet import Fernet

# Directorio de origen y destino (modifica estas rutas según tu configuración)
source_dir = 'C:\\ruta\\a\\copiar'
backup_dir = 'C:\\ruta\\a\\tu\\carpeta\\copia_seguridad'

# Crea el directorio de copia de seguridad si no existe
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Ruta del archivo de clave y archivo de mapeo
key_path = os.path.join(backup_dir, 'encryption_key.key')
map_path = os.path.join(backup_dir, 'file_map.json')

# Genera una clave para la encriptación si no existe
if not os.path.exists(key_path):
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
else:
    with open(key_path, 'rb') as key_file:
        key = key_file.read()

cipher = Fernet(key)

# Cargar el mapeo de nombres de archivo si existe
if os.path.exists(map_path):
    with open(map_path, 'r') as map_file:
        file_map = json.load(map_file)
else:
    file_map = {}

# Función para encriptar y guardar los archivos
def encrypt_and_backup_file(filepath, backup_dir):
    try:
        # Lee el contenido del archivo original
        with open(filepath, 'rb') as file:
            file_data = file.read()
        
        # Encripta el contenido del archivo
        encrypted_data = cipher.encrypt(file_data)
        
        # Genera un nombre de archivo único
        unique_filename = str(uuid.uuid4())
        
        # Guarda el archivo encriptado en el directorio de copia de seguridad
        backup_filepath = os.path.join(backup_dir, unique_filename)
        with open(backup_filepath, 'wb') as backup_file:
            backup_file.write(encrypted_data)
        
        # Guarda el mapeo del nombre original, la ruta relativa y el nombre encriptado
        relative_path = os.path.relpath(filepath, source_dir)
        file_map[unique_filename] = relative_path

        # Actualiza el archivo de mapeo
        with open(map_path, 'w') as map_file:
            json.dump(file_map, map_file)

    except Exception as e:
        print(f"Error encriptando el archivo {filepath}: {e}")

# Recorre todos los archivos en el directorio de origen
for root, dirs, files in os.walk(source_dir):
    for file in files:
        filepath = os.path.join(root, file)
        if os.path.basename(filepath) != 'encryption_key.key' and os.path.basename(filepath) != 'file_map.json':
            encrypt_and_backup_file(filepath, backup_dir)

print("Copia de seguridad completada y archivos encriptados.")
