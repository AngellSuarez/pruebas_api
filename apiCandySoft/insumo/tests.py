from django.test import TestCase
from insumo.models import Marca, Insumo

# Create your tests here.
class InsumoModelTest(TestCase):
    
    def test_crear_marca(self):
        nombre_marca = "marca prueba 23"
        
        marca = Marca.objects.create(nombre = nombre_marca)
        
        self.assertEqual(Marca.objects.count(), 1)
        self.assertEqual(marca.nombre, nombre_marca)
        self.assertEqual(str(marca), nombre_marca)
        
    def test_crear_insumo(self):
        nombre_marca = "Marca de prueba"
        marca = Marca.objects.create(nombre=nombre_marca)

        datos_insumo = {
            "nombre": "Lima de uñas",
            "stock": 10,
            "marca_id": marca
        }
        # se usa ** para pasar el diccionario como argumentos de palabra clave.
        insumo = Insumo.objects.create(**datos_insumo)

        self.assertEqual(Insumo.objects.count(), 1)
        
        # comprobar que el estado se haya actualizado a 'activo'
        self.assertEqual(insumo.estado, "Activo")
        
    def test_insumo_estado_bajo(self):
        marca = Marca.objects.create(nombre="Marca de prueba")
        
        # Crea un insumo con stock bajo
        insumo = Insumo.objects.create(
            nombre="Algodón",
            stock=5,
            marca_id=marca
        )
        
        # comprobar que el estado se haya actualizado a 'Bajo'
        self.assertEqual(insumo.estado, "Bajo")
        
    def test_insumo_estado_agotado(self):
        marca = Marca.objects.create(nombre="Marca de prueba")
        
        insumo = Insumo.objects.create(
            nombre="Gel para uñas",
            stock=0,
            marca_id=marca
        )
        
        # comprobar que el estado se haya actualizado a 'Agotado'
        self.assertEqual(insumo.estado, "Agotado")