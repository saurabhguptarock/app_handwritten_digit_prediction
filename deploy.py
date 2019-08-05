from flask import Flask, request
from keras.models import load_model
app = Flask(__name__)


@app.route('/<url>', methods=['POST'])
def index(url):
    # model = load_model('model.h5')
    return url
