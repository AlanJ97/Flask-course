#importamos flask
from flask import Flask
from flask import request

#nuevo objeto
app =Flask(__name__)

@app.route('/')#wrap o un decorador
def index():#función
    return "hola mundo, helllo"


@app.route('/params/')
@app.route('/params/<name>/')#wrap o un decorador
@app.route('/params/<name>/<int:num>')
def param(name = 'Default name' , num = 'Default num'):#función
    return "EL parametro es {} {}".format(name , num)

if __name__ == '__main__':   
    app.run(debug= True, port = 8000 )#ejecuta el servidor por default en el puerto 5000