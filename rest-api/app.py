from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os 
from flask import render_template, redirect, request 

dir_path = os.path.dirname(os.path.realpath(__file__))
e = create_engine('sqlite:///students.db')
app = Flask(__name__)
app.STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__),'static'),
)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/age")
def age_dis():
	conn = e.connect()
	query = conn.execute("select distinct AGE from students")
	rows  = [i for i in query.cursor.fetchall()]
	return render_template("age.html",rows = rows)

@app.route("/age_name")
def age_name():	
	conn = e.connect()
	query = conn.execute("select NAME,AGE from students")
	rows = [i for i in query.cursor.fetchall()]
	return render_template("agedisplay.html",rows = rows)


if __name__ == '__main__':
	app.run(debug=True)