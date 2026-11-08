from datetime import date

from validaciones import (
    leer_entero_positivo,
    leer_float_positivo
)

from persistencia import (
    registrar_venta_txt
)


def calcular_descuento(
    subtotal
):

    if subtotal >= 100000:

        return subtotal * 0.10

    if subtotal >= 50000:

        return subtotal * 0.05

    return 0


def mostrar_carrito(
    carrito,
    inventario
):

    if not carrito:
        return

    print(
        "\n::: CARRITO :::"
    )

    for codigo, cantidad in (
        carrito.items()
    ):

        producto = inventario[
            codigo
        ]

        print(
            f"{codigo} - "
            f"{producto['nombre']} - "
            f"{cantidad}"
        )


def registrar_venta(
    inventario
):

    carrito = {}

    subtotal = 0

    while True:

        codigo = input(
            "\nCodigo producto "
            "(0 finalizar): "
        ).upper()

        if codigo == "0":
            break

        producto = inventario.get(
            codigo
        )

        if producto is None:

            print("Producto inexistente.")

            continue

        print(
            f"Producto: "
            f"{producto['nombre']}"
        )

        print(
            f"Stock disponible: "
            f"{producto['stock']}"
        )

        cantidad = (
            leer_entero_positivo(
                "Cantidad: "
            )
        )

        stock_disponible = (
            producto["stock"]
            -
            carrito.get(
                codigo,
                0
            )
        )

        if cantidad > stock_disponible:

            raise ValueError(
                "Stock insuficiente."
            )

        carrito[codigo] = (
            carrito.get(
                codigo,
                0
            )
            +
            cantidad
        )

        subtotal += (
            producto["precio"]
            * cantidad
        )

        mostrar_carrito(
            carrito,
            inventario
        )

    if not carrito:

        print("Venta cancelada.")

        return

    descuento = (
        calcular_descuento(
            subtotal
        )
    )

    total = subtotal - descuento

    print("\n::: RESUMEN VENTA :::")

    print(
        f"Subtotal: "
        f"${subtotal:,.0f}"
    )

    print(
        f"Descuento: "
        f"${descuento:,.0f}"
    )

    print(
        f"Total: "
        f"${total:,.0f}"
    )

    while True:

        pago = (
            leer_float_positivo(
                "Pago recibido: "
            )
        )

        if pago < total:

            print(
                "Pago insuficiente."
            )

            continue

        break

    cambio = pago - total

    print(
        f"Cambio: "
        f"${cambio:,.0f}"
    )

    for codigo, cantidad in (
        carrito.items()
    ):

        inventario[codigo][
            "stock"
        ] -= cantidad

    registrar_venta_txt(
        str(date.today()),
        total,
        carrito
    )

    print("\nVenta registrada correctamente.")