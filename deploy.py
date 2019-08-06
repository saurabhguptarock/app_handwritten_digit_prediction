from flask import Flask, request, jsonify
from base64 import decodebytes
from keras.models import load_model
app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # model = load_model('model.h5')
    img_data = request.json.image
    # with open("img.png", "wb") as img:
    #     img.write(decodebytes(img_data))
    return img_data
