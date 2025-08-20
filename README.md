# CandySoft

# Tabla de contenido
- Descripción del proyecto
- Tecnologias
- Funciones
- Configuración y Ejecución
- Test realizados
- Autores
# Descripción del proyecto
El backend de **Candy Soft** está desarrollado en **Python con Django REST Framework (DRF)** y proporciona la API que gestiona los procesos principales del negocio **Candy Nails Spa**.

# Tecnologías
- **Django** + **Django REST Framework** para la API.
- **MySQL** como base de datos relacional.
- **JWT** para autenticación y protección de rutas.

# Funciones
### Funcionalidades principales

- Gestión de usuarios y administrativos.  
- Gestión de roles y permisos.  
- Gestión de compras.  
- Gestión de insumos.  
- Gestión de abastecimientos y su reporte.  
- Gestión de asignación de citas y creación de ventas.  
- Gestión de servicios.  
- Gestión de clientes y manicuristas.  
- Gestión de liquidaciones hacia las manicuristas.  
- Visualización de indicadores de negocio.  
- Funciones de acceso y manejo de sesiones.  

# Configuración y ejecución 

### 🔑 Requerimientos previos
asegúrate de tener instalado en tu sistema:

- **Python 3.11+**
- **MySQL 8+** (con una base de datos creada para Candy Soft, puede usarse el .sql del repositorio)
- **pip** (gestor de paquetes de Python)
- **virtualenv** (recomendado para entornos virtuales)
- **Git** (para clonar el repositorio)
---

### 1. Clonar el repositorio
```bash
git clone https://github.com/AngellSuarez/pruebas_api.git
cd ApiCandyModularizada-main-segura
```

### 2.Crear y activar el entorno virtual
Linux y MacOs
```bash
python3 -m venv "nombre de tu entorno"
source ./venv/bin/activate
```
windows
```bash
python -m venv "nombre de tu entorno"
venv\Scripts\activate
```

### 3.Instalar las dependencias
```bash
pip install -r requirements.txt
```
### 4. Crear la base de datos
Ejecuta el script para crear la base de datos que se encuentra en la carpeta, o hazlo desde consola con los siguientes pasos
#### - inicia la consola de mysql en terminal
```bash
mysql -u "tu usuario" -p #ingresa tu contraseña luego de esto
```
#### - Ingresa el comando para crear la base de datos
```bash
CREATE DATABASE CandySoftApi2;
```

### 5.Crea tus variables de entorno
primero ingresa a la sub carpeta apiCandySoft
```bash
cd apiCandySoft
```
El proyecto utiliza un archivo `.env` para centralizar la configuración sensible (claves, contraseñas y accesos).

Aquí lo que debe contener el archivo:

#### - Seguridad
```bash
SECRET_KEY=tu_clave_secreta_generada_por_django  
DEBUG=True
```
para generar una nueva clave secreta de django en tu terminal escribe el siguiente comando, y copia el resultado en tu variable
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
#### - Base de datos
Asegúrate de que MySQL esté corriendo y que la base de datos exista antes de aplicar migraciones.
```
DB_ENGINE=django.db.backends.mysql  
DB_NAME=CandySoftApi2  
DB_USER=usuario  
DB_PASSWORD=contraseña  
DB_HOST=localhost  
DB_PORT=3306
```
#### - Correo
```
EMAIL_HOST=smtp.gmail.com  
EMAIL_PORT=587  
EMAIL_USE_TLS=True  
EMAIL_HOST_USER=tu_correo@gmail.com  
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
```

#### - Api externa subida de imagenes (ImgBB)
Es necesario crear una cuenta gratuita en ImgBB para obtener un `API_KEY`, que se utiliza para la gestión de imágenes en los servicios.
```
IMGBB_API_KEY=tu_api_key_imgbb
```
### 6. Aplicar las migraciones
dentro de la sub carpeta apiCandysoft aplica los siguientes comandos en la terminal
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Ejecuta el servidor de desarrollo
en tu terminal ingresa el comando
```bash
python manage.py runserver
```
haciendo disponible la api bajo la ruta desde tu navegador
http://127.0.0.1:8000/

# Test realizados
los test realizados fueron hacia los siguientes modulos y sus clases:
	- insumo -- > marca , insumo
	- servicio -- > servicio
	- usuario -- > usuario junto con la creación de un rol asociado
	- authRecuperacion -- > ruta completa de creación de un rol, permiso, asignar el permiso al rol, crear un usuario con dicho rol, hacer login y por ultimo crear un insumo usando el token que fue recibido en la respuesta de login.

#### - Como realizar los test
Para realizar los test se necesita estar en la carpeta con que cuenta con el archivo manage.py, este se encuentra dentro de apiCandySoft
```bash
cd apiCandySoft
#hacemos ls para verificar que dentro de la carpeta luzca algo asi
ls
abastecimiento  apiCandySoft  authrecuperacion  calificacion  cita  compra  insumo  manage.py  manicurista  proveedor  rol  servicio  usuario  utils
```
Dentro de la carpeta se procede a realizar el siguiente comando para empezar las pruebas
```bash
python manage.py test
```
lo cual va a empezar a buscar todos los test dentro del proyecto y ejecutarlos dando por resultado en la terminal algo como esto, donde cada punto (.) simboliza el funcionamiento correcto de cada test:
```bash
Found 9 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.........
----------------------------------------------------------------------
Ran 9 tests in 1.792s

OK
Destroying test database for alias 'default'...
```
# Autores
**Aprendiz:** Miguel Ángel Cardona Suárez
**Ficha:** 2901665
**Proyecto:** CandySoft