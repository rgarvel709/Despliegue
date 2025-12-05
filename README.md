1. Herramienta usada para generar documentación HTML
Herramienta utilizada:
He utilizado pdoc para Python, que genera documentación HTML automáticamente a partir de los docstrings del código.
El codigo usado es: python -m pdoc main.py -o docs

2. Ejemplo de código documentado
def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Cociente de la división.

    Raises:
        ValueError: Si el divisor es cero.
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

3. Enlace público a GitHub PagesExplicación del workflow de publicación:
https://rgarvel709.github.io/Despliegue/

4. Explicación del workflow de publicación
name: CI con AutoCommit

on:
  push:
  workflow_dispatch:

jobs:
  test-and-update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install pytest
      - name: Run tests
        run: python test_main.py
      - name: Update README
        run: python update_readme.py
      - name: Auto-commit README
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: Actualización automática del README por CI

Pasos clave:

Se ejecuta automáticamente con cada push a la rama main.
Instala las dependencias necesarias y genera la documentación HTML.
Publica el resultado en GitHub Pages usando la acción oficial.
En Settings - Pages, seleccioné la rama gh-pages como fuente.

5. Mensajes de commit evidenciando la configuración
Ejemplos de mensajes claros y descriptivos:

Configurar workflow para despliegue automático de documentación
Generar documentación HTML con pdoc
Actualizar docstrings y mejorar documentación
Publicar documentación en GitHub Pages
Corregir errores en workflow de CI/CD
Justificación:

Estos mensajes explican que se ha hecho facilitando el seguimiento.

6. Cómo clonar y regenerar la documentación localmente
Clonar el repositorio:

git clone https://github.com/rgarvel709/Despliegue.git
cd Despliegue

Instalar pdoc:

pip install pdoc

Generar la documentación HTML:

python -m pdoc main.py -o docs


7. Cuestionario de evidencias
a) ¿Qué herramienta o generador utilizaste para crear la documentación HTML?
Utilicé pdoc para Python, que genera documentación HTML a partir de los docstrings.
b) Muestra un fragmento del código con comentarios/docstrings estructurados. ¿Qué estilo has utilizado?
He usado Google Style docstrings, con las etiquetas Args:, Returns: y Raises:. Ejemplo arriba.
c) ¿Qué configuración del workflow y del repositorio utilizaste para publicar la documentación en GitHub Pages? Explica los pasos clave.
El workflow se ejecuta en cada push a main, instala pdoc, genera la documentación y la publica con actions/deploy-pages. En Settings, seleccioné gh-pages como fuente para GitHub Pages.
d) ¿Cómo facilita GitHub Pages compartir documentación actualizada con el equipo y usuarios externos? ¿Ventajas frente a solo tener los archivos HTML en el repo?
GitHub Pages permite que la documentación esté accesible y actualizada para todo el equipo y usuarios externos, sin necesidad de descargar o navegar por carpetas. Es mucho más cómodo y profesional.
e) ¿Son claros y descriptivos los mensajes de commit? Justifícalo.
Si cada commit indica en imperativo la acción realizada, facilitando el seguimiento y la colaboración.
f) ¿Cómo garantizas que la documentación en GitHub Pages es accesible públicamente pero el código fuente solo es accesible para personal autorizado?
La documentación es pública en GitHub Pages, pero el código puede estar en un repositorio privado. Así, sólo quienes tengan acceso al repo ven el código pero la documentación es accesible para todos.
g) ¿Dónde explicas cómo acceder a la documentación publicada en GitHub Pages y dónde detallas las herramientas y comandos usados para generarla?
En el apartado 3 incluyo el enlace a la documentación publicada. En el apartado 1 y 6 detallo la herramienta y los comandos usados.
h) Justifica por qué el workflow implementa CI/CD. ¿Qué evento dispara automáticamente la generación y publicación de la documentación? ¿Por qué esto es despliegue continuo?
El workflow implementa CI/CD porque cada vez que se hace push a main se genera y publica automáticamente la documentación. Asi la documentación siempre está actualizada sin intervención manual.

