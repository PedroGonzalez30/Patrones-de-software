from abc import ABC, abstractmethod
import unittest


class State(ABC):
    @abstractmethod
    def power(self, remote):
        pass

    @abstractmethod
    def mute(self, remote):
        pass

    @abstractmethod
    def volumen_up(self, remote):
        pass

    @abstractmethod
    def volumen_down(self, remote):
        pass


class Estado_ON(State):
    def power(self, remote):
        print("Apagando la TV")
        remote.set_state(Estado_OFF())

    def mute(self, remote):
        print("Silenciando la TV")
        remote.set_state(Estado_MUTE())

    def volumen_up(self, remote):
        remote.volume = min(100, remote.volume + 5)
        print(f"Subiendo volumen: {remote.volume}")

    def volumen_down(self, remote):
        remote.volume = max(0, remote.volume - 5)
        print(f"Bajando volumen: {remote.volume}")


class Estado_OFF(State):
    def power(self, remote):
        print("Encendiendo la TV")
        remote.set_state(Estado_ON())

    def mute(self, remote):
        print("No se puede silenciar, la TV esta apagada")

    def volumen_up(self, remote):
        print("No se puede subir volumen, la TV esta apagada")

    def volumen_down(self, remote):
        print("No se puede bajar volumen, la TV esta apagada")


class Estado_MUTE(State):
    def power(self, remote):
        print("Apagando la TV desde silencio")
        remote.set_state(Estado_OFF())

    def mute(self, remote):
        print("Desactivando silencio")
        remote.set_state(Estado_ON())

    def volumen_up(self, remote):
        print("Subiendo volumen y desactivando silencio")
        remote.set_state(Estado_ON())
        remote.volume = min(100, remote.volume + 5)

    def volumen_down(self, remote):
        print("Bajando volumen y desactivando silencio")
        remote.set_state(Estado_ON())
        remote.volume = max(0, remote.volume - 5)


class ControlRemoto:
    def __init__(self):
        self.state = Estado_OFF()
        self.volume = 20

    def set_state(self, state):
        self.state = state

    def power(self):
        self.state.power(self)

    def mute(self):
        self.state.mute(self)

    def volume_up(self):
        self.state.volumen_up(self)

    def volume_down(self):
        self.state.volumen_down(self)


#Test
class TestControlRemoto(unittest.TestCase):
    def setUp(self):
        self.remote = ControlRemoto()

    def test_power_on(self):
        self.remote.power()
        self.assertIsInstance(self.remote.state, Estado_ON)

    def test_volumen_up_on(self):
        self.remote.power()
        old_volume = self.remote.volume
        self.remote.volume_up()
        self.assertGreater(self.remote.volume, old_volume)

    def test_mute_on(self):
        self.remote.power()
        self.remote.mute()
        self.assertIsInstance(self.remote.state, Estado_MUTE)

    def test_unmute(self):
        self.remote.power()
        self.remote.mute()
        self.remote.mute()
        self.assertIsInstance(self.remote.state, Estado_ON)

    def test_power_off(self):
        self.remote.power()
        self.remote.power()
        self.assertIsInstance(self.remote.state, Estado_OFF)

    def test_volume_cambiar_muted(self):
        self.remote.power()
        self.remote.mute()
        self.remote.volume_up()
        self.assertIsInstance(self.remote.state, Estado_ON)

    def test_volumen_mientras_off(self):
        self.remote.volume_up()
        self.assertEqual(self.remote.volume, 20)


if __name__ == "__main__":
    unittest.main()
