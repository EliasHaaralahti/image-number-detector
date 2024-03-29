from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import base64
import re
import time

# Comment one of the imports below
# PYTHON2 IMPORT
#import cStringIO
# PYTHON3 IMPORT
from io import BytesIO, StringIO

from src.detect_image_number import detect_image_number
from src.preprocess import process_image

app = Flask(__name__)

def generateFileName():
    t = time.localtime()
    timestamp = time.strftime('%Y-%b-%d_%H:%M:%S', t)
    return str(timestamp) + '.png'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    image_b64 = request.values['imageBase64']
    # Remove pattern from the data and decode from base64
    # Python2 way
    #image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
    # Python3 way
    base64data = re.sub('^data:image/.+;base64,', '', image_b64)
    image_data = base64.b64decode(base64data)
    # Python2
    #image_PIL = Image.open(cStringIO.StringIO(image_data))
    # Python3
    image_PIL = Image.open(BytesIO(image_data))
    
    filename = generateFileName()
    filepath = 'images/'
    image_PIL.save(filepath + filename)

    # TODO: Instead of saving the image, send the numpy array
    # to process_image directly, such as:
    # image_np = np.array(image_PIL)

    # Preprocess image
    output = 'images/processed_images/'
    processed_image = process_image(filepath, filename, output)

    # Detect number
    result = detect_image_number(processed_image)
    print("result")
    print(result)
    return result

if __name__ == "__main__":
    app.run()

