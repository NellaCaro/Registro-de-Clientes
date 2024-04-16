
def calcular_puntos_afiliacion(medio):
    if medio == "recomendacion":
        return 500, 200
    elif medio == "whatsapp":
        return 50, 0
    elif medio == "web":
        return 100, 0
    else:
        return 0, 0

def calcular_puntos_compra(puntos_actuales):
    return puntos_actuales + 250

# Función para clasificar al cliente según sus puntos
def clasificar_cliente(puntos):
    if 50 <= puntos <= 1000:
        return "Bronce"
    elif 1001 <= puntos <= 5000:
        return "Plata"
    elif puntos >= 5001:
        return "Oro"
