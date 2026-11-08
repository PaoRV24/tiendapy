from collections import defaultdict

from persistencia import (
    cargar_ventas
)


def alertas_stock(inventario):

    proveedores = defaultdict(list)

    for producto in inventario.values():

        if (
            producto["stock"]
            <=
            producto["stock_minimo"]
        ):

            estado = "AGOTADO"

            if producto["stock"] > 0:
                estado = "BAJO STOCK"

            proveedores[
                producto["proveedor"]
            ].append(
                (
                    producto["nombre"],
                    producto["stock"],
                    estado
                )
            )

    if not proveedores:

        print(
            "\nNo existen alertas de stock."
        )

        return

    print(
        "\n=== ALERTAS DE INVENTARIO ==="
    )

    for proveedor, productos in proveedores.items():

        print(
            f"\nPROVEEDOR: {proveedor}"
        )

        for nombre, stock, estado in productos:

            print(
                f"- {nombre} | "
                f"Stock: {stock} | "
                f"{estado}"
            )


def cierre_dia(inventario):

    ventas = cargar_ventas()

    if not ventas:

        print(
            "\nNo existen ventas registradas."
        )

        return

    total_vendido = 0

    movimientos = {}

    productos_vendidos = set()

    for venta in ventas:

        total_vendido += venta["total"]

        detalle = venta["detalle"]

        productos = detalle.split(";")

        for producto in productos:

            codigo, cantidad = (
                producto.split(":")
            )

            cantidad = int(cantidad)

            productos_vendidos.add(
                codigo
            )

            movimientos[codigo] = (
                movimientos.get(
                    codigo,
                    0
                )
                +
                cantidad
            )

    numero_ventas = len(ventas)

    ticket_promedio = (
        total_vendido
        /
        numero_ventas
    )

    if movimientos:

        codigo_mas_vendido = max(
            movimientos,
            key=movimientos.get
        )

        if codigo_mas_vendido in inventario:

            producto_mas_vendido = (
                inventario[
                    codigo_mas_vendido
                ]["nombre"]
            )

        else:

            producto_mas_vendido = (
                codigo_mas_vendido
            )

    else:

        producto_mas_vendido = (
            "Ninguno"
        )

    productos_sin_ventas = []

    categorias_con_movimiento = set()

    for codigo, producto in (
        inventario.items()
    ):

        if codigo not in productos_vendidos:

            productos_sin_ventas.append(
                producto["nombre"]
            )

        else:

            categorias_con_movimiento.add(
                producto["categoria"]
            )

    print(
        "\n===== CIERRE DEL DIA ====="
    )

    print(
        f"Total vendido: "
        f"${total_vendido:,.0f}"
    )

    print(
        f"Numero de ventas: "
        f"{numero_ventas}"
    )

    print(
        f"Ticket promedio: "
        f"${ticket_promedio:,.0f}"
    )

    print(
        f"Producto mas vendido: "
        f"{producto_mas_vendido}"
    )

    print(
        "\nProductos sin ventas:"
    )

    if not productos_sin_ventas:

        print(
            "Todos tuvieron movimiento."
        )

    else:

        for producto in productos_sin_ventas:

            print(
                f"- {producto}"
            )

    print(
        "\nCategorias con movimiento:"
    )

    for categoria in sorted(
        categorias_con_movimiento
    ):

        print(
            f"- {categoria}"
        )