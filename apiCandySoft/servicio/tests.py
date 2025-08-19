from django.test import TestCase
from servicio.models import Servicio
from datetime import timedelta
from django.core.exceptions import ValidationError
# Create your tests here.
class Test_servicio(TestCase):
    
    #setup de los datos 
    def setUp(self):
        
        self.data_valida_servicio = {
            'nombre':'Servicio prueba',
            'descripcion':'soy una prueba pa probar',
            'estado': 'Activo',
            'tipo':'manicure',
            'url_imagen':'http://soyunaurl.com/soyunaimagen.jpg',
            'precio':20000,
            'duracion': timedelta(minutes=70)
        }
        
    def test_crear_servicio(self):
        
        servicio = Servicio.objects.create(**self.data_valida_servicio)
        
        self.assertEqual(Servicio.objects.count(),1)
        self.assertEqual(servicio.nombre, 'Servicio prueba')
        self.assertEqual(servicio.estado, 'Activo')
        
    def test_data_invalida_crear(self):
        
        data_invalida = self.data_valida_servicio.copy()
        data_invalida['tipo'] = 'tontolon'
        
        with self.assertRaises(ValidationError):
            servicio = Servicio(**data_invalida)
            servicio.full_clean()