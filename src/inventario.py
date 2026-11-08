from tabulate import tabulate

from validaciones import (
    leer_texto,
    leer_entero_positivo,
    leer_entero_no_negativo,
    leer_float_positivo,
    validar_categoria
)


def registrar_producto(inventario):

    codigo = leer_texto(
        "Codigo producto: "
    ).upper()

    if codigo in inventario:

        raise ValueError(
            "El codigo ya existe."
        )

    nombre = leer_texto(
        "Nombre: "
    )

    while True:

        categoria = leer_texto(
            "Categoria (Lacteos, Bebidas, Aseo, Abarrotes, Snacks): "
        )

        categoria_limpia = (
            categoria
            .strip()
            .lower()
        )

        if validar_categoria(
            categoria_limpia
        ):

            categoria = (
                categoria_limpia
                .title()
            )

            break

        print(
            "Categoria invalida."
        )

    precio = leer_float_positivo(
        "Precio: "
    )

    stock = leer_entero_positivo(
        "Stock actual: "
    )

    stock_minimo = (
        leer_entero_positivo(
            "Stock minimo: "
        )
    )

    proveedor = leer_texto(
        "Proveedor: "
    )

    inventario[codigo] = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }

    print(
        "Producto registrado correctamente."
    )


def listar_productos(inventario):

    if not inventario:

        print(
            "Inventario vacio."
        )

        return

    tabla = []

    for producto in inventario.values():

        tabla.append([
            producto["codigo"],
            producto["nombre"],
            producto["categoria"],
            producto["precio"],
            producto["stock"],
            producto["stock_minimo"],
            producto["proveedor"]
        ])

    print(
        tabulate(
            tabla,
            headers=[
                "Codigo",
                "Nombre",
                "Categoria",
                "Precio",
                "Stock",
                "Minimo",
                "Proveedor"
            ],
            tablefmt="grid"
        )
    )


def buscar_por_codigo(inventario):

    codigo = input(
        "Codigo: "
    ).upper()

    producto = inventario.get(
        codigo
    )

    if producto is None:

        print(
            "Producto no encontrado."
        )

        return

    print(
        "\n=== PRODUCTO ENCONTRADO ==="
    )

    for clave, valor in producto.items():

        print(
            f"{clave}: {valor}"
        )


def buscar_por_categoria(
    inventario
):

    categoria = input(
        "Categoria: "
    ).strip().lower()

    encontrados = []

    for producto in inventario.values():

        if (
            producto["categoria"]
            .lower()
            ==
            categoria
        ):

            encontrados.append([
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            ])

    if not encontrados:

        print(
            "No hay productos para esa categoria."
        )

        return

    print(
        tabulate(
            encontrados,
            headers=[
                "Codigo",
                "Nombre",
                "Precio",
                "Stock"
            ],
            tablefmt="grid"
        )
    )


def modificar_producto(
    inventario
):

    codigo = input(
        "Codigo del producto: "
    ).upper()

    producto = inventario.get(
        codigo
    )

    if producto is None:

        print(
            "Producto no encontrado."
        )

        return

    print(
        "\nProducto encontrado."
    )

    print(
        f"Precio actual : {producto['precio']}"
    )

    print(
        f"Stock actual : {producto['stock']}"
    )

    nuevo_precio = (
        leer_float_positivo(
            "Nuevo precio: "
        )
    )

    nuevo_stock = (
        leer_entero_no_negativo(
            "Nuevo stock: "
        )
    )

    producto["precio"] = (
        nuevo_precio
    )

    producto["stock"] = (
        nuevo_stock
    )

    print(
        "Producto actualizado."
    )


def eliminar_producto(
    inventario
):

    codigo = input(
        "Codigo: "
    ).upper()

    if codigo not in inventario:

        print(
            "Producto inexistente."
        )

        return

    nombre = (
        inventario[codigo]
        ["nombre"]
    )

    del inventario[codigo]

    print(
        f"{nombre} eliminado correctamente."
    )