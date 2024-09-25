# se importa el modulo flask desde el paquete flask
from flask import Flask

# crea una instancia de la clase Flask.
# el argumento __name__le dice a Flask
# que utilire del archivo actual main,py
app = Flask(__name__)

# este es un decorador que define una ruta 
#corresponde a la pagina principal de la app
@app.route("/")

# cuando alguien visite app ( por ejemplo , http://localhost:5000/),
# la funcion hello () sera ejecutada
def hello():
    return "<h1>hello,world Flask !</h1>"

# solo se ejecuta si el archivo es ejecutado directamente
#arranca la aplicacion Flask en modo de depracion (debug=true)
if __name__== '__main__':
    app.run(debug=True,port=5000)
