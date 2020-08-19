from flask import Response, request
from application import app
import random

@app.route('/animal', methods=['GET'])
def animal():
    animals = ["dog", "cat", "horse", "cow"]
    rand_animal = random.choice(animals)

    return Response(rand_animal, mimetype='text/plain')

@app.route('/noise', methods=['GET'])
def noise():
    animal = request.data.decode("utf-8")
    if animal == "dog":
        noise = "woof"
    elif animal == "cat":
        noise = "meow"
    elif animal == "horse":
        noise = "neigh"
    elif animal == "cow":
        noise = "moo"
    else:
        noise = "Don't know what noise this animal makes"

    return Response(noise, mimetype='text/plain')
