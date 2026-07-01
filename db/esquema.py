from .db_conexion import conexion

with conexion() as conn:

    conn.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY UNIQUE AUTOINCREMENT,
            categoria TEXT NOT NULL UNIQUE,
        )
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY UNIQUE AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion,
            cantidad REAL,
            precio REAL,
            categoria_fk INTEGER,
            FOREIGN KEY (categoria_fk) REFERENCES categorias(id)   
        )
    ''')

    conn.commit()
        