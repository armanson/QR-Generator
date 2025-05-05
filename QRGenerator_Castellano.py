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
        print("Formato no válido. Debe ser jpg, png o pdf.")

def main():
    print("Bienvenido a QRGenerator")
    tipo = input("¿Quieres generar un código QR a partir de una URL o un archivo PDF? (ingresa 'url' o 'pdf'): ").strip().lower()
    
    if tipo == 'url':
        data = input("Ingresa la URL: ")
    elif tipo == 'pdf':
        data = input("Ingresa el nombre del archivo PDF (con extensión): ")
        if not os.path.isfile(data):
            print("El archivo PDF no existe. Asegúrate de que el nombre y la extensión sean correctos.")
            return
    else:
        print("Tipo no válido. Saliendo.")
        return

    formato = input("¿En qué formato deseas guardar el QR? (jpg, png, pdf): ").strip().lower()
    nombre_archivo = "QR_" + data.split('/')[-1].split('.')[0]  # Nombre basado en la entrada

    generar_qr(data, formato, nombre_archivo)
    print(f"Código QR generado y guardado como {nombre_archivo}.{formato}")

if __name__ == "__main__":
    main()


