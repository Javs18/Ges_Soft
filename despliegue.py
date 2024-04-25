import os
import paramiko

def comprimir_archivos():
    # Comprimir archivos de la aplicación en un archivo zip
    os.system("zip -r app.zip app")

def transferir_archivos():
    # Conectar al servidor remoto utilizando SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="000webhost", username="admin", password="admin123")

    # Transferir el archivo zip al servidor remoto
    sftp_client = ssh_client.open_sftp()
    sftp_client.put("customjrz.zip", "/user/web/customjrz.zip")
    sftp_client.close()

    # Cerrar conexión SSH
    ssh_client.close()

def generar_despliegue():
    print("Generando despliegue de la aplicación...")
    comprimir_archivos()
    transferir_archivos()
    print("Despliegue generado exitosamente.")

if __name__ == "__main__":
    generar_despliegue()
