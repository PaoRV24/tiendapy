TiendaPy
Programa de consola en Python para gestionar el inventario y las ventas de una tienda de barrio. Este proyecto fue desarrollado como trabajo final del curso Python 0 a 100 de ACM.

Qué hace
Registra productos nuevos en el inventario.
Busca productos por código o por categoría.
Modifica precios y stock de productos existentes.
Elimina productos del inventario.
Registra ventas con uno o varios productos.
Aplica descuentos automáticos según el valor de la compra.
Calcula el cambio a entregar al cliente.
Descuenta automáticamente el stock cuando se registra una venta.
Genera alertas de productos con bajo stock o agotados.
Genera el cierre del día con estadísticas de ventas.
Guarda toda la información en archivos de texto para conservar los datos entre ejecuciones.
Reglas de la tienda
No se puede vender una cantidad mayor al stock disponible.
No se permiten precios ni cantidades iguales o inferiores a cero.
Las compras iguales o superiores a $50.000 reciben un descuento del 5%.
Las compras iguales o superiores a $100.000 reciben un descuento del 10%.
El pago recibido no puede ser inferior al total de la compra.
Los códigos de producto no pueden repetirse.
Un producto con stock igual a cero aparece como AGOTADO en las alertas.

Cómo correrlo
Necesita Python 3 (probado con Python 3.12) y la librería tabulate.

Crear entorno virtual (solo la primera vez)
python -m venv venv
Instalar dependencias
pip install -r requirements.txt
Ejecutar el programa
python src/main.py

Tener en cuenta: hay que correr el programa desde la carpeta tiendapy/, porque las rutas de data/ son internas.

Al correr, el programa carga automáticamente el inventario almacenado en inventario.txt y muestra el menú principal.

Archivos de datos
data/inventario.txt
Contiene un producto por línea.

Formato:

codigo|nombre|categoria|precio|stock|stock_minimo|proveedor
Ejemplo:

LAC001|Leche Entera 1L|Lacteos|4200|35|10|Alqueria
data/ventas.txt
Contiene una venta por línea.

Formato:

fecha|total|codigo:cantidad;codigo:cantidad
Ejemplo:

2026-11-02|8400|LAC001:2
Si inventario.txt o ventas.txt no existen, el programa los crea automáticamente al iniciar. Si encuentra una línea dañada, la ignora y continúa con las demás.

Cómo se encuentra organizado el código
El proyecto está dividido en módulos para separar responsabilidades y facilitar su uso y mantenimiento.

src/main.py
Acá es el punto de entrada del programa. Contiene el menú principal y coordina todas las operaciones del sistema.

src/inventario.py
Gestiona las operaciones relacionadas con el inventario:

Registrar productos
Buscar productos por código
Buscar productos por categoría
Modificar productos
Eliminar productos
Listar productos

src/ventas.py
Gestiona el proceso de ventas:

Registro de ventas
Validación de stock
Aplicación de descuentos
Cálculo del total
Cálculo del cambio
Actualización automática del inventario

src/reportes.py
Genera los reportes del sistema:

Alertas de stock
Productos agotados
Cierre del día
Producto más vendido
Ticket promedio
Productos sin ventas
Categorías con movimiento

src/persistencia.py
Gestiona la lectura y escritura de los archivos:

inventario.txt
ventas.txt
También crea automáticamente los archivos de datos si en el caso que no existan.

src/validaciones.py
Contiene las funciones reutilizables para validar los datos ingresados por el usuario:

Texto obligatorio
Enteros positivos
Enteros no negativos
Números decimales positivos
Categorías válidas

Decisiones
Proyecto modular. El código se separó en varios archivos para mantener responsabilidades independientes y facilitar el mantenimiento.
Sin programación orientada a objetos. Los productos se representan mediante diccionarios y el inventario mediante un diccionario cuya clave es el código del producto.
Persistencia en archivos de texto. El inventario y las ventas se almacenan en archivos .txt, siguiendo los requisitos del proyecto.
Validaciones centralizadas. Todas las validaciones reutilizables se encuentran en validaciones.py.
Tablas con tabulate. Se utiliza la librería tabulate para mejorar la presentación de la información en consola.
Control de versiones con Git. El proyecto fue gestionado mediante Git para registrar y controlar cambios durante el desarrollo.
Entorno virtual con venv. Las dependencias se aislaron mediante un entorno virtual para mantener el proyecto independiente del sistema operativo.

Autora
Yully Paola Reyes Villalba