from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/primos/<num>')
def primos(num):
    if(num<=1):
        print(num , " el numero no es primo")
    else:
        for i in range(2,number):
            if(number  % 1==0):
                cont  = cont +1
        if(cont>1):
            print(num ," el numero no es primo")
        else:
            print(num ," el numero si es primo)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
