import cliente
from puntajes import clasificar_cliente

def generar_archivo_cliente_tipo(tipo):
    filename = f"Cliente_{tipo}.txt"

    with open(filename, "w") as file:
        file.write("DNI,Nombre,Domicilio,Email,Medio de Afiliacion,Puntaje Actual,Clasificacion\n")

        for c in cliente.clientes:
            puntos_totales = c['puntos_afiliacion'] + c['puntos_compra']
            clasificacion = clasificar_cliente(puntos_totales)

            if clasificacion == tipo:
                linea = f"{c['dni']},{c['nombre']},{c['domicilio']},{c['email']},{c['medio_afiliacion']},{puntos_totales},{clasificacion}\n"
                file.write(linea)