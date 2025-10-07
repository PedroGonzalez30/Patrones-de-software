import unittest

class Command:
    def execute(self):
        pass


class Lampara:
    def __init__(self):
        self.encendida = False
        self.color = "blanco"

    def encender(self):
        self.encendida = True
        print("Lampara se encendio")

    def apagar(self):
        self.encendida = False
        print("Lampara se apago")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"lampara cambio a color {nuevo_color}")


class EncenderLampara(Command):
    def __init__(self, lampara):
        self.lampara = lampara

    def execute(self):
        self.lampara.encender()


class ApagarLampara(Command):
    def __init__(self, lampara):
        self.lampara = lampara

    def execute(self):
        self.lampara.apagar()


class CambiarColor(Command):
    def __init__(self, lampara, color):
        self.lampara = lampara
        self.color = color

    def execute(self):
        self.lampara.cambiar_color(self.color)


class Control:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def presionar_boton(self):
        if self.command:
            self.command.execute()


class TestPatron(unittest.TestCase):
    def setUp(self):
        self.lampara = Lampara()
        self.app = Control()

    def test_encender_lampara(self):
        cmd = EncenderLampara(self.lampara)
        self.app.set_command(cmd)
        self.app.presionar_boton()
        self.assertTrue(self.lampara.encendida)

    def test_apagar_lampara(self):
        self.lampara.encender()
        cmd = ApagarLampara(self.lampara)
        self.app.set_command(cmd)
        self.app.presionar_boton()
        self.assertFalse(self.lampara.encendida)

    def test_cambiar_color(self):
        cmd = CambiarColor(self.lampara, "azul")
        self.app.set_command(cmd)
        self.app.presionar_boton()
        self.assertEqual(self.lampara.color, "azul")


if __name__ == "__main__":
    unittest.main()
