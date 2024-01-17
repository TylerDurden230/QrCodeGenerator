import qrcode
import sys

def genera_qrcode(link, nome_file_output):
    # Crea un oggetto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Aggiungi i dati al QRCode
    qr.add_data(link)
    qr.make(fit=True)

    # Crea un oggetto immagine del QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Salva l'immagine del QRCode su un file
    img.save(nome_file_output)

    # Visualizza l'immagine del QRCode
    img.show()

if __name__ == "__main__":
    # Verifica che sia fornito almeno un argomento dalla riga di comando
    if len(sys.argv) < 2:
        print("Usage: python script.py <link_da_convertire>")
        sys.exit(1)

    # Ottieni il link da convertire dall'argomento della riga di comando
    link_da_convertire = sys.argv[1]

    # Inserisci il nome del file di output (con estensione PNG)
    nome_file_output = "QRCode.png"

    # Chiama la funzione per generare il QR code
    genera_qrcode(link_da_convertire, nome_file_output)
