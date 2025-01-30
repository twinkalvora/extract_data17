from flask import Flask, request
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    image = request.files['image']
    img = Image.open(io.BytesIO(image.read()))

    text = pytesseract.image_to_string(img)
    return {"extracted_text": text}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
