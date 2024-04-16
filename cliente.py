from puntajes import calcular_puntos_afiliacion, calcular_puntos_compra, clasificar_cliente

clientes = []

def agregar_cliente():
    dni = input("Ingrese DNI del cliente: ")
    nombre = input("Ingrese nombre y apellido del cliente: ")
    domicilio = input("Ingrese domicilio del cliente: ")
    email = input("Ingrese dirección de correo electrónico del cliente: ")
    medio_afiliacion = input("Ingrese medio de afiliación (web/recomendacion/whatsapp): ").lower()

    puntos_recomendador, puntos_afiliacion = calcular_puntos_afiliacion(medio_afiliacion)

    puntos_compra = 0

    clientes.append({
        "dni": dni,
        "nombre": nombre,
        "domicilio": domicilio,
        "email": email,
        "medio_afiliacion": medio_afiliacion,
        "puntos_afiliacion": puntos_afiliacion,
        "puntos_compra": puntos_compra
    })

    if medio_afiliacion == "recomendacion":
        dni_recomendador = input("Ingrese DNI del cliente que recomendó: ")
        recomendador_encontrado = False  # Variable para verificar si se encontró el recomendador
        for c in clientes:
            if c["dni"] == dni_recomendador:
                c["puntos_afiliacion"] += puntos_recomendador
                print(f"{puntos_recomendador} puntos añadidos al cliente que recomendó.")
                recomendador_encontrado = True
                break
        if not recomendador_encontrado:
            print(f"DNI: {dni_recomendador} no encontrado")

    print("Cliente agregado con éxito.\n")

def modificar_cliente(dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            print("Modificar datos del cliente:")
            nombre = input(f"Nuevo nombre y apellido ({cliente['nombre']}): ") or cliente['nombre']
            domicilio = input(f"Nuevo domicilio ({cliente['domicilio']}): ") or cliente['domicilio']
            email = input(f"Nueva dirección de correo electrónico ({cliente['email']}): ") or cliente['email']

            cliente.update({
                "nombre": nombre,
                "domicilio": domicilio,
                "email": email
            })

            print("Datos del cliente modificados con éxito.\n")
            return

    print("Cliente no encontrado.\n")

def eliminar_cliente(dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            clientes.remove(cliente)
            print("Cliente eliminado con éxito.\n")
            return

    print("Cliente no encontrado.\n")

def compra_cliente(dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            puntaje = calcular_puntos_compra(cliente['puntos_afiliacion']);
            cliente.update({
                "puntos_compra": puntaje
            })
            clasificacion = clasificar_cliente(puntaje)
            if clasificacion == "Bronce":
                descuento = "10% de descuento"
            elif clasificacion == "Plata":
                descuento = "15% de descuento"
            elif clasificacion == "Oro":
                descuento = "20% de descuento"
            else:
                descuento = "0 de descuento"

            print(f"Se agregan 250 puntos por compra, su clasificacion es: {clasificacion} y tienes {descuento} en futuras compras\n")
            return

    print("Cliente no encontrado.\n")

def mostrar_cliente(dni_buscar):
    for cliente in clientes:
        if cliente["dni"] == dni_buscar:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        print("Cliente encontrado:")
        print("DNI:", cliente_encontrado["dni"])
        print("Nombre:", cliente_encontrado["nombre"])
        print("Domicilio:", cliente_encontrado["domicilio"])
        print("Email:", cliente_encontrado["email"])
        print("Medio de Afiliación:", cliente_encontrado["medio_afiliacion"])
        print("Puntos de Afiliación:", cliente_encontrado["puntos_afiliacion"])
        print("Puntos de Compra:", cliente_encontrado["puntos_compra"])
        print("Categoria:", clasificar_cliente(cliente_encontrado["puntos_afiliacion"]))
    else:
        print(f"No se encontró ningún cliente con DNI {dni_buscar}.")
