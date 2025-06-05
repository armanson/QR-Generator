# Generador de Códigos QR - armanson ( Castellano )

Esta es una herramienta gráfica sencilla y fácil de usar para generar códigos QR. Permite a los usuarios crear códigos QR a partir de URLs o texto y exportarlos en varios formatos de imagen ( JPEG, JPG y PNG ) o PDF.

## Características Principales

* **Genera códigos QR a partir de URLs o texto.**
* **Inclusión de GUI para facilitar el uso a los usuarios.**
* **Visualiza el código QR generado en tiempo real dentro de la aplicación.**
* **Guarda tus códigos QR en formatos populares como PNG, JPG, JPEG, o como un documento PDF.**

## Cómo Funciona

La herramienta funciona de la siguiente manera:

1.  **Introducción de Datos:** El usuario introduce la URL o el texto deseado directamente en el campo de entrada.
2.  **Generación del QR:** Al pulsar el botón "Generar QR", la aplicación utiliza la librería `qrcode` para crear la imagen del código QR y la muestra en la interfaz.
3.  **Guardar el QR:** Una vez generado, el usuario puede elegir el formato de salida (PNG, JPG, JPEG, PDF) y guardar el código QR en la ubicación deseada.

### Para generar un QR a partir de un archivo (PDF, JPG, PNG, etc.):

Dado que la aplicación solo acepta URLs o texto, si deseas generar un QR que apunte a un archivo (como un PDF o una imagen), deberás seguir estos pasos antes de usar la herramienta:

1.  **Sube tu archivo a un servicio en la nube:** Utiliza un servicio como Google Drive, Dropbox, Microsoft OneDrive, Imgur (para imágenes), o tu propio servidor web.
2.  **Obtén la URL pública del archivo:** Una vez subido, el servicio te proporcionará una URL (enlace) para acceder a ese archivo. Asegúrate de que el archivo sea **público o compartible mediante un enlace público** para que cualquiera pueda escanear el QR y acceder a él.
3.  **Copia esa URL pública y pégala** en el campo de entrada de esta herramienta para generar tu código QR.

## Cómo Descargar y Ejecutar la Herramienta

La herramienta está alojada en GitHub. Para descargarla y ejecutarla, sigue los siguientes pasos para tu sistema operativo:

El repositorio del proyecto es: `https://github.com/armanson/QR-Generator`

### Para Usuarios de Windows

1.  **Instalar Python y Git:**
    * Descarga e instala Python 3.x desde [https://www.python.org/downloads/](https://www.python.org/downloads/). Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
    * Descarga e instala Git desde [https://git-scm.com/downloads](https://git-scm.com/downloads/).
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
    python QRGenerator_V1.5.0_Castellano.py
    ```

### Para Usuarios de macOS

1.  **Instalar Python y Git:**
    * macOS suele venir con Python preinstalado, pero es recomendable instalar la última versión de Python 3.x desde [https://www.python.org/downloads/](https://www.python.org/downloads/) o usando Homebrew (`brew install python`).
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
    python QRGenerator_V1.5.0_Castellano.py
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
    python QRGenerator_V1.5.0_Castellano.py
