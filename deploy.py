from flask import Flask, request
from keras.models import load_model
app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # model = load_model('model.h5')
    return request.json
