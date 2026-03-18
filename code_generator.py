import qrcode

def generate_qr(link, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Success! QR code saved as {filename}")

my_link = "https://forms.gle/LcRCXnb4UMdZKEbZ8"
output_file = "form_qr.png"

if __name__ == "__main__":
    generate_qr(my_link, output_file)