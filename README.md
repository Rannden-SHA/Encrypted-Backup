# Encrypted-Backup
Backup files with encryption

# 🛡️ Script de Encriptado y Desencriptado de Archivos 🗝️

Este repositorio contiene scripts en Python que permiten hacer un respaldo de un directorio y encriptar los archivos. Además, incluye un script para desencriptar los archivos y restaurarlos a su estado original.

## 📋 Tabla de Contenidos

- [Descripción](#Descripción)
- [Características](#Características)
- [Requisitos](#Requisitos)
- [Instalación](#Instalación)
- [Uso](#Uso)
- [Problemas Conocidos](#Problemas-Conocidos)
- [Contribución](#Contribución)
- [Licencia](#Licencia)

## 📝 Descripción

Estos scripts permiten encriptar y desencriptar archivos en un directorio especificado. La información necesaria para desencriptar (clave y mapeo) se guarda en un directorio separado. Esto es útil para asegurar la confidencialidad de los datos almacenados.

## ✨ Características

- **Encriptación**: Encripta archivos usando el algoritmo Fernet.
- **Desencriptación**: Restaura los archivos encriptados a su estado original.
- **Mapeo**: Mantiene un mapeo de los archivos encriptados para asegurar la correcta restauración.
- **Manejo de Errores**: Verifica permisos y maneja excepciones durante el proceso.

## 🔧 Requisitos

- Python 3.x
- Módulo `cryptography`

## 🚀 Instalación

1. Clona el repositorio:

```
git clone https://github.com/Rannden-SHA/Encrypted-Backup.git
```

3. Navega al directorio del proyecto:

```
cd Encrypted-Backup
```

3. Instala las dependencias:

```
pip install cryptography
```

## 📂 Estructura del Proyecto

```
Encrypted-Backup/
├── backup.py
├── restore.py
├── README.md
└── mapeo/
    ├── encryption_key.key
    └── file_map.json
```

## 🛠️ Uso
Encriptar Archivos

Primero hay que editar el script y modificar las lineas donde están las variables source_dir y backup_dir que se encuentran al principio del código (para indicar la ruta de la carpeta que queremos hacer el backup y el destino al que se creará una copia encriptada, respectivamente)

  Ejecutar el script de encriptado:
      Abre el símbolo del sistema como administrador.
      Navega hasta el directorio del script.
      Ejecuta el script:
    
```
python backup.py
```

Desencriptar Archivos

Primero hay que editar el script y modificar las lineas donde están las variables bcakup_dir y decrypt_dir que se encuentran al principio del código (para indicar la ruta de la carpeta que queremos restaurar y el destino al que se creará una copia desencriptada, respectivamente)

  Ejecutar el script de desencriptado:
      Abre el símbolo del sistema.
      Navega hasta el directorio del script.
      Ejecuta el script:
        
```
python restore.py
```

## ⚠️ Problemas Conocidos

  Permisos: Si el script no puede sobrescribir un archivo, asegúrate de tener los permisos necesarios para copiar los archivos en el directorio de origen.
  Interrupciones: Si el script se interrumpe, los mapeos y la clave se mantendrán actualizados, permitiendo reanudar la operación en el punto donde se detuvo.

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

  Haz un fork del proyecto.
  Crea una nueva rama (feature/nueva-funcionalidad).
  Realiza los cambios necesarios y haz commit de los mismos.
  Envía un pull request.

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más información, consulta el archivo LICENSE.
