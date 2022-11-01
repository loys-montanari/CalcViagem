import re
from turtle import distance
from unittest import result
from flask import Flask, render_template, request, redirect,json
import requests

app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():
        
    return render_template('index.html')


@app.route("/", methods=['POST'])
def resultado():
        # JSON file
        f = open ("Precos.json", "r").readlines()[0]
        valores = json.loads(f)
        gasolina = float(valores["preco"]["valor"])
        
        consumo = request.form.get('consumo')
        distancia = request.form.get('distancia') 
        distancia = float(distancia) 
        consumo = float(consumo) 
        result = round((distancia/consumo)*gasolina,2)
        return render_template('index.html', consumo=consumo, distancia=distancia, result=result)