# Documento de instalación


### 0. Programa para que podamos trabjar en remoto en la máquina de un operador.
Bajarse e instalar este programa.
[https://anydesk.es/download?os=win](https://anydesk.es/download?os=win)

Luego pasarle la dirección AnyDesk

Luego esperar para aceptar la entrada a su oedenador de forma remota de los técnicos.

### 1. Bajar e instalar python3
https://www.python.org/getit/

En win configurar las variables de entorno: 

* PYTHON_HOME
* PATH

### 2. Bajar e instalar el driver de chrome 
https://sites.google.com/a/chromium.org/chromedriver/downloads

### 3. Instalar pip 

3.1 Win

python -m pip install -U pip

https://bootstrap.pypa.io/get-pip.py



### 4. Bajar los archivos fuentes
Dirección donde están los fuente: [Link fuentes](https://drive.google.com/open?id=133ZpgI7VegnoULgyoF7wMEf4RsqxWPdB)

* scrapOK2.py
* getionDialogo.py
* contactos.txt
* crhomedriver.exe (el que bajaron en el punto 2)
* Requerimientos.txt


### 5. Instalar las dependencias 
pip install -r Requirementos.txt


### 6. Ejecutar el programa
python scrapOk2.py
