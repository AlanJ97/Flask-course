#importamos flask
from flask import Flask
#nuevo objeto
app =Flask(__name__)
@app.route('/')#wrap o un decorador
def index():#función
    return "hola mundo"
app.run()#ejecuta el servidor por default en el puerto 5000