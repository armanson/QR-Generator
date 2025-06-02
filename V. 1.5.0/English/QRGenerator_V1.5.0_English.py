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
        self.title("QR Generator GUI - Created by armanson")
        self.geometry("650x550")
        self.resizable(True, True)
        self.theme_option = "Dark" if ctk.get_appearance_mode() == "Dark" else "Light"

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

        creator_label = ctk.CTkLabel(self.top_frame, text="Created by armanson", font=("Arial", 14, "italic"))
        creator_label.pack(side="left", padx=10)

        self.theme_menu = ctk.CTkOptionMenu(self.top_frame, values=["Light", "Dark"], command=self.change_theme)
        self.theme_menu.set(self.theme_option)
        self.theme_menu.pack(side="right", padx=10)

        self.data_label = ctk.CTkLabel(self, text="Enter URL or text for the QR code:")
        self.data_label.pack(pady=(10, 5))

        self.data_entry = ctk.CTkEntry(self, placeholder_text="Enter URL or text here")
        self.data_entry.pack(pady=10, padx=20, fill="x")

        self.generate_button = ctk.CTkButton(self, text="Generate QR", command=self.generate_qr)
        self.generate_button.pack(pady=15)

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(pady=10)

        self.save_frame = ctk.CTkFrame(self)
        self.save_button = ctk.CTkButton(self.save_frame, text="Save QR code", command=self.save_qr)
        self.format_combo = ctk.CTkComboBox(self.save_frame, values=["JPG", "JPEG", "PNG", "PDF"])
        self.format_combo.set("PNG")
        self.save_frame.pack_forget()

    def on_closing(self):
        if self.qr_path and os.path.exists(self.qr_path):
            os.remove(self.qr_path)
        self.destroy()

    def change_theme(self, choice):
        self.theme_option = choice
        ctk.set_appearance_mode("Dark" if choice == "Dark" else "Light")

    def generate_qr(self):
        data_from_entry = self.data_entry.get().strip()
        
        if not data_from_entry:
            messagebox.showerror("Error", "Please enter a valid URL or text.")
            return

        if self.qr_path and os.path.exists(self.qr_path):
            os.remove(self.qr_path)
        self.qr_path = None
        self.qr_image = None
        self.qr_raw_image = None
        self.data_input_to_encode = ""

        self.generate_button.configure(state="disabled")

        self.data_input_to_encode = data_from_entry
        self._generate_qr_image()

        self.generate_button.configure(state="normal")

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

        self.image_label.configure(image=self.qr_image, text="")

        self.save_frame.pack(pady=10)
        self.save_button.pack(side="left", padx=5)
        self.format_combo.pack(side="left", padx=5)

    def save_qr(self):
        if not self.qr_raw_image:
            messagebox.showerror("Error", "No QR code to save.")
            return

        file_format = self.format_combo.get().lower()
        filename = filedialog.asksaveasfilename(defaultextension=f".{file_format}", filetypes=[(file_format.upper(), f"*.{file_format}")])
        if not filename:
            return

        try:
            if file_format == "pdf":
                img_width, img_height = self.qr_raw_image.size
                temp_path_for_pdf = "temp_qr_for_pdf_" + str(os.getpid()) + ".png"
                self.qr_raw_image.save(temp_path_for_pdf)
                
                c = canvas.Canvas(filename, pagesize=(img_width, img_height))
                c.drawImage(temp_path_for_pdf, 0, 0, width=img_width, height=img_height)
                c.save()
                os.remove(temp_path_for_pdf)
            elif file_format in ["jpg", "jpeg"]:
                self.qr_raw_image.convert("RGB").save(filename, "JPEG")
            else: # PNG
                self.qr_raw_image.save(filename, "PNG")

            messagebox.showinfo("Saved", f"QR saved as {filename}")
            
            if self.qr_path and os.path.exists(self.qr_path):
                os.remove(self.qr_path)
            
            self.data_entry.delete(0, "end")
            self.data_entry.configure(placeholder_text="Enter URL or text for the QR")
            self.image_label.configure(image=None, text="")
            self.save_frame.pack_forget()
            
            self.qr_image = None
            self.qr_image_pil = None
            self.qr_path = None
            self.qr_raw_image = None
            self.data_input_to_encode = ""

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the QR code:\n{str(e)}")

if __name__ == "__main__":
    app = QRApp()
    app.mainloop()
