import sqlite3

def add_to_table(username, password):
	db = get_db_connection()
	check_user = db.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,)).fetchone()[0]
	if check_user > 0:
		return False
	db.execute('INSERT INTO users (username, password) VALUES (?, ?)',
				(username, password))
	db.commit()
	db.close()
	return True

def get_db_connection():
	connection = sqlite3.connect('database.db')
	return connection

def verify_login_data(db, username, password):
	login = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
	db.close()
	return login

def delete_account(user):
	db = get_db_connection()
	db.execute('DELETE FROM users WHERE username = ?', (user,))
	db.commit()
	db.close()

def update_password(new_pass, password):
	try:
		db = get_db_connection()
		cursor = db.cursor()
		cursor.execute('UPDATE users SET password = ? WHERE password = ?', (new_pass, password))
		db.commit()
		db.close()
		return True
	except:
		return False


# def execute_db_query(query, variables_tuple):
# 	db = sqlite3.connect('database.db')
# 	cursor = db.cursor()
# 	result = cursor.execute(query, variables_tuple)
# 	return result
