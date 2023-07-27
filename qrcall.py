import qrcode

def generate_phone_call_qr_code(phone_number):
    # Create the phone call URI.
    phone_call_uri = "tel:" + phone_number

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(phone_call_uri)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="gold", back_color="black")

    return qr_image

if __name__ == "__main__":
    # Replace 'your_phone_number' with the desired phone number, including the country code.
    phone_number = "+91"
    
    qr_code_image = generate_phone_call_qr_code(phone_number)
    
    # Save the image as a PNG file
    qr_code_image.save("phone_call_qr_code2.png")
