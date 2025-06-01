QR Generator

# Generador de Códigos QR - armanson

Esta es una herramienta gráfica sencilla y fácil de usar para generar códigos QR. Permite a los usuarios crear códigos QR a partir de diferentes tipos de datos y exportarlos en varios formatos de imagen o PDF.

## Características Principales

* **Genera códigos QR a partir de URLs o PDF, JPG, JPEG, PNG.
* **Inclusión de GUI para facilitar el uso a los usuarios.
* **Visualiza el código QR generado en tiempo real dentro de la aplicación.
* **Guarda tus códigos QR en formatos populares como PNG, JPG, JPEG, o incluso como un documento PDF.

## Cómo Funciona

La herramienta funciona de la siguiente manera:

1.  **El usuario elige si el código QR se generará a partir de una URL, o un archivo PDF, JPG, JPEG, PNG.
2.  **Introducción de Datos:**
    * Si se selecciona "URL", el usuario simplemente escribe la "URL" deseada en el campo de texto.
    * Si se selecciona un tipo de archivo (PDF, JPG, etc.), aparece un botón "Seleccionar archivo" que permite al usuario navegar y elegir un archivo de su sistema. **Importante:** El código QR contendrá la *ruta* del archivo seleccionado, no el contenido binario del mismo. Esto significa que al escanear el QR, se obtendrá la ruta del archivo, no el archivo en sí. Para que el archivo sea accesible por otros, este debería estar alojado en algún servicio web y el QR debería ser de la URL de dicho archivo.
3.  **Generación del QR:** Al pulsar el botón "Generar QR", la aplicación utiliza la librería `qrcode` para crear la imagen del código QR y la muestra en la interfaz.
4.  **Guardar el QR:** Una vez generado, el usuario puede elegir el formato de salida (PNG, JPG, JPEG, PDF) y guardar el código QR en la ubicación deseada.

## Cómo Descargar y Ejecutar la Herramienta

La herramienta está alojada en GitHub. Para descargarla y ejecutarla, sigue los siguientes pasos para tu sistema operativo:

El repositorio del proyecto es: `https://github.com/armanson/QR-Generator`

### Para Usuarios de Windows

1.  **Instalar Python y Git:**
    * Descarga e instala Python 3.x desde [python.org](https://www.python.org/downloads/). Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
    * Descarga e instala Git desde [git-scm.com/downloads](https://git-scm.com/downloads/).
2.  **Abrir el Símbolo del Sistema (CMD) o PowerShell.**
3.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/armanson/QR-Generator.git](https://github.com/armanson/QR-Generator.git)
    ```
4.  **Navegar al Directorio del Proyecto:**
    ```bash
    cd QR-Generator
    ```
5.  **Instalar Dependencias:**
    ```bash
    pip install customtkinter qrcode Pillow reportlab
    ```
6.  **Ejecutar la Herramienta:**
    ```bash
    python QRGenerator_GUI_ARMANSON_FINAL.py
    ```

### Para Usuarios de macOS

1.  **Instalar Python y Git:**
    * macOS suele venir con Python preinstalado, pero es recomendable instalar la última versión de Python 3.x desde [python.org](https://www.python.org/downloads/) o usando Homebrew (`brew install python`).
    * Instala Git, por ejemplo, con Homebrew (`brew install git`) o Xcode Command Line Tools (`xcode-select --install`).
2.  **Abrir la Terminal.**
3.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/armanson/QR-Generator.git](https://github.com/armanson/QR-Generator.git)
    ```
4.  **Navegar al Directorio del Proyecto:**
    ```bash
    cd QR-Generator
    ```
5.  **Instalar Dependencias:**
    ```bash
    pip install customtkinter qrcode Pillow reportlab
    ```
6.  **Ejecutar la Herramienta:**
    ```bash
    python QRGenerator_GUI_ARMANSON_FINAL.py
    ```

### Para Usuarios de Linux

1.  **Instalar Python y Git:**
    * La mayoría de las distribuciones de Linux ya vienen con Python 3 preinstalado. Si no, puedes instalarlo usando tu gestor de paquetes (ej., `sudo apt install python3` en Debian/Ubuntu, `sudo yum install python3` en Fedora/CentOS).
    * Instala Git usando tu gestor de paquetes (ej., `sudo apt install git` o `sudo yum install git`).
2.  **Abrir una Terminal.**
3.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/armanson/QR-Generator.git](https://github.com/armanson/QR-Generator.git)
    ```
4.  **Navegar al Directorio del Proyecto:**
    ```bash
    cd QR-Generator
    ```
5.  **Instalar Dependencias:**
    ```bash
    pip install customtkinter qrcode Pillow reportlab
    ```
6.  **Ejecutar la Herramienta:**
    ```bash
    python QRGenerator_GUI_ARMANSON_FINAL.py
    ```
