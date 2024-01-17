import qrcode
import tkinter as tk
from tkinter import Entry, Button, Label, filedialog

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

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = Label(master, text="Inserisci il link:")
        self.label.pack()

        self.link_entry = Entry(master, width=40)
        self.link_entry.pack()

        self.generate_button = Button(master, text="Genera QR Code", command=self.genera_qrcode)
        self.generate_button.pack()

        self.quit_button = Button(master, text="Esci", command=master.quit)
        self.quit_button.pack()

    def genera_qrcode(self):
        link = self.link_entry.get()

        if not link:
            self.label.config(text="Inserisci un link valido.")
            return

        nome_file_output = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if nome_file_output:
            self.label.config(text="")
            genera_qrcode(link, nome_file_output)
        else:
            self.label.config(text="Operazione annullata.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
