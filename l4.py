class Configuracion:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Configuracion, cls).__new__(cls)
            cls.__instance.parametros = {
                "API_KEY": "12345-ABCDE",
                "URL": "https://api.ejemplo.com"
            }
            print("Nueva instancia de Configuracion creada")
        return cls.__instance

    def get(self, clave):
        return self.parametros.get(clave, None)


class ConexionDB:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ConexionDB, cls).__new__(cls)
            cls.__instance.conectado = False
            cls.__instance.db_url = "localhost:5432/mi_db"
            print("Objeto ConexionDB creado")
        return cls.__instance

    def conectar(self): #simula la apertura de una conexion
        if not self.conectado:
            print(f"Conectando a {self.db_url}")
            self.conectado = True
        else:
            print("Ya existe una conexion activa")

    def query(self, sql): #simula la ejecucion
        if self.conectado:
            print(f"Ejecutando: {sql}")
        else:
            print("No hay conexion activa")


if __name__ == "__main__":
    c1 = Configuracion()
    c2 = Configuracion()
    print("¿Son la misma configuracion?", c1 is c2)
    print("API_KEY:", c1.get("API_KEY"))

    db1 = ConexionDB()
    db2 = ConexionDB()
    print("¿Son la misma conexion?", db1 is db2)
    db1.conectar()
    db2.conectar()
