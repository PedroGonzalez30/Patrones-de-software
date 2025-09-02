
from abc import ABC, abstractmethod
import random

opciones = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]


class Pay_Limon(ABC):
    @abstractmethod
    def precio(self):
        pass


class Rebanada(Pay_Limon):
    def precio(self):
        return 25  
 

class PayDecorador(Pay_Limon):
    def __init__(self, pay):
        self._pay = pay  

    def precio(self):
        return self._pay.precio()


class MedioPay(PayDecorador):
    def precio(self):
        return self._pay.precio() + 25


class PayCompleto(PayDecorador):
    def precio(self):
        return self._pay.precio() + 50


class Descuento(PayDecorador):
    def precio(self):
        return (self._pay.precio()) 


if __name__ == "__main__":

    op = random.choice(opciones)
    pay = Rebanada()
    pay_rebanada = MedioPay(pay)
    pay_completo = PayCompleto(MedioPay(pay))
    pay_descuento = Descuento(PayCompleto(pay))

    print("** Pasteleria el chuy **")
    print("Hoy es: ", op)
    if(op == 'Jueves'):
        print("Hoy descuento en la compra de pay completo")

    print("Rebanada de Pay de limon: $", pay.precio())

    print("Medio Pay de limon: $", pay_rebanada.precio())

    if(op == 'Jueves'):
        print("Precio Original: $", pay_completo.precio(), 
          " | Precio con descuento: $", pay_descuento.precio())
    else:
        print("Pay de limon completo: $", pay_completo.precio()) 
        