from abc import ABC, abstractmethod
import unittest

class ImageProcessor(ABC):
    def process_image(self):
        self.load_image()
        self.apply_filter()
        self.save_result()

    @abstractmethod
    def load_image(self):
        pass

    @abstractmethod
    def apply_filter(self):
        pass

    def save_result(self):
        print("Guardando imagen procesada en el disco...")

class JPGProcessor(ImageProcessor):
    def load_image(self):
        print("Cargando imagen JPG...")

    def apply_filter(self):
        print("Aplicando filtro de nitidez a JPG...")

class PNGProcessor(ImageProcessor):
    def load_image(self):
        print("Cargando imagen PNG...")

    def apply_filter(self):
        print("Aplicando filtro de color a PNG...")

class TestImageProcessor(unittest.TestCase):
    def test_jpg_processor(self):
        jpg = JPGProcessor()
        try:
            jpg.process_image()
        except Exception as e:
            self.fail(f"JPGProcessor lanzo una excepcion: {e}")

    def test_png_processor(self):
        png = PNGProcessor()
        try:
            png.process_image()
        except Exception as e:
            self.fail(f"PNGProcessor lanzo una excepcion: {e}")

    def test_is_subclass(self):
        self.assertTrue(issubclass(JPGProcessor, ImageProcessor))
        self.assertTrue(issubclass(PNGProcessor, ImageProcessor))

    def test_abstract_methods(self):
        self.assertTrue(callable(JPGProcessor().load_image))
        self.assertTrue(callable(JPGProcessor().apply_filter))
        self.assertTrue(callable(PNGProcessor().load_image))
        self.assertTrue(callable(PNGProcessor().apply_filter))

if __name__ == "__main__":
    jpg = JPGProcessor()
    png = PNGProcessor()

    print("Procesando imagen JPG:")
    jpg.process_image()

    print("\nProcesando imagen PNG:")
    png.process_image()

    print("\nEjecutando pruebas unitarias...\n")
    resultado = unittest.main(exit=False)
    if resultado.result.wasSuccessful():
        print("\nTodas las pruebas unitarias se ejecutaron correctamente.")
    else:
        print("\nAlgunas pruebas fallaron. Revisa los detalles arriba.")
