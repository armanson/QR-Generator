# QR Generator

This is a simple and user-friendly graphical user interface (GUI) tool for generating QR codes. It allows users to create QR codes from different types of data and export them in various image or PDF formats.

## Key Features

* **Generates QR codes from URLs, or PDF, JPG, JPEG, PNG files.**
* **Includes a GUI for enhanced user-friendliness.**
* **Real-time Preview:** Visualize the generated QR code instantly within the application.
* **Versatile Saving Options:** Save your QR codes in popular formats like PNG, JPG, JPEG, or even as a PDF document.

## How It Works

The tool operates as follows:

1.  **Input Type Selection:** The user chooses whether the QR code will be generated from a URL, or a PDF, JPG, JPEG, PNG file.
2.  **Data Input:**
    * If "URL" is selected, the user simply types the desired URL into the text field.
    * If a file type (PDF, JPG, etc.) is selected, a "Select file" button appears, allowing the user to browse and choose a file from their system. **Important:** The QR code will contain the *path* to the selected file, not its binary content. This means that scanning the QR will provide the file's path, not the file itself. For the file to be accessible by others, it should be hosted on a web service, and the QR should be of that file's URL.
3.  **QR Generation:** Upon clicking the "Generate QR" button, the application uses the `qrcode` library to create the QR code image and displays it in the interface.
4.  **Saving the QR:** Once generated, the user can choose the output format (PNG, JPG, JPEG, PDF) and save the QR code to their desired location.

## How to Download and Run the Tool

The tool is hosted on GitHub. To download and run it, follow the specific steps for your operating system:

The project repository is: `https://github.com/armanson/QR-Generator`

### For Windows Users

1.  **Install Python and Git:**
    * Download and install Python 3.x from [python.org](https://www.python.org/downloads/). Make sure to check the "Add Python to PATH" option during installation.
    * Download and install Git from [git-scm.com/downloads](https://git-scm.com/downloads/).
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
    python QRGenerator_V1.0.0_English.py
    ```

### For macOS Users

1.  **Install Python and Git:**
    * macOS usually comes with Python pre-installed, but it's recommended to install the latest Python 3.x version from [python.org](https://www.python.org/downloads/) or using Homebrew (`brew install python`).
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
    python QRGenerator_V1.0.0_English.py
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
    pip install customtkinter qrcode Pillow reportlab
    ```
6.  **Run the Tool:**
    ```bash
    python QRGenerator_V1.0.0_English.py
    ```
