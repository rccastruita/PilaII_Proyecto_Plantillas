# env.py
# variables de entorno para el servidor
# actualmente solo se utiliza para actualizar la información de la versión actual

version = '0.2.1.0'
version_tag = f"V{version}"
version_title = f"Version {version}"

version_tooltip = '- TAREA -<br>Crear un proyecto Django con bd y templates'
version_description = 'Tarea: Crear un Proyecto Django con bd y templates'

changelog = {
    'V0.2.1.0': [
        'Modelos Producto y Sucursal agregados.',
        'Modelos Categoría, Presentación agregados.'
        'Vista Productos agregada.',
        'Vista Sucursales ahora es dinámica.',
        'Vista detalles Producto inicializada.',
        'Distintas mejoras a la interfaz de usuario.',
        'Pendiente refactorizar el código CSS.',
        'Base de datos cambiada de sqlite a PostgreSQL',
    ]
}