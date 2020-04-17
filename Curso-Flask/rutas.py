#importamos flask
from flask import Flask
from flask import request

#nuevo objeto
app =Flask(__name__)

@app.route('/')#wrap o un decorador
def index():#función
    return "hola mundo, helllo"

#?params=1
@app.route('/params')#wrap o un decorador
def param():#función
    param = request.args.get('params1','No contiene este parametro')
    param_dos = request.args.get('params2','No contiene este parametro')
    return "EL parametro es {}, {}".format(param, param_dos)

if __name__ == '__main__':   
    app.run(debug= True, port = 8000 )#ejecuta el servidor por default en el puerto 5000