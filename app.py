import json
from urllib import response
from flask import Flask, jsonify, request, send_file
import os
from flask_cors import CORS
from PIL import Image
from yolo import process
import io
import base64
app = Flask(__name__)

@app.route('/', methods=['POST','PUT'])
def upload_image():
    file = request.files['file']
    if not file:
        return {'error': 'Missing file'}, 400
    input_image=Image.open(file)
    output_image = process(input_image)
    output_image.save("plot.png")
    with open("plot.png", "rb") as img_file:
        b64_bytes = base64.b64encode(img_file.read())
    return b64_bytes
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
