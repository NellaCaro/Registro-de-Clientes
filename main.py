import cliente
import archivos
from test_agregar_usuarios import registrar_clientes_prueba


def main():
    while True:
        print("\n=== Menú de opciones ===")
        print("1. Agregar Cliente")
        print("2. Modificar Cliente")
        print("3. Eliminar Cliente")
        print("4. Generar Archivo de Clientes Bronce")
        print("5. Generar Archivo de Clientes Plata")
        print("6. Generar Archivo de Clientes Oro")
        print("7. Realizar una compra")
        print("8. Mostrar Cliente")
        print("9. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            cliente.agregar_cliente()
        elif opcion == "2":
            dni_modificar = input("Ingrese DNI del cliente a modificar: ")
            cliente.modificar_cliente(dni_modificar)
        elif opcion == "3":
            dni_eliminar = input("Ingrese DNI del cliente a eliminar: ")
            cliente.eliminar_cliente(dni_eliminar)
        elif opcion == "4":
            archivos.generar_archivo_cliente_tipo("Bronce")
            print("Archivo generado: Cliente_Bronce.txt")
        elif opcion == "5":
            archivos.generar_archivo_cliente_tipo("Plata")
            print("Archivo generado: Cliente_Plata.txt")
        elif opcion == "6":
            archivos.generar_archivo_cliente_tipo("Oro")
            print("Archivo generado: Cliente_Oro.txt")
        elif opcion == "7":
            dni_comprador = input("Ingrese DNI del cliente que realizo la compra: ")
            cliente.compra_cliente(dni_comprador)
        elif opcion == "8":
            dni_cliente = input("Ingrese DNI del cliente: ")
            cliente.mostrar_cliente(dni_cliente)
        elif opcion == "9":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    registrar_clientes_prueba()
    main()
