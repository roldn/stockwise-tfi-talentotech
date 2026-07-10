from db.db_conexion import conexion

def cargar_datos_iniciales() -> None:
    with conexion() as conn:

        # Verificar si ya hay datos — no insertar si la tabla ya tiene registros
        if conn.execute("SELECT COUNT(*) FROM categorias").fetchone()[0] > 0:
            return

        categorias = [
            ("Muebles",),
            ("Electrónica",),
            ("Librería",),
            ("Limpieza",),
            ("Indumentaria",),
        ]
        conn.executemany(
            "INSERT INTO categorias (nombre) VALUES (?)",
            categorias
        )

        productos = [
            ("Silla ejecutiva",     "Silla de oficina con ruedas",  10, 150.00, 1),
            ("Mesa de escritorio",  "Mesa de madera 1.20m",          5, 320.00, 1),
            ("Monitor 24 pulgadas", "Monitor Full HD",                8, 280.00, 2),
            ("Teclado inalámbrico", "Teclado bluetooth",             15,  45.00, 2),
            ("Resma A4",            "500 hojas 75g",                 50,   8.50, 3),
            ("Birome azul x10",     "Pack de 10 biromes",            30,   3.20, 3),
            ("Lavandina 1L",        "Lavandina concentrada",         20,   2.50, 4),
            ("Remera básica",       "Remera algodón talle M",        25,  12.00, 5),
        ]
        conn.executemany(
            """INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria_id)
               VALUES (?, ?, ?, ?, ?)""",
            productos
        )
