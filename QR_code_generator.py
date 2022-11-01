import qrcode

def generate_qrcode(text="https://jiya55.github.io/NGO-website/sa.html"):
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img= qr.make_image(fill_color="black", back_color="white")
    img.save("ngo_website.png")
url = input("Please enter your Url: ")
generate_qrcode()
