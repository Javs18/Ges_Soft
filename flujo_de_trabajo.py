class PaginaVentaTenisPersonalizados:
    def __init__(self):
        self.flujo = []

    def agregar_paso(self, paso):
        self.flujo.append(paso)

    def ejecutar_flujo(self):
        for paso in self.flujo:
            paso()

def inicio_sesion_o_registro():
    print("Paso 1: Inicio de sesión o registro")

def explorar_productos():
    print("Paso 2: Exploración de productos")

def personalizar_tenis():
    print("Paso 3: Personalización del tenis")

def carrito_de_compras():
    print("Paso 4: Carrito de compras")

def proceso_de_pago():
    print("Paso 5: Proceso de pago")

def confirmar_orden():
    print("Paso 6: Confirmación de la orden")

def seguimiento_y_entrega():
    print("Paso 7: Seguimiento y entrega")

def soporte_al_cliente():
    print("Paso 8: Soporte al cliente")

# Crear una instancia de la clase PaginaVentaTenisPersonalizados
pagina_venta_tenis = PaginaVentaTenisPersonalizados()

# Agregar los pasos al flujo de trabajo en orden
pagina_venta_tenis.agregar_paso(inicio_sesion_o_registro)
pagina_venta_tenis.agregar_paso(explorar_productos)
pagina_venta_tenis.agregar_paso(personalizar_tenis)
pagina_venta_tenis.agregar_paso(carrito_de_compras)
pagina_venta_tenis.agregar_paso(proceso_de_pago)
pagina_venta_tenis.agregar_paso(confirmar_orden)
pagina_venta_tenis.agregar_paso(seguimiento_y_entrega)
pagina_venta_tenis.agregar_paso(soporte_al_cliente)

# Ejecutar el flujo de trabajo
pagina_venta_tenis.ejecutar_flujo()
