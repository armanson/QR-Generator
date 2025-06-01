import customtkinter as ctk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class QRApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR Generator GUI - Creado por armanson")
        self.geometry("650x550")
        self.resizable(True, True)
        self.theme_option = "Oscuro" if ctk.get_appearance_mode() == "Dark" else "Claro"

        self.qr_image = None # Objeto PhotoImage para mostrar en la GUI
        self.qr_path = None # Ruta al archivo PNG temporal del QR generado
        self.qr_raw_image = None # Objeto PIL Image del QR generado
        self.data_input = "" # El dato que se introduce para generar el QR

        self.build_interface()

    def build_interface(self):
        # Esta función ahora solo construye la interfaz principal y los widgets que deben estar siempre presentes.
        # Los elementos dinámicos (imagen QR, opciones de guardar) se gestionan con pack/pack_forget.

        # Barra superior (se asegura de que exista o se recrea si se llamó build_interface por primera vez)
        if not hasattr(self, 'top_frame') or not self.top_frame.winfo_exists():
            self.top_frame = ctk.CTkFrame(self)
            self.top_frame.pack(fill="x", pady=10, padx=10)

            creator_label = ctk.CTkLabel(self.top_frame, text="Creado por armanson", font=("Arial", 14, "italic"))
            creator_label.pack(side="left", padx=10)

            self.menu_tema = ctk.CTkOptionMenu(self.top_frame, values=["Claro", "Oscuro"], command=self.change_theme)
            self.menu_tema.set(self.theme_option)
            self.menu_tema.pack(side="right", padx=10)

        # Destruir todos los widgets excepto la barra superior y los que ya existen
        for widget in self.winfo_children():
            if widget != self.top_frame and widget.winfo_exists(): # Añadido check .winfo_exists()
                widget.destroy()

        # Tipo de datos
        self.label_tipo = ctk.CTkLabel(self, text="Selecciona el tipo de entrada para el código QR:")
        self.label_tipo.pack(pady=(10, 5))

        self.combo_tipo = ctk.CTkComboBox(self, values=["URL", "PDF", "JPG", "JPEG", "PNG"], command=self.on_type_change)
        self.combo_tipo.set("URL") # Valor inicial
        self.combo_tipo.pack(pady=5, padx=20, fill="x")

        # Entrada de datos
        self.entry_data = ctk.CTkEntry(self, placeholder_text="Introduce el dato aquí o selecciona un archivo")
        self.entry_data.pack(pady=10, padx=20, fill="x")

        self.boton_buscar = ctk.CTkButton(self, text="Seleccionar archivo", command=self.seleccionar_archivo)
        self.boton_buscar.pack_forget() # Oculto por defecto

        # Botón para generar QR
        self.boton_generar = ctk.CTkButton(self, text="Generar QR", command=self.generar_qr)
        self.boton_generar.pack(pady=15)

        # Imagen de previsualización
        self.label_imagen = ctk.CTkLabel(self, text="")
        self.label_imagen.pack(pady=10)

        # Guardar opciones
        self.frame_guardar = ctk.CTkFrame(self)
        self.boton_guardar = ctk.CTkButton(self.frame_guardar, text="Guardar código QR", command=self.guardar_qr)
        self.combo_formato = ctk.CTkComboBox(self.frame_guardar, values=["JPG", "JPEG", "PNG", "PDF"])
        self.combo_formato.set("PNG") # Formato por defecto
        self.frame_guardar.pack_forget() # Oculto por defecto

    def change_theme(self, choice):
        self.theme_option = choice
        ctk.set_appearance_mode("Dark" if choice == "Oscuro" else "Light")

    def on_type_change(self, selected_type):
        self.entry_data.delete(0, "end")
        if selected_type in ["PDF", "JPG", "JPEG", "PNG"]:
            self.entry_data.configure(placeholder_text=f"Ruta del archivo {selected_type} para el QR")
            self.boton_buscar.pack(pady=5)
        else: # URL
            self.entry_data.configure(placeholder_text="Introduce la URL o texto para el QR")
            self.boton_buscar.pack_forget()

        # Limpiar la imagen del QR y ocultar las opciones de guardar al cambiar el tipo
        self.label_imagen.configure(image=None, text="")
        self.frame_guardar.pack_forget()
        
        # Asegurarse de limpiar las referencias a imágenes temporales
        self.qr_image = None
        self.qr_raw_image = None
        if self.qr_path and os.path.exists(self.qr_path):
            os.remove(self.qr_path) # Eliminar el archivo temporal del QR si existe
        self.qr_path = None
        self.data_input = ""

    def seleccionar_archivo(self):
        tipo = self.combo_tipo.get()
        filetypes = [("Todos los archivos", "*.*")]
        if tipo == "PDF":
            filetypes = [("Archivos PDF", "*.pdf")]
        elif tipo == "JPEG":
            filetypes = [("Archivos JPEG", "*.jpeg")]
        elif tipo == "JPG":
            filetypes = [("Archivos JPG", "*.jpg")]
        elif tipo == "PNG":
            filetypes = [("Archivos PNG", "*.png")]

        archivo = filedialog.askopenfilename(filetypes=filetypes)
        if archivo:
            self.data_input = archivo
            self.entry_data.delete(0, "end")
            self.entry_data.insert(0, archivo)
            self.entry_data.pack(pady=10, padx=20, fill="x")

    def generar_qr(self):
        try:
            data = self.entry_data.get().strip()
            if not data:
                messagebox.showerror("Error", "Introduce una entrada válida o selecciona un archivo.")
                return

            self.data_input = data
            
            # Limpiar cualquier QR temporal anterior antes de generar uno nuevo
            if self.qr_path and os.path.exists(self.qr_path):
                os.remove(self.qr_path)
            
            # Usar un nombre de archivo temporal único para evitar conflictos y asegurar que se cargue la imagen correcta
            temp_qr_filename = "temp_qr_code_" + str(os.getpid()) + ".png" # Añadir PID para mayor unicidad

            # Generar QR
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(temp_qr_filename)

            self.qr_path = temp_qr_filename # Guardar la ruta del archivo temporal
            self.qr_raw_image = img # Guardar el objeto PIL Image

            # Cargar y mostrar el QR en la GUI
            # Abrir la imagen con PIL y crear una referencia PhotoImage
            # Es crucial mantener una referencia a PhotoImage en self.qr_image
            self.qr_image_pil = Image.open(self.qr_path).resize((200, 200), Image.Resampling.LANCZOS) # Usar LANCZOS para mejor calidad
            self.qr_image = ImageTk.PhotoImage(self.qr_image_pil) # Crear PhotoImage

            self.label_imagen.configure(image=self.qr_image, text="")

            # Mostrar opciones para guardar
            self.frame_guardar.pack(pady=10)
            self.boton_guardar.pack(side="left", padx=5)
            self.combo_formato.pack(side="left", padx=5)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el código QR:\n{str(e)}")

    def guardar_qr(self):
        if not self.qr_raw_image:
            messagebox.showerror("Error", "No hay código QR para guardar.")
            return

        formato = self.combo_formato.get().lower()
        filename = filedialog.asksaveasfilename(defaultextension=f".{formato}", filetypes=[(formato.upper(), f"*.{formato}")])
        if not filename:
            return

        try:
            if formato == "pdf":
                # Para PDF, necesitamos una imagen temporal para incrustar
                temp_path_for_pdf = "temp_qr_for_pdf_" + str(os.getpid()) + ".png"
                self.qr_raw_image.save(temp_path_for_pdf)
                
                c = canvas.Canvas(filename)
                c.drawImage(temp_path_for_pdf, 50, 700, width=200, height=200) # Ejemplo de posición y tamaño
                c.save()
                os.remove(temp_path_for_pdf) # Eliminar la imagen temporal
            elif formato in ["jpg", "jpeg"]:
                # Convertir a RGB para JPG/JPEG, ya que no soportan transparencia
                self.qr_raw_image.convert("RGB").save(filename, "JPEG")
            else: # PNG
                self.qr_raw_image.save(filename, "PNG")

            messagebox.showinfo("Guardado", f"QR guardado como {filename}")
            
            # Limpiar el QR temporal generado en generar_qr si existe
            if self.qr_path and os.path.exists(self.qr_path):
                os.remove(self.qr_path)
            
            # Resetear la interfaz a su estado inicial
            self.entry_data.delete(0, "end")
            self.entry_data.configure(placeholder_text="Introduce la URL o texto para el QR")
            self.boton_buscar.pack_forget() # Oculta el botón de archivo
            self.label_imagen.configure(image=None, text="") # Borra la imagen del QR
            self.frame_guardar.pack_forget() # Oculta las opciones de guardar
            
            # Limpiar todas las referencias a imágenes para evitar problemas de memoria
            self.qr_image = None
            self.qr_image_pil = None # También limpiar la referencia a la imagen PIL
            self.qr_path = None
            self.qr_raw_image = None
            self.data_input = ""
            self.combo_tipo.set("URL") # Restablece el tipo de entrada a URL

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el código QR:\n{str(e)}")


if __name__ == "__main__":
    app = QRApp()
    app.mainloop()

