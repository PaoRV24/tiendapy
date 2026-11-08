from inventario import (
    registrar_producto,
    listar_productos,
    buscar_por_codigo,
    buscar_por_categoria,
    modificar_producto,
    eliminar_producto
)

from ventas import (
    registrar_venta
)

from reportes import (
    alertas_stock,
    cierre_dia
)

from persistencia import (
    cargar_inventario,
    guardar_inventario
)


def mostrar_menu():

    print(
        "\n================================="
    )

    print(
        "         TIENDAPY"
    )

    print(
        "================================="
    )

    print(
        "1. Registrar producto"
    )

    print(
        "2. Listar productos"
    )

    print(
        "3. Buscar por codigo"
    )

    print(
        "4. Buscar por categoria"
    )

    print(
        "5. Modificar producto"
    )

    print(
        "6. Eliminar producto"
    )

    print(
        "7. Registrar venta"
    )

    print(
        "8. Alertas de stock"
    )

    print(
        "9. Cierre del dia"
    )

    print(
        "10. Guardar cambios"
    )

    print(
        "0. Salir"
    )


def main():

    inventario = (
        cargar_inventario()
    )

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opcion: "
        )

        try:

            if opcion == "1":

                registrar_producto(
                    inventario
                )

            elif opcion == "2":

                listar_productos(
                    inventario
                )

            elif opcion == "3":

                buscar_por_codigo(
                    inventario
                )

            elif opcion == "4":

                buscar_por_categoria(
                    inventario
                )

            elif opcion == "5":

                modificar_producto(
                    inventario
                )

            elif opcion == "6":

                eliminar_producto(
                    inventario
                )

            elif opcion == "7":

                registrar_venta(
                    inventario
                )

            elif opcion == "8":

                alertas_stock(
                    inventario
                )

            elif opcion == "9":

                cierre_dia(
                    inventario
                )

            elif opcion == "10":

                guardar_inventario(
                    inventario
                )

                print(
                    "\nInventario guardado correctamente."
                )

            elif opcion == "0":

                guardar_inventario(
                    inventario
                )

                print(
                    "\nCambios guardados."
                )

                print(
                    "Hasta pronto."
                )

                break

            else:

                print(
                    "Opcion invalida."
                )

        except ValueError as error:

            print(
                f"\nError: {error}"
            )

        except Exception as error:

            print(
                "\n================================="
            )

            print(
                "ERROR INESPERADO"
            )

            print(
                f"Detalle: {error}"
            )

            print(
                "La aplicacion continuara ejecutandose."
            )

            print(
                "================================="
            )


if __name__ == "__main__":

    main()