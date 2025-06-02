import customtkinter as ctk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
import os
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class QRApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR Generator GUI - Creado por armanson")
        self.geometry("650x550")
        self.resizable(True, True)
        self.theme_option = "Oscuro" if ctk.get_appearance_mode() == "Dark" else "Claro"

        self.qr_image = None
        self.qr_path = None
        self.qr_raw_image = None
        self.data_input_to_encode = ""

        self.build_interface()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def build_interface(self):
        for widget in self.winfo_children():
            if widget.winfo_exists():
                widget.destroy()

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", pady=10, padx=10)

        creator_label = ctk.CTkLabel(self.top_frame, text="Creado por armanson", font=("Arial", 14, "italic"))
        creator_label.pack(side="left", padx=10)

        self.menu_tema = ctk.CTkOptionMenu(self.top_frame, values=["Claro", "Oscuro"], command=self.change_theme)
        self.menu_tema.set(self.theme_option)
        self.menu_tema.pack(side="right", padx=10)

        self.label_tipo = ctk.CTkLabel(self, text="Introduce la URL o texto para el código QR:")
        self.label_tipo.pack(pady=(10, 5))

        self.entry_data = ctk.CTkEntry(self, placeholder_text="Introduce la URL o texto aquí")
        self.entry_data.pack(pady=10, padx=20, fill="x")

        self.boton_generar = ctk.CTkButton(self, text="Generar QR", command=self.generar_qr)
        self.boton_generar.pack(pady=15)

        self.label_imagen = ctk.CTkLabel(self, text="")
        self.label_imagen.pack(pady=10)

        self.frame_guardar = ctk.CTkFrame(self)
        self.boton_guardar = ctk.CTkButton(self.frame_guardar, text="Guardar código QR", command=self.guardar_qr)
        self.combo_formato = ctk.CTkComboBox(self.frame_guardar, values=["JPG", "JPEG", "PNG", "PDF"])
        self.combo_formato.set("PNG")
        self.frame_guardar.pack_forget()

    def on_closing(self):
        if self.qr_path and os.path.exists(self.qr_path):
            os.remove(self.qr_path)
        self.destroy()

    def change_theme(self, choice):
        self.theme_option = choice
        ctk.set_appearance_mode("Dark" if choice == "Oscuro" else "Light")

    def generar_qr(self):
        data_from_entry = self.entry_data.get().strip()
        
        if not data_from_entry:
            messagebox.showerror("Error", "Introduce una URL o texto válido.")
            return

        if self.qr_path and os.path.exists(self.qr_path):
            os.remove(self.qr_path)
        self.qr_path = None
        self.qr_image = None
        self.qr_raw_image = None
        self.data_input_to_encode = ""

        self.boton_generar.configure(state="disabled")

        self.data_input_to_encode = data_from_entry
        self._generate_qr_image()

        self.boton_generar.configure(state="normal")

    def _generate_qr_image(self):
        temp_qr_filename = "temp_qr_code_" + str(os.getpid()) + ".png"

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.data_input_to_encode)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(temp_qr_filename)

        self.qr_path = temp_qr_filename
        self.qr_raw_image = img

        self.qr_image_pil = Image.open(self.qr_path).resize((200, 200), Image.Resampling.LANCZOS)
        self.qr_image = ImageTk.PhotoImage(self.qr_image_pil)

        self.label_imagen.configure(image=self.qr_image, text="")

        self.frame_guardar.pack(pady=10)
        self.boton_guardar.pack(side="left", padx=5)
        self.combo_formato.pack(side="left", padx=5)

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
                img_width, img_height = self.qr_raw_image.size
                temp_path_for_pdf = "temp_qr_for_pdf_" + str(os.getpid()) + ".png"
                self.qr_raw_image.save(temp_path_for_pdf)
                
                c = canvas.Canvas(filename, pagesize=(img_width, img_height))
                c.drawImage(temp_path_for_pdf, 0, 0, width=img_width, height=img_height)
                c.save()
                os.remove(temp_path_for_pdf)
            elif formato in ["jpg", "jpeg"]:
                self.qr_raw_image.convert("RGB").save(filename, "JPEG")
            else: # PNG
                self.qr_raw_image.save(filename, "PNG")

            messagebox.showinfo("Guardado", f"QR guardado como {filename}")
            
            if self.qr_path and os.path.exists(self.qr_path):
                os.remove(self.qr_path)
            
            self.entry_data.delete(0, "end")
            self.entry_data.configure(placeholder_text="Introduce la URL o texto para el QR")
            self.label_imagen.configure(image=None, text="")
            self.frame_guardar.pack_forget()
            
            self.qr_image = None
            self.qr_image_pil = None
            self.qr_path = None
            self.qr_raw_image = None
            self.data_input_to_encode = ""

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el código QR:\n{str(e)}")

if __name__ == "__main__":
    app = QRApp()
    app.mainloop()
