from .db_conexion import conexion

with conexion() as conn:

    conn.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY UNIQUE AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            descripcion TEXT
        )
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY UNIQUE AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion,
            cantidad REAL,
            precio REAL,
            categoria_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)   
        )
    ''')

    conn.commit()
        
