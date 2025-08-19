# usuario/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from usuario.models.usuario import Usuario
from rol.models import Rol
from usuario.models.cliente import Cliente
import json

# Create your tests here.
class RegistroClienteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.rol_cliente = Rol.objects.create(nombre='cliente', descripcion='Rol para clientes')
        self.url = reverse('register_cliente')

    def test_registro_exitoso(self):
        data = {
            "username": "nuevo_cliente",
            "nombre": "Nuevo",
            "apellido": "Cliente",
            "correo": "nuevo.cliente@gmail.com",
            "tipo_documento": "CC",
            "numero_documento": "987654321",
            "password": "mi_password_segura",
            "celular": "3111234567"
        }
        
        response = self.client.post(self.url, data=json.dumps(data), content_type="application/json")
        
        self.assertEqual(response.status_code, 201)
        self.assertIn('tokens', response.json())
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Usuario.objects.count(), 1)
        
    def test_registro_con_datos_faltantes(self):

        data = {
            "nombre": "Incompleto",
            "apellido": "Test"
        }
        
        response = self.client.post(self.url, data=json.dumps(data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('correo', response.json())