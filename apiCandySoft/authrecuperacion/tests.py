# insumo/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from usuario.models.usuario import Usuario
from rol.models import Rol, Permiso, Permiso_Rol
from insumo.models import Insumo, Marca

class InsumoAPITestCase(APITestCase):

    def setUp(self):
        # usuario y rol pa autenticar
        self.rol_admin = Rol.objects.create(nombre='Admin', descripcion='Rol para administradores')
        self.permiso_insumo = Permiso.objects.create(modulo='Insumo')
        self.rol_permiso_contiene = Permiso_Rol.objects.create(rol_id = self.rol_admin, permiso_id = self.permiso_insumo)
        
        self.user = Usuario.objects.create_user(
            username='testadmin', 
            password='testpassword123', 
            rol_id=self.rol_admin,
            nombre='Admin',
            apellido='Test',
            correo='admin@example.com',
            tipo_documento='CC',
            numero_documento='123456789'
        )
        
        # crear una marca ahi toda breve pal insumo
        self.marca = Marca.objects.create(nombre='TestMarca')
        
        # URLs  Insumo API 
        self.list_create_url = reverse('insumos-list') 
        
    #conseguir los tokens    
    def _get_auth_token(self):
        login_data = {
            'username': 'admin@example.com', 
            'password': 'testpassword123'
        }
        response = self.client.post(reverse('token_obtain_pair'), login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']
    
    def test_create_insumo(self):
        token = self._get_auth_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        data = {
            'nombre': 'Lima',
            'stock': 10,
            'marca_id': self.marca.id,
        }
        
        response = self.client.post(self.list_create_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Insumo.objects.count(), 1)
        self.assertEqual(Insumo.objects.get().nombre, 'Lima')