from app import app
from flask import render_template
import sqlite3 as sql

@app.route('/')
@app.route('/index')
def index():
	with sql.connect('handshake-interview.db') as conn:
		conn.row_factory = sql.Row
		curr = conn.cursor()
		curr.execute("SELECT * from alarms")
		rows = curr.fetchall()
		return render_template('index.html', alarms=rows)
	