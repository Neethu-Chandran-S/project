from flask import Flask, render_template,request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html',method="post")
if __name__ == "__main__":
    app.run()