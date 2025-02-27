import qrcode
import os

try:
    # Get user input for data and filename
    data = input("Enter the text or URL: ").strip()
    if not data:
        raise ValueError("Data for the QR code cannot be empty.")
    
    filename = input("Enter the filename (with extension, e.g., qr_code.png): ").strip()
    if not filename.endswith(('.png', '.jpg', '.jpeg')):
        filename += ".png"  
    
    # Ensure the filename is valid
    if os.path.dirname(filename) and not os.path.exists(os.path.dirname(filename)):
        raise ValueError("The specified directory does not exist.")
    
    # Create QR Code with customization options
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate the image with custom colors
    fill_color = input("Enter QR color (default: black): ").strip() or "black"
    back_color = input("Enter background color (default: white): ").strip() or "white"
    
    image = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    image.save(filename)
    print(f"✅ QR code saved as: {filename}")

    # Show QR code after generation (optional)
    image.show()

except Exception as e:
    print(f"❌ Error: {e}")
