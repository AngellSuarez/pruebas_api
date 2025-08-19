from django.test import TestCase
from .models.usuario import Usuario
from rol.models import Rol
from django.core.exceptions import ValidationError

# Create your tests here.
class usuarioModelTest(TestCase):
    
    def test_crear_usuario(self):
        rol_data = {
            "nombre":"cliente",
            "descripcion":"prueba de rol"
        }
        
        rol = Rol.objects.create(**rol_data)
        
        datos_usuario = {
            "nombre":"lara samuel",
            "apellido":"henao",
            "correo":"prueba124@gmail.com",
            "tipo_documento":"CC",
            "numero_documento":"123456780",
            "rol_id":rol
        }
        usuario_agregado = Usuario.objects.create(**datos_usuario)
        
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(usuario_agregado.estado, "Activo")
        
    def test_usuario_tipo_documento_incorrecto(self):
        rol = Rol.objects.create(nombre="cliente", descripcion="prueba de rol")

        datos_usuario_invalido = {
            "nombre": "usuarioinvalido",
            "apellido": "apellidoinvalido",
            "correo": "invalido@gmail.com",
            "tipo_documento": "XYZ",
            "numero_documento": "987654321",
            "rol_id": rol
        }
        usuario_invalido = Usuario(**datos_usuario_invalido)
        
        with self.assertRaises(ValidationError):
            usuario_invalido.full_clean()

        self.assertEqual(Usuario.objects.count(), 0)
        
        
        
        