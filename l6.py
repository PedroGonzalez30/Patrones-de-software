class ServicioExternoUsuario:
    def obtener_usuario(self):
        return {
            "name": "Clarita",
            "mail": "clarita@gmail.com",
            "age_years": 20
        }


class AdaptadorUsuario:
    def __init__(self, servicio_externo):
        self.servicio_externo = servicio_externo

    def obtener_usuario_estandar(self):
        datos = self.servicio_externo.obtener_usuario()
        return {
            "nombre": datos["name"],
            "correo": datos["mail"],
            "edad": datos["age_years"]
        }


class FachadaSistema:
    def __init__(self):
        self.adaptador = AdaptadorUsuario(ServicioExternoUsuario())

    def obtener_info_usuario(self):
        return self.adaptador.obtener_usuario_estandar()


import unittest

class TestAdaptador(unittest.TestCase):

    def test_adaptador_formatea_correcto(self):
        servicio = ServicioExternoUsuario()
        adaptador = AdaptadorUsuario(servicio)
        usuario = adaptador.obtener_usuario_estandar()
        self.assertEqual(usuario["nombre"], "Clarita")
        self.assertEqual(usuario["correo"], "clarita@gmail.com")
        self.assertEqual(usuario["edad"], 20)

    def test_fachada(self):
        sistema = FachadaSistema()
        usuario = sistema.obtener_info_usuario()
        self.assertIn("nombre", usuario)
        self.assertIn("correo", usuario)
        self.assertIn("edad", usuario)


if __name__ == "__main__":
    unittest.main()
