from abc import ABC, abstractmethod

class subject(ABC):
    @abstractmethod
    def add_observer(self, observer: "Observer"):
        pass

    @abstractmethod
    def remove_observer(self, observer: "Observer"):
        pass

    @abstractmethod
    def notify_observers(self, message: str):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, mensaje: str):
        pass


# --- Sujeto concreto (Subasta) ---
class Subastador(subject):
    def __init__(self, articulo: str, precio_inicial: float):
        self._observers: list[Observer] = []
        self.articulo = articulo
        self.precio_actual = precio_inicial
        self.mejor_postor = None
        self.activa = True  

    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self._observers:
            observer.update(message)

    def ofertar(self, postor: "Postor", cantidad: float):
        if not self.activa:
            postor.update(f"La subasta por {self.articulo} ya termino. No se aceptan mas ofertas.")
            return

        if cantidad > self.precio_actual:
            self.precio_actual = cantidad
            self.mejor_postor = postor
            self.notify_observers(f"Nueva oferta: {postor.nombre} ofrecio ${cantidad} por {self.articulo}")
        else:
            postor.update(f"Tu oferta de ${cantidad} es menor que la actual ( ${self.precio_actual} )")

    def cerrar_subasta(self):
        self.activa = False
        if self.mejor_postor:
            self.notify_observers(
                f"La subasta termino. Ganador es {self.mejor_postor.nombre} "
                f"con una oferta de ${self.precio_actual} por {self.articulo}")
        else:
            self.notify_observers(f"La subasta termino. Nadie oferto por {self.articulo}.")


class Postor(Observer):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def update(self, mensaje: str):
        print(f"[ {self.nombre} ] notificacion: {mensaje}")


if __name__ == "__main__":
    subastador = Subastador("Patito de oro", 1000)

    postor1 = Postor("Carlos")
    postor2 = Postor("Garibay")
    postor3 = Postor("Mario")

    subastador.add_observer(postor1)
    subastador.add_observer(postor2)
    subastador.add_observer(postor3)

    subastador.ofertar(postor1, 1200)
    subastador.ofertar(postor2, 1500)
    subastador.ofertar(postor3, 1400)  
    subastador.ofertar(postor1, 2000)

    subastador.cerrar_subasta()

    subastador.ofertar(postor3, 2500)
