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
        self.title("QR Generator GUI - Created by armanson")
        self.geometry("650x550")
        self.resizable(True, True)
        # Determine initial theme based on system setting
        self.theme_option = "Dark" if ctk.get_appearance_mode() == "Dark" else "Light"

        self.qr_image = None  # PhotoImage object for displaying in GUI
        self.qr_image_pil = None # PIL Image object to maintain reference
        self.qr_path = None  # Path to the temporary PNG file of the generated QR
        self.qr_raw_image = None  # PIL Image object of the generated QR
        self.data_input = ""  # The data entered to generate the QR

        self.build_interface()

    def build_interface(self):
        # This function now only builds the main interface and widgets that should always be present.
        # Dynamic elements (QR image, save options) are managed with pack/pack_forget.

        # Top bar (ensures it exists or recreates it if build_interface was called for the first time)
        # Only create if it doesn't exist to avoid duplicates when calling build_interface in certain scenarios.
        if not hasattr(self, 'top_frame') or not self.top_frame.winfo_exists():
            self.top_frame = ctk.CTkFrame(self)
            self.top_frame.pack(fill="x", pady=10, padx=10)

            creator_label = ctk.CTkLabel(self.top_frame, text="Created by armanson", font=("Arial", 14, "italic"))
            creator_label.pack(side="left", padx=10)

            self.theme_menu = ctk.CTkOptionMenu(self.top_frame, values=["Light", "Dark"], command=self.change_theme)
            self.theme_menu.set(self.theme_option)
            self.theme_menu.pack(side="right", padx=10)

        # Destroy all widgets except the top bar and those that already exist
        for widget in self.winfo_children():
            if widget != self.top_frame and widget.winfo_exists():
                widget.destroy()

        # Data type selection
        self.type_label = ctk.CTkLabel(self, text="Select the input type for the QR code:")
        self.type_label.pack(pady=(10, 5))

        self.type_combo = ctk.CTkComboBox(self, values=["URL", "PDF", "JPG", "JPEG", "PNG"], command=self.on_type_change)
        self.type_combo.set("URL")  # Initial value
        self.type_combo.pack(pady=5, padx=20, fill="x")

        # Data input
        self.data_entry = ctk.CTkEntry(self, placeholder_text="Enter data here or select a file")
        self.data_entry.pack(pady=10, padx=20, fill="x")

        self.browse_button = ctk.CTkButton(self, text="Select file", command=self.select_file)
        self.browse_button.pack_forget()  # Hidden by default

        # Generate QR Button
        self.generate_button = ctk.CTkButton(self, text="Generate QR", command=self.generate_qr)
        self.generate_button.pack(pady=15)

        # Preview Image
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(pady=10)

        # Save options
        self.save_frame = ctk.CTkFrame(self)
        self.save_button = ctk.CTkButton(self.save_frame, text="Save QR Code", command=self.save_qr)
        self.format_combo = ctk.CTkComboBox(self.save_frame, values=["JPG", "JPEG", "PNG", "PDF"])
        self.format_combo.set("PNG")  # Default format
        self.save_frame.pack_forget()  # Hidden by default

    def change_theme(self, choice):
        self.theme_option = choice
        ctk.set_appearance_mode("Dark" if choice == "Dark" else "Light")

    def on_type_change(self, selected_type):
        self.data_entry.delete(0, "end")
        if selected_type in ["PDF", "JPG", "JPEG", "PNG"]:
            self.data_entry.configure(placeholder_text=f"Path to {selected_type} file for QR")
            self.browse_button.pack(pady=5)
        else:  # URL
            self.data_entry.configure(placeholder_text="Enter URL or text for QR")
            self.browse_button.pack_forget()

        # Clear the QR image and hide save options when changing type
        self.image_label.configure(image=None, text="")
        self.save_frame.pack_forget()
        
        # Ensure temporary image references are cleared
        self.qr_image = None
        self.qr_image_pil = None
        if self.qr_path and os.path.exists(self.qr_path):
            os.remove(self.qr_path)  # Delete the temporary QR file if it exists
        self.qr_path = None
        self.data_input = ""

    def select_file(self):
        file_type = self.type_combo.get()
        filetypes = [("All files", "*.*")]
        if file_type == "PDF":
            filetypes = [("PDF files", "*.pdf")]
        elif file_type == "JPEG":
            filetypes = [("JPEG files", "*.jpeg")]
        elif file_type == "JPG":
            filetypes = [("JPG files", "*.jpg")]
        elif file_type == "PNG":
            filetypes = [("PNG files", "*.png")]

        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            self.data_input = file_path
            self.data_entry.delete(0, "end")
            self.data_entry.insert(0, file_path)
            self.data_entry.pack(pady=10, padx=20, fill="x")

    def generate_qr(self):
        try:
            data = self.data_entry.get().strip()
            if not data:
                messagebox.showerror("Error", "Please enter valid data or select a file.")
                return

            self.data_input = data
            
            # Clear any previous temporary QR before generating a new one
            if self.qr_path and os.path.exists(self.qr_path):
                os.remove(self.qr_path)
            
            # Use a unique temporary filename to avoid conflicts
            temp_qr_filename = "temp_qr_code_" + str(os.getpid()) + ".png"

            # Generate QR
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(temp_qr_filename)

            self.qr_path = temp_qr_filename  # Save the path to the temporary file
            self.qr_raw_image = img  # Save the PIL Image object

            # Load and display the QR in the GUI
            # Open the image with PIL and create a PhotoImage reference
            # It's crucial to maintain a reference to PhotoImage in self.qr_image
            self.qr_image_pil = Image.open(self.qr_path).resize((200, 200), Image.Resampling.LANCZOS)
            self.qr_image = ImageTk.PhotoImage(self.qr_image_pil)

            self.image_label.configure(image=self.qr_image, text="")

            # Show save options
            self.save_frame.pack(pady=10)
            self.save_button.pack(side="left", padx=5)
            self.format_combo.pack(side="left", padx=5)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while generating the QR code:\n{str(e)}")

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
                # For PDF, we need a temporary image to embed
                temp_path_for_pdf = "temp_qr_for_pdf_" + str(os.getpid()) + ".png"
                self.qr_raw_image.save(temp_path_for_pdf)
                
                c = canvas.Canvas(filename)
                # Adjust position and size of the QR in the PDF if necessary
                c.drawImage(temp_path_for_pdf, 50, 700, width=200, height=200)
                c.save()
                os.remove(temp_path_for_pdf)  # Delete the temporary image
            elif file_format in ["jpg", "jpeg"]:
                # Convert to RGB for JPG/JPEG, as they don't support transparency
                self.qr_raw_image.convert("RGB").save(filename, "JPEG")
            else:  # PNG
                self.qr_raw_image.save(filename, "PNG")

            messagebox.showinfo("Saved", f"QR saved as {filename}")
            
            # Clean up the temporary QR generated in generate_qr if it exists
            if self.qr_path and os.path.exists(self.qr_path):
                os.remove(self.qr_path)
            
            # Reset the interface to its initial state
            self.data_entry.delete(0, "end")
            self.data_entry.configure(placeholder_text="Enter URL or text for QR")
            self.browse_button.pack_forget()  # Hide file selection button
            self.image_label.configure(image=None, text="")  # Clear QR image
            self.save_frame.pack_forget()  # Hide save options
            
            # Clear all image references to prevent memory issues
            self.qr_image = None
            self.qr_image_pil = None
            self.qr_path = None
            self.qr_raw_image = None
            self.data_input = ""
            self.type_combo.set("URL")  # Reset input type to URL

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the QR code:\n{str(e)}")


if __name__ == "__main__":
    app = QRApp()
    app.mainloop()
