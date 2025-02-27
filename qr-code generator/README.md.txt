# QR Code Generator

## 📌 Description
This is a simple Python-based QR code generator that allows users to create QR codes from text or URLs. The generated QR codes can be saved as image files (.png, .jpg, .jpeg) with customizable colors.

## 🚀 Features
- Generate QR codes from any text or URL
- Customizable QR code and background colors
- Saves QR codes as image files (.png, .jpg, .jpeg)
- Displays the generated QR code after saving
- Handles errors gracefully for better user experience

## 🛠️ Requirements
Ensure you have Python installed along with the required dependencies:

```bash
pip install qrcode[pil]
```

## 🏃‍♂️ Usage
Run the script using Python:

```bash
python qr_code_generator.py
```

### 🎨 Customization Options
- Enter the text or URL you want to convert into a QR code
- Provide a filename (with or without extension, default: .png)
- Choose custom QR code and background colors (optional)

## 📝 Example
```
Enter the text or URL: https://github.com
Enter the filename (with extension, e.g., qr_code.png): github_qr.png
Enter QR color (default: black): blue
Enter background color (default: white): yellow
✅ QR code saved as: github_qr.png
```

## 🖼️ Output
The generated QR code is saved and displayed automatically.

## ⚠️ Error Handling
- Prevents empty inputs for the QR code data
- Ensures the provided filename has a valid image extension
- Checks for invalid or non-existent directories before saving

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to fork this repository and improve the script! Suggestions and pull requests are welcome. 🚀

