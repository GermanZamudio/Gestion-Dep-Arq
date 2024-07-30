# Administración de Depósito

## Descripción
Esta aplicación, desarrollada con Django, permite la administración eficiente de un depósito (pañol), incluyendo la gestión de inventarios de licitación/stock, registro de movimientos, novedades, y control de herramientas.

## Características
- **Inventario de Licitación/Stock**: Gestión y seguimiento de los bienes en stock y las licitaciones.
- **Registro de Movimientos**: Registro detallado de entradas y salidas de bienes.
- **Novedades**: Seguimiento de eventos importantes y novedades en el depósito.
- **Herramientas**: Inventario y control de herramientas utilizadas en el depósito.
- **Sistema de Login**: Acceso seguro con autenticación de usuario.

## Tecnologías Utilizadas
- **Backend**: Django
- **Base de Datos**: PostgreSQL (o la base de datos que estés utilizando)

## Instalación
Sigue estos pasos para instalar y ejecutar el proyecto localmente.

### Prerrequisitos
- Python y pip
- PostgreSQL (o la base de datos que estés utilizando)

### Instrucciones

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/deposito-admin.git
    cd deposito-admin
    ```

2. Configura el entorno virtual para Django:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias de Django:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura la base de datos PostgreSQL y actualiza `settings.py` con tus credenciales.

5. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

6. Crea un superusuario para acceder al sistema:
    ```sh
    python manage.py createsuperuser
    ```

7. Carga datos iniciales si tienes fixtures:
    ```sh
    python manage.py loaddata initial_data.json
    ```

8. Inicia el servidor de Django:
    ```sh
    python manage.py runserver
    ```

9. Accede a la aplicación en tu navegador en `http://localhost:8000` e inicia sesión con el superusuario creado.

## Uso
### Inventario de Licitación/Stock
- **Agregar bienes**: Navega a la sección "Inventario de Licitación/Stock" y usa el formulario para agregar nuevos bienes.
- **Actualizar stock**: Actualiza las cantidades de stock conforme ingresan o salen bienes.

### Registro de Movimientos
- **Registrar movimientos**: Ve a la sección "Registro de Movimientos" para registrar entradas y salidas de bienes del depósito.

### Novedades
- **Agregar novedades**: Añade y consulta novedades importantes relacionadas con el depósito.

### Herramientas
- **Inventario de herramientas**: Gestiona el inventario de herramientas disponibles.
- **Control de herramientas**: Lleva un control sobre la utilización y el estado de las herramientas.

## Contacto
German Zamudio - germanbenjamin@hotmail.com

## Enlace al Proyecto: [https://gestion-dep-arq.onrender.com/)
- ** Credenciales: 
  Usuario: test.user
  Contraseña: test
