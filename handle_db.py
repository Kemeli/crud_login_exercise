import sqlite3

def get_db_connection():
	connection = sqlite3.connect('database.db')
	return connection


def add_to_table(username, password):
	query_select = "SELECT COUNT(*) FROM users WHERE username = ?"
	db = get_db_connection()
	check_user = db.execute(query_select, (username,)).fetchone()[0]
	if check_user > 0:
		return False
	query_insert = 'INSERT INTO users (username, password) VALUES (?, ?)'
	db.execute(query_insert, (username, password))
	db.commit()
	db.close()
	return True


def verify_login_data(username, password):
	db = get_db_connection()
	query = 'SELECT * FROM users WHERE username = ? AND password = ?'
	login = db.execute(query, (username, password)).fetchone()
	db.close()
	return login

def delete_account(user):
	query = 'DELETE FROM users WHERE username = ?'
	return execute_db_query(query, (user,))


def update_password(new_pass, password):
	query = 'UPDATE users SET password = ? WHERE password = ?'
	return execute_db_query(query, (new_pass, password))


def execute_db_query(query, variables_tuple):
	db = get_db_connection()
	try:
		cursor = db.cursor()
		cursor.execute(query, variables_tuple)
		db.commit()
	except:
		print("error")
		return False
	db.close()
	return True

