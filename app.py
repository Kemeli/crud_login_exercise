from flask import Flask, render_template, request, redirect, url_for, jsonify
from handle_db import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

user = ''

@app.route('/login', methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		global user
		user = request.form['username']
		password = request.form['password']
		if verify_login_data(user, password):
			return redirect(url_for('home'))
		else:
			return render_template("login.html", message="invalid user or password")
	else:
		return render_template("login.html")


@app.route('/signup', methods=('GET', 'POST'))
def signup():
	if request.method == 'POST':
		login = request.form['username']
		password = request.form['password']
		if add_to_table(login, password) == False:
			return render_template("signup.html", message="username not available")
		return redirect(url_for('login'))
	else:
		return render_template("signup.html")


@app.route('/home', methods=('GET', 'POST'))
def home():
	return render_template("home.html")


@app.route('/update', methods=('GET', 'POST'))
def update():
	if request.method == 'POST':
		password = request.form['password']
		new_pass = request.form['new_password']
		if update_password(new_pass, password):
			return render_template("login.html", message="password succesfully updated")
		else:
			return render_template("update.html", message="error, wrong password")
	return render_template("update.html")


@app.route('/delete', methods=('GET', 'POST'))
def delete():
	if request.method == 'POST':
		delete_account(user)
		return redirect(url_for('index'))


if __name__ == "__main__":
	app.run(debug=True)
