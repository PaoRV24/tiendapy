from pathlib import Path


RUTA_INVENTARIO = Path(
    "data/inventario.txt"
)

RUTA_VENTAS = Path(
    "data/ventas.txt"
)


def crear_archivos_si_no_existen():

    RUTA_INVENTARIO.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if not RUTA_INVENTARIO.exists():

        RUTA_INVENTARIO.touch()

    if not RUTA_VENTAS.exists():

        RUTA_VENTAS.touch()


def cargar_inventario():

    inventario = {}

    crear_archivos_si_no_existen()

    try:

        with open(
            RUTA_INVENTARIO,
            "r",
            encoding="utf-8"
        ) as archivo:

            for numero_linea, linea in enumerate(
                archivo,
                start=1
            ):

                linea = linea.strip()

                if not linea:
                    continue

                try:

                    datos = linea.split("|")

                    if len(datos) != 7:
                        raise ValueError

                    producto = {
                        "codigo": datos[0],
                        "nombre": datos[1],
                        "categoria": datos[2],
                        "precio": float(datos[3]),
                        "stock": int(datos[4]),
                        "stock_minimo": int(datos[5]),
                        "proveedor": datos[6]
                    }

                    inventario[
                        producto["codigo"]
                    ] = producto

                except (
                    ValueError,
                    IndexError
                ):

                    print(
                        f"Advertencia: línea "
                        f"{numero_linea} inválida."
                    )

    except FileNotFoundError:

        print(
            "No existe inventario.txt"
        )

    return inventario


def guardar_inventario(
    inventario
):

    crear_archivos_si_no_existen()

    with open(
        RUTA_INVENTARIO,
        "w",
        encoding="utf-8"
    ) as archivo:

        for producto in inventario.values():

            linea = (
                f"{producto['codigo']}|"
                f"{producto['nombre']}|"
                f"{producto['categoria']}|"
                f"{producto['precio']}|"
                f"{producto['stock']}|"
                f"{producto['stock_minimo']}|"
                f"{producto['proveedor']}\n"
            )

            archivo.write(linea)


def registrar_venta_txt(
    fecha,
    total,
    detalle
):

    crear_archivos_si_no_existen()

    productos = []

    for codigo, cantidad in detalle.items():

        productos.append(
            f"{codigo}:{cantidad}"
        )

    detalle_texto = ";".join(
        productos
    )

    linea = (
        f"{fecha}|"
        f"{total}|"
        f"{detalle_texto}\n"
    )

    with open(
        RUTA_VENTAS,
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(linea)


def cargar_ventas():

    ventas = []

    crear_archivos_si_no_existen()

    try:

        with open(
            RUTA_VENTAS,
            "r",
            encoding="utf-8"
        ) as archivo:

            for linea in archivo:

                linea = linea.strip()

                if not linea:
                    continue

                try:

                    fecha, total, detalle = (
                        linea.split("|")
                    )

                    ventas.append(
                        {
                            "fecha": fecha,
                            "total": float(total),
                            "detalle": detalle
                        }
                    )

                except (
                    ValueError,
                    IndexError
                ):

                    print(
                        "Advertencia: venta corrupta."
                    )

    except FileNotFoundError:

        pass

    return ventas


def obtener_producto_por_codigo(
    inventario,
    codigo
):

    return inventario.get(
        codigo.upper()
    )