from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/generate', methods = ['GET', 'POST'])
def generate():

    animal = requests.get("http:/service2:5001/animal")
    noise = requests.post("http:/service2:5001/noise", data=animal.text)

    return render_template('generate.html', title='Generate', animal=animal.text, noise=noise.text)