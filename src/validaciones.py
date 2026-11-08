def leer_texto(mensaje):

    while True:

        dato = input(mensaje).strip()

        if dato:
            return dato

        print(
            "Error: el valor no puede estar vacío."
        )


def leer_entero_positivo(mensaje):

    while True:

        try:

            valor = int(input(mensaje))

            if valor <= 0:

                print(
                    "Error: debe ser mayor que cero."
                )

                continue

            return valor

        except ValueError:

            print(
                "Error: ingrese un número entero válido."
            )


def leer_entero_no_negativo(mensaje):

    while True:

        try:

            valor = int(input(mensaje))

            if valor < 0:

                print(
                    "Error: no se permiten valores negativos."
                )

                continue

            return valor

        except ValueError:

            print(
                "Error: ingrese un número entero válido."
            )


def leer_float_positivo(mensaje):

    while True:

        try:

            valor = float(input(mensaje))

            if valor <= 0:

                print(
                    "Error: el valor debe ser mayor que cero."
                )

                continue

            return valor

        except ValueError:

            print(
                "Error: ingrese un número válido."
            )


def leer_opcion(mensaje, opciones):

    while True:

        opcion = input(
            mensaje
        ).strip()

        if opcion in opciones:
            return opcion

        print(
            "Opción inválida."
        )


def validar_categoria(categoria):

    categorias_validas = {
        "lacteos",
        "bebidas",
        "aseo",
        "abarrotes",
        "snacks"
    }

    return (
        categoria.strip().lower()
        in categorias_validas
    )