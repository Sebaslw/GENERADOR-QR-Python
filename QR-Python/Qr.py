#importamos el qr de su libreria
import qrcode

# Creamos el qr
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Importamos su data 
qr.add_data('https://github.com/Sebaslw?tab=repositories')
qr.make(fit=True)

# Guardamos el qr en un Archivo 
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")
