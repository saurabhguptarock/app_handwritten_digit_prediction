from flask import Flask, request, jsonify
from base64 import decodebytes
from keras.models import load_model
import numpy as np
import cv2
# import matplotlib.pyplot as plt
app = Flask(__name__)

# img = cv2.imread('img.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img.shape)


@app.route('/', methods=['POST'])
def index():
    # model = load_model('model.h5')
    img_data = request.json['image']
    with open("img.png", "wb") as img:
        img.write(decodebytes(img_data))

    img = cv2.imread('img.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    prediction = 2
    return jsonify(prediction=img)
