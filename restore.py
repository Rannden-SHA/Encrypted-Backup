import os
import json
from cryptography.fernet import Fernet

# Directorio de la copia de seguridad y destino para los archivos desencriptados
backup_dir = 'C:\\ruta\\a\\tu\\carpeta\\copia_seguridad'
decrypt_dir = 'C:\\ruta\\destino\\restauracion'

# Crea el directorio de destino si no existe
if not os.path.exists(decrypt_dir):
    os.makedirs(decrypt_dir)

# Lee la clave de encriptación
key_path = os.path.join(backup_dir, 'encryption_key.key')
with open(key_path, 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)

# Lee el mapeo de nombres de archivo
map_path = os.path.join(backup_dir, 'file_map.json')
with open(map_path, 'r') as map_file:
    file_map = json.load(map_file)

# Función para desencriptar y restaurar los archivos
def decrypt_and_restore_file(encrypted_filename, relative_path, decrypt_dir):
    try:
        # Ruta completa del archivo encriptado
        encrypted_filepath = os.path.join(backup_dir, encrypted_filename)
        
        # Lee el contenido del archivo encriptado
        with open(encrypted_filepath, 'rb') as file:
            encrypted_data = file.read()
        
        # Desencripta el contenido del archivo
        decrypted_data = cipher.decrypt(encrypted_data)
        
        # Ruta completa del archivo desencriptado
        decrypt_filepath = os.path.join(decrypt_dir, relative_path)
        
        # Crea las carpetas necesarias si no existen
        os.makedirs(os.path.dirname(decrypt_filepath), exist_ok=True)
        
        # Guarda el archivo desencriptado con su nombre original en el directorio de destino
        with open(decrypt_filepath, 'wb') as decrypt_file:
            decrypt_file.write(decrypted_data)
    except Exception as e:
        print(f"Error desencriptando el archivo {encrypted_filename}: {e}")

# Recorre el mapeo de archivos y restaura cada uno
for encrypted_filename, relative_path in file_map.items():
    decrypt_and_restore_file(encrypted_filename, relative_path, decrypt_dir)

print("Archivos desencriptados y restaurados con sus nombres y rutas originales.")
