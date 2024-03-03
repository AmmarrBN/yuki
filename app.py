from flask import Flask, request, make_response, jsonify, redirect, url_for, render_template, send_file, send_from_directory
from flask_restful import Resource, Api, reqparse

app = Flask(__name__) 
api = Api(app)

@app.route('/')
def index_bak():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
