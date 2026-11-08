TiendaPy
Sistema de gestión para una tienda de barrio desarrollado en Python.

Funcionalidades
Gestión de Inventario
Registrar productos
Consultar productos
Buscar por código
Buscar por categoría
Modificar productos
Eliminar productos
Listar inventario completo

Gestión de Ventas
Registro de ventas
Carrito de compras
Control de stock
Cálculo automático de descuentos
Cálculo de cambio

Reportes
Alertas de stock bajo
Productos agotados
Reporte de cierre del día
Ticket promedio
Producto más vendido

Persistencia
Inventario almacenado en inventario.txt
Ventas almacenadas en ventas.txt

Estructura del Proyecto
TiendaPy/

README.md

requirements.txt

data/ inventario.txt ventas.txt

src/ main.py inventario.py ventas.py reportes.py persistencia.py validaciones.py

Requisitos
Python 3.10 o superior

Instalar dependencias:

pip install -r requirements.txt

Ejecución
Ubicarse dentro de la carpeta raíz:

python src/main.py

Formato de Inventario
codigo|nombre|categoria|precio|stock|stock_minimo|proveedor

Ejemplo:

LAC001|Leche Entera 1L|Lacteos|4200|35|10|Alqueria

Formato de Ventas
fecha|total|codigo:cantidad;codigo:cantidad

Ejemplo:

2026-11-02|18400|LAC001:2;BEB001:1

Tecnologías Utilizadas
Python
pathlib
tabulate
Archivos TXT
Programación Modular
Manejo de Excepciones

Autor
Paola Reyes Villalba