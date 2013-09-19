# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for
from .. import app


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		
		return render_template('index.html')
	else:
		print request.form['dise']
		return redirect(url_for('clicked'), code=303)


@app.route('/clicked')
def clicked():
	return render_template('clicked.html')