#Homework 2
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'May 12, 1984'

@app.route('/greeting/<Name>')
def greeting(Name):
    return 'Hello' + Name
    
#Extra Credit    
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return str(num1 * num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@app.route('/favoritefoods')
def favoritefoods():
    return jsonify('Chicken', 'Pizza', 'Nachos')
    