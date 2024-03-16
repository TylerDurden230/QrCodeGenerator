import qrcode
import sys

def genera_qrcode(link, nome_file_output):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_file_output)
    img.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <link_da_convertire>")
        sys.exit(1)
    link_da_convertire = sys.argv[1]
    nome_file_output = "QRCode.png"
    genera_qrcode(link_da_convertire, nome_file_output)
