
# Calculadora

Este proyecto es una calculadora hecha en python, contiene operadores matematicos basicos como son: 

suma
resta
multiplicacion
division

## ¿Como correr el workflow local?

Para correr el workflow de github actions en nuestro dispositivo, usamos una herramienta que se llama act el cual sirve para simular los workflows de github pero en local

## ¿Como funciona act?

Act es una herramienta que nos deja correr los workflows de GitHub Actions en nuestra propia computadora. Cuando usamos act este se encarga de hacer lo mismo que haria GitHub, pero sin tener que subir nada. Usa Docker para crear un entorno parecido al de GitHub y asi podemos ver si todo funciona bien antes de subir los cambios. Si algo falla, nos muestra los errores igual que en GitHub.

### Requisitos

1. tener instalado Docker (puedes buscar tutorial en el youtube)
2. tener instalado act (puedes buscar tutorial en el youtube)
3. Instalamos las dependencias del proyecto colocando en la consola:
	
	pip install -r requirements.txt
	

### Comando para correr


para correr el workflow colocamos esto en la consola:

    act -j build


### Paso a paso para ejecutar el pipeline

1. Abrimos la terminal en la carpeta del proyecto
2. Nos aseguramos que tenemos Docker y act instalados
3. Instalamos las dependencias con pip install -r requirements.txt
4. Ejecutamos el comando act -j build
5. Miramos los logs, si todo sale bien el pipeline termina y dice que todo ok. Si hay error, nos dice donde fallo (linter, pruebas o cobertura)

## ¿Como funciona el pipeline?

El pipeline es como una serie de pasos que revisan el codigo cada vez que subimos algo o hacemos un pull request. Primero revisa el estilo con flake8 (linter), luego "build" (en python solo es un paso de prueba), despues corre las pruebas y revisa que la cobertura sea suficiente (80%). Si algo falla, el pipeline se para y nos dice el error. Si todo pasa, termina y sale en verde.

