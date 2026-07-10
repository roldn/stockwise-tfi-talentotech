from db.esquema import inicializar_db
from db.datos_iniciales import cargar_datos_iniciales
from ui.app import App

if __name__ == "__main__":
    inicializar_db()
    cargar_datos_iniciales()
    app = App()
    app.mainloop()
