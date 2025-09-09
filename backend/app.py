
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return 'Backend is running!'

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    img = Image.open(io.BytesIO(file.read()))
    # TODO: Load model & make prediction
    return jsonify({'breed': 'Sample Breed', 'confidence': 0.95})

if __name__ == '__main__':
    app.run(debug=True)

