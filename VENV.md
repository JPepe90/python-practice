# Entornos virtuales
Los entornos virtuales sirven para asociar las dependencias de modulos especificos correspondientes a cada proyecto cuando requieren versiones especificas que no son las globales. De esta forma podemos utilizar modulos especificos para un determinado proyecto que solo funcionará para ese entorno virtual.

## Instalacion de entornos virtuales
Para verificar donde se esta ejecutando python3:

```sh
which python3
```

Para verificar donde se esta ejecutando pip3:

```sh
which pip3
```

En Linux o WSL debemos instalar el paquete venv:

```sh
sudo apt install -y python3-venv
```

Para crear un ambiente virtual debo entrar a la carpeta que quiero virtualizar, en este caso haremos la carpeta charts y creamos el venv con el nombre que querramos, en este caso charts-env y lo activamos:

```sh
cd charts
python3 -m venv charts-env
source charts-env/bin/activate
```

En la consola saldrá el indicador de que el entorno ha sido activado:

```
(charts-env) jpepe@DESKTOP-FPETKI1:~/py_projects/python-practice/charts$
```

Con el ambiente virtual activado, podemos utilizar las instrucciones which para verificar que python3 y pip3 esten funcionando desde la ruta de nuestro entorno virtual.

En el caso de este proyecto unicamente voy a instalar matplotlib:

```sh
pip3 install matplotlib
```

Para desactivar el ambiente utilizamos la instruccion:

```sh
deactivate
```

Luego paso a la carpeta del juego y creo un nuevo ambiente virtual llamado game-env, lo activo e instalo matplotlib en la version 3.5.0:

```sh
cd ..
cd game
python3 -m venv game-env
source game-env/bin/activate
pip3 install matplotlib==3.5.0
```

Verifico la version instalada con 

```sh
pip3 freeze
```

## Guardar dependencias a requirements.txt
Para generar un archivo txt de dependencias automaticas, estando en el entorno virtual que deseamos guardar ejecutamos el siguiente comando en la terminal:

```sh
pip3 freeze > requirements.txt
```

Utilizando este archivo txt, podemos instalar todas estas dependencias de una sola vez con el siguiente comando en la terminal:

```sh
pip3 install -r requirements.txt
```