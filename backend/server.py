import os
import numpy as np
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import requests
from io import BytesIO
import pickle

app = Flask(__name__)

model = load_model('BrainTumor10Epochs.h5')


def get_className(value):
    class_no = int(round(float(value[0])))  # Convert to Python float before rounding
    if class_no == 0:
        return "No Brain Tumor"
    elif class_no == 1:
        return "Warning! Tumor detected. Please contact us immediately for further evaluation and treatment."
    else:
        return "Unknown class"

def is_valid_url(url):
    return url.startswith(('http:', 'https:'))

def getResult(url):
    try:
        if not is_valid_url(url):
            return None  # If it's not a valid URL, return None or handle accordingly

        # Download the image from the URL
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        
        image = image.resize((64, 64))
        image = np.array(image)
        input_img = np.expand_dims(image, axis=0)
        result = model.predict(input_img)
        return result
    except Exception as e:
        print('Error processing input:', str(e))
        return None

@app.route('/tumorpredict', methods=['POST'])
def tumorpredict():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if url and is_valid_url(url):
            value = getResult(url)
            
            if value is not None:
                result = get_className(value)
                return jsonify({'result': result})
                
        return jsonify({'error': 'Invalid URL'}), 400
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
