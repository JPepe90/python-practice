# Instalacion de un entorno profesional de Python en WSL

```sh
sudo apt update
```

Upgrade:

```sh
sudo apt -y upgrade
```

Con esto ya tenemos python3 instalado y actualizado.

### Instalacion de gestor de paquetes (pip)

```sh
sudo apt install -y python3-pip
```

Para verificar la version de pip:

```sh
pip3 -V
```

### Otras dependencias de un entorno profesional

```sh
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

# Instrucciones para correr el Juego

```sh
cd game
python3 main.py
```