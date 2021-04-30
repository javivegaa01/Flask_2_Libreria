import os
import json
from flask import Flask, render_template,abort
app = Flask(__name__)	

with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",libros=datos)

@app.route('/libro/<isbn>',methods=["GET","POST"])
def libros(isbn):
    for libro in datos:
        if "isbn" in libro.keys() and isbn==libro["isbn"]:
	        return render_template("libros.html",libro=libro)
    abort(404)

@app.route('/categoria/<categoria>',methods=["GET","POST"])
def categoria(categoria):
    for libro in datos:
        if "categories" in libro.keys() and categoria in libro["categories"]:
	        return render_template("categorias.html",libros=datos,categoria=categoria)
    abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)