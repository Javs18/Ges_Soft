import os
import shutil

def instalar_dependencias():
    # Instalar dependencias del sistema
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y apache2 sqlite3")

def configurar_basedatos():
    # Configurar base de datos SQLite
    os.system("sqlite3 database.db < schema.sql")

def desplegar_aplicacion():
    # Copiar archivos de la aplicación al directorio de despliegue del servidor
    shutil.copytree("customjrz", "/user/web/customjrz")

def reiniciar_servidor():
    # Reiniciar servidor web Apache
    os.system("sudo service apache2 restart")

def crear_entorno_de_liberacion():
    print("Creando entorno de liberación para la página web de venta de tenis personalizados...")
    instalar_dependencias()
    configurar_basedatos()
    desplegar_aplicacion()
    reiniciar_servidor()
    print("Entorno de liberación creado exitosamente.")

if __name__ == "__main__":
    crear_entorno_de_liberacion()
