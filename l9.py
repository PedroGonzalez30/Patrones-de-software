import time
import unittest


class ImagenReal:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.cargar_disco()

    def cargar_disco(self):

        print(f"Cargando imagen {self.nombre_archivo} desde disco...")
        time.sleep(1)

    def mostrar(self):
        return f"Mostrando imagen {self.nombre_archivo}"


class ProxyImagen:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.imagen_real = None  

    def mostrar(self):
        if self.imagen_real is None:
            self.imagen_real = ImagenReal(self.nombre_archivo)
        return self.imagen_real.mostrar()


class ProxyControlAcceso:
    def __init__(self, usuario, nombre_archivo):
        self.usuario = usuario
        self.proxy_virtual = ProxyImagen(nombre_archivo)

    def mostrar(self):
        # Solo el admin puede mostrar imagenes
        if self.usuario == "admin":
            return self.proxy_virtual.mostrar()
        else:
            return "Acceso denegado. Solo el administrador puede ver las imagenes."


class TestProxyImagen(unittest.TestCase):

    # Prueba de carga de imagen cuando se necesite
    def test_carga_diferida(self):
        proxy = ProxyImagen("foto.jpg")
        self.assertIsNone(proxy.imagen_real)  
        proxy.mostrar()  
        self.assertIsNotNone(proxy.imagen_real)  

    # Prueba solo admin
    def test_acceso_admin(self):

        proxy = ProxyControlAcceso("admin", "foto.jpg")
        resultado = proxy.mostrar()
        self.assertEqual(resultado, "Mostrando imagen foto.jpg")

    # preuba a usuario
    def test_acceso_denegado(self):
        proxy = ProxyControlAcceso("invitado", "foto.jpg")
        resultado = proxy.mostrar()
        self.assertEqual(resultado, "Acceso denegado. Solo el administrador puede ver las imagenes.")


if __name__ == "__main__":
    unittest.main()
