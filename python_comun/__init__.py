"""
Python_Comun - Librería de funciones comunes

NOTA: Para rehacer toda la estructura de librerías en la aplicación,
se puede eliminar todo y volver a crearlo:

Desde un terminal, estando con el entorno activo:
$ source .venv/bin/activate
Hacemos:

Si queremos utilizar la librería en modo edición, vamos al archivo project.toml, y en la
entrada de la librería, hay que poner editable=true. Por ejemplo:

python-xml = { path = "../../Python_XML", editable=true }

Si queremos que la librería se la descargue de github (proyecto público), en el toml hay que
poner:

python-xml = { git = "https://github.com/pedrogil1919/Python_XML.git" }

Sin embargo, en general para que los cambios tengan efecto, suele ser necesearioo borrar todo
y volver a crearlo. Desde un terminal en el directorio donde está el toml:

$ deactivate
$ rm -rf .venv
$ python3 -m venv .venv
Y volvemos a activar el entorno virtual:
$ source .venv/bin/activate
# Borrar todo y volver a crearlo.
$ rm uv.lock
$ uv lock
$ uv sync


"""
from python_comun.funciones_comunes import *
from python_comun.ventana_inicio import *
from python_comun.formulario_seleccion import *

__all__ = []
