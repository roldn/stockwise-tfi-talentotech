from db.db_conexion import conexion

def inicializar_db() -> None:
    with conexion() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                descripcion TEXT
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER,
                precio REAL,
                categoria_id INTEGER,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id)   
            )
        ''')
            
