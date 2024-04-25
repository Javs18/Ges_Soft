import requests

def probar_servidor():
    # Probar si el servidor está en funcionamiento
    try:
        response = requests.get("http://localhost")
        if response.status_code == 200:
            print("El servidor está en funcionamiento.")
        else:
            print("Error: El servidor no está respondiendo correctamente.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def probar_pagina_de_inicio():
    # Probar la accesibilidad de la página de inicio
    try:
        response = requests.get("http://localhost")
        if response.status_code == 200:
            print("La página de inicio es accesible.")
        else:
            print("Error: La página de inicio no está accesible.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def ejecutar_pruebas():
    print("Ejecutando pruebas en el entorno de liberación...")
    probar_servidor()
    probar_pagina_de_inicio()
    print("Pruebas completadas.")

if __name__ == "__main__":
    ejecutar_pruebas()
