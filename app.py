from flask import Flask, jsonify, g 
from flask_cors import CORS

from resources.persons import person

import models

DEBUG = True 
PORT = 8000


app = Flask(__name__)


@app.before_request 
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response 


CORS(person, origins=['http://localhost:3000'], supports_credentials=True) 



app.register_blueprint(person, url_prefix='/api/v1/persons')





# @app.route('/')
# def index():
#     return 'this is a test'


if __name__ == '__main__':
	models.initialize() 
	app.run(debug=DEBUG, port=PORT)