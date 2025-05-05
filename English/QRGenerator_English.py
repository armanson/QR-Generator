import qrcode
from reportlab.pdfgen import canvas
import os

def generar_qr(data, formato, nombre_archivo):
    # Generar el código QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Guardar en el formato deseado
    if formato == 'jpg':
        img.save(f"{nombre_archivo}.jpg")
    elif formato == 'png':
        img.save(f"{nombre_archivo}.png")
    elif formato == 'pdf':
        img.save(f"{nombre_archivo}.png")  # Guardar primero como PNG
        c = canvas.Canvas(f"{nombre_archivo}.pdf")
        c.drawImage(f"{nombre_archivo}.png", 0, 0)
        c.save()
        os.remove(f"{nombre_archivo}.png")  # Eliminar el PNG temporal
    else:
        print("Invalid format. It must be jpg, png o pdf.")

def main():
    print("Welcome to QRGenerator")
    tipo = input("Do you want to generate a QR code from a URL or PDF File? (Insert 'url' o 'pdf'): ").strip().lower()
    
    if tipo == 'url':
        data = input("Enther the URL: ")
    elif tipo == 'pdf':
        data = input("Enter the name of the PDF file (Whit extension): ")
        if not os.path.isfile(data):
            print("The PDF file does not exist. Make sure the name and extension is correct.")
            return
    else:
        print("Invalid type. Exiting.")
        return

    formato = input("¿In what format do you want to save the QR? (jpg, png, pdf): ").strip().lower()
    nombre_archivo = "QR_" + data.split('/')[-1].split('.')[0]  # Nombre basado en la entrada

    generar_qr(data, formato, nombre_archivo)
    print(f"QR code generated and saved as {nombre_archivo}.{formato}")

if __name__ == "__main__":
    main()


