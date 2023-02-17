from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
@app.route('/')
def hiiiiiiiiiiii():
    return "<h1>Привіт пупс</h1>"
@app.route('/add_tov/<int:tovar>/')
def adder(tovar):
    file = open("son.json", "r")
    txt = json.load(file)
    txt.append(tovar)
    file.close()
    file = open("son.json", "w")
    json.dump(txt,file)
    file.close()
    if request.args.get("after") == None:
        return "<meta http-equiv='Refresh' content='0; url=https://vaniademianov.github.io/shop/main'/>"
    else:
        req = request.args.get("after")
        return "<meta http-equiv='Refresh' content='0; url=https://vaniademianov.github.io/" +req + "'/>"
@app.route('/delete_tov/<int:tovar>/')
def deletor(tovar):
    file = open("son.json", "r")
    txt = json.load(file)
    txt.remove(tovar)
    file.close()
    file = open("son.json", "w")
    json.dump(txt,file)
    file.close()
    if request.args.get("after") == None:
        return "<meta http-equiv='Refresh' content='0; url=https://vaniademianov.github.io/shop/cart'/>"
    else:
        req = request.args.get("after")
        return "<meta http-equiv='Refresh' content='0; url=https://vaniademianov.github.io/" +req + "'/>"
@app.route('/showall/')
def showall():
    file = open("son.json", "r")
    txt = json.load(file)

    file.close()
    return jsonify(txt)
@app.route('/clear_cart/')
def clear():
    file = open("son.json", "w")
    json.dump([], file)

    file.close()
    if request.args.get("after") == None:
        return "<meta http-equiv='Refresh' content='0; url=https://vaniademianov.github.io/shop/cart'/>"
    else:
        req = request.args.get("after")
        return "<meta http-equiv='Refresh' content='0; url=https://vaniademianov.github.io/" +req + "'/>"
@app.route('/sina/')
def sina():
    file = open("son.json", "r")
    txt = json.load(file)
    tin = 0
    file.close()

    for text in txt:
        all = decs(text)
        all = all.get_json()
        tin += all[1]
    return str(tin)
@app.route('/describe_element/<int:element>/')
def decs(element):
    info = []
    if element == 1:
        info = ["Вітчим вітчимів, звичайний", 1000, "primo.jfif"]
    if element == 2:
        info = ["Кампудахтер Поліни", 2000, "comuter.jfif"]
    if element == 3:
        info = ["Піца з Маркетопту", 150, "pizza.png"]
    if element == 4:
        info = ["Манікен путіна", 100, "lox.png"]
    if element == 5:
        info = ["Яйце куряче", 10, "egg.png"]
    if element == 6:
        info = ["Мука 1 класу, 1 кг", 300, "flour.png"]
    if element == 7:
        info = ["Сік Садочок мультифрукт, 1 літр", 150, "sik.png"]
    if element == 8:
        info = ["Іграшка L.O.L.", 130, "lol.jfif"]
    if element == 9:
        info = ["Цукор, 1 кг", 30, "sugar.jfif"]
    if element == 10:
        info = ["Бойовий комар, одна штука", 10000, "komar.jpg"]
    info.append(element)
    return jsonify(info)