# webempresarial
_Ejemplo una ampliación web para restaurantes con Django en la cual se puede realizar las siguientes acciones._
* Crear nuevos platillos desde el administrador.
* Enviar un correo desde el servidor de prueba mailtrap.
* Agregar nuevas publicaciones en la sección de blog.
* Secciones dinámicas para mostrar política, cookies, aviso legal de forma dinámica cargados desde panel de * administración.

## Requerimientos de configuración

### Configuraciones extra para hacer funcionar él envió de correo.
* Crear una cuenta en mailtrap https://mailtrap.io/.
* Una vez que se tiene la cuenta:
* Accedemos a la configuración de la cuenta de email.
* Seleccionamos el lenguaje y copiamos la configuración para colocarla al final del archivo webempresarial/settings.py 
    ```
    # Configuracion email
    EMAIL_HOST = 'smtp.mailtrap.io'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''

    ```
* También será necesario modificar el archivo contact/view.py para agregar un correo de destino.
    ```
    mail = EmailMessage(
                    "La Sabrosa: Nuevo mensaje de contacto", #Asunto
                    "De {} {}\n\nEscribió:\n\n{}".format(name, mail, content), #Mensaje
                    "lasabrosa.com", #Email de Origen
                    ["correo_prueba@email.com"], #Email de destino
                    reply_to=[mail]
                )
    ```
> Nota: En esta sección se puede configurar cualquier otro servidor de correo.

### Requerimientos para compilar el proyecto
* Crea un ambiente virtual.
    ```
    py -m venv env
    o
    virtualenv env
    ```
* Instalar librerías necesarias
    ```
    pip install -r requirements.txt
    ```
## Compilar aplicación.
```
py manage.py runserver
```