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


# QR Code Generator - armanson

This is a simple and user-friendly graphical tool for generating QR codes. It allows users to create QR codes from URLs or text and export them in various image formats (JPEG, JPG, and PNG) or PDF.

## Main Features

* **Generates QR codes from URLs or text.**
* **Includes a GUI for easy user interaction.**
* **Visualizes the generated QR code in real-time within the application.**
* **Saves your QR codes in popular formats such as PNG, JPG, JPEG, or as a PDF document.**

## How It Works

The tool operates as follows:

1.  **Data Input:** The user directly enters the desired URL or text into the input field.
2.  **QR Generation:** Upon clicking the "Generate QR" button, the application uses the `qrcode` library to create the QR code image and displays it in the interface.
3.  **Save QR:** Once generated, the user can choose the output format (PNG, JPG, JPEG, PDF) and save the QR code to their desired location.

### To generate a QR from a file (PDF, JPG, PNG, etc.):

Since the application only accepts URLs or text, if you wish to generate a QR code that points to a file (like a PDF or an image), you will need to follow these steps before using the tool:

1.  **Upload your file to a cloud service:** Use a service like Google Drive, Dropbox, Microsoft OneDrive, Imgur (for images), or your own web server.
2.  **Obtain the public URL of the file:** Once uploaded, the service will provide you with a URL (link) to access that file. Ensure the file is **public or shareable via a public link** so that anyone can scan the QR and access it.
3.  **Copy that public URL and paste it** into the input field of this tool to generate your QR code.

## How to Download and Run the Tool

The tool is hosted on GitHub. To download and run it, follow the steps below for your operating system:

The project repository is: `https://github.com/armanson/QR-Generator`

### For Windows Users

1.  **Install Python and Git:**
    * Download and install Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to check the "Add Python to PATH" option during installation.
    * Download and install Git from [https://git-scm.com/downloads](https://git-scm.com/downloads/).
2.  **Open Command Prompt (CMD) or PowerShell.**
3.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/armanson/QR-Generator.git](https://github.com/armanson/QR-Generator.git)
    ```
4.  **Navigate to the Project Directory:**
    ```bash
    cd QR-Generator
    ```
5.  **Install Dependencies:**
    ```bash
    pip install customtkinter qrcode Pillow reportlab
    ```
6.  **Run the Tool:**
    ```bash
    python QRGenerator_V1.5.0_Castellano.py
    ```

### For macOS Users

1.  **Install Python and Git:**
    * macOS usually comes with Python pre-installed, but it's recommended to install the latest Python 3.x version from [https://www.python.org/downloads/](https://www.python.org/downloads/) or using Homebrew (`brew install python`).
    * Install Git, for example, with Homebrew (`brew install git`) or Xcode Command Line Tools (`xcode-select --install`).
2.  **Open Terminal.**
3.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/armanson/QR-Generator.git](https://github.com/armanson/QR-Generator.git)
    ```
4.  **Navigate to the Project Directory:**
    ```bash
    cd QR-Generator
    ```
5.  **Install Dependencies:**
    ```bash
    pip install customtkinter qrcode Pillow reportlab
    ```
6.  **Run the Tool:**
    ```bash
    python QRGenerator_V1.5.0_Castellano.py
    ```

### For Linux Users

1.  **Install Python and Git:**
    * Most Linux distributions come with Python 3 pre-installed. If not, you can install it using your package manager (e.g., `sudo apt install python3` on Debian/Ubuntu, `sudo yum install python3` on Fedora/CentOS).
    * Install Git using your package manager (e.g., `sudo apt install git` or `sudo yum install git`).
2.  **Open a Terminal.**
3.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/armanson/QR-Generator.git](https://github.com/armanson/QR-Generator.git)
    ```
4.  **Navigate to the Project Directory:**
    ```bash
    cd QR-Generator
    ```
5.  **Install Dependencies:**
    ```bash
