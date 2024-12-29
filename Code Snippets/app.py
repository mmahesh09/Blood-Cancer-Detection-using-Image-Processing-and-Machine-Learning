from flask import Flask, request, render_template
import pickle
import numpy as np
from PIL import Image
import io
import traceback

app = Flask(__name__)

# Define the model path
MODEL_PATH = "blood.pkl"

# Load the model from a .pkl file
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if an image file is included in the request
        if 'image' not in request.files:
            return render_template('index.html', prediction_text='No file uploaded.')

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', prediction_text='No file selected.')

        # Process the uploaded image
        image = Image.open(io.BytesIO(file.read()))
        image = image.convert('RGB')  # Ensure the image is in RGB mode
        image = image.resize((224, 224))  # Resize to the expected input size
        image_array = np.array(image) / 255.0  # Normalize the image

        # Ensure the input has the correct dimensions (batch size, height, width, channels)
        if len(image_array.shape) == 3:  # Add batch dimension if missing
            image_array = np.expand_dims(image_array, axis=0)

        # Make prediction
        predictions = model.predict(image_array)

        # Interpret predictions
        categories = ['No Cancer', 'Early Stage', 'Pre-cancerous', 'Progressive Cancer']
        predicted_label = categories[np.argmax(predictions)]

        return render_template('index.html', prediction_text=f'Prediction: {predicted_label}')

    except Exception as e:
        # Print the stack trace
        traceback.print_exc()
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
