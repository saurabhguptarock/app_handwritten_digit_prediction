from flask import Flask, request
from keras.models import load_model,
app = Flask(__name__)


@app.route('/')
def index():
    model = load_model('model.h5')
    return model.to_json()
