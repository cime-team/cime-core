# Instalación y Ejecución

> :warning: **Atención:**  
>
>Este proceso de instalación asume que tu sistema tiene instalado `Python
3.6.0` o superior. Puedes asegurarte que tu versión es apropiada ejecutando
`python3 --version`. Si entrega un error, no tienes instalado Python 3. [Descárgalo aquí.](https://www.python.org/downloads/)

#### macOS/Linux/WSL

    git clone git@github.com:cime-team/cime-core.git
    cd cime-core
    python3 -m venv .
    source ./bin/activate
    pip install -r requirements.pip
    mv .env.ejemplo .env
    ./manage.py migrate

#### Windows

En Windows 10 se **recomienda** utilizar WSL o alguna otra capa de emulación de
UNIX, como [Git BASH](https://git-for-windows.github.io/) o
[Cygwin](https://www.cygwin.com/) y utilizar las mismas instrucciones que para
Linux. Si eres de esos desarrolladores que nada los separará de Windows 7,
asegurate que `git` y `python3` estén en tu `PATH`, y sigue estas instrucciones:

    git clone git@github.com:cime-team/cime-core.git
    dir cime-core
    python3 -m venv .
    .\Scripts\activate.bat
    pip install -r requirements.pip
    copy ".\.env.ejemplo" ".\.env"
    .\manage.py migrate

Esto instalará el entorno virtual para la aplicación y sus dependencias,
asegurando que tus dependencias de Python no se mezclen con las de tu sistema.
También creará una base de datos de desarrollo en formato sqlite en el mismo
directorio.

Cuando termines tu trabajo y quieras desactivarlo, puedes ejecutar:

    deactivate #macOS/Linux
    .\Scripts\deactivate.bat #Windows

## Ejecución del servidor de desarrollo

Con el entorno virtual activo, es cosa de ejecutar:

    ./manage.py runserver
