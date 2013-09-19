# -*- coding: utf-8 -*-

import csv
from flask import render_template, request, redirect, url_for
from .. import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        fp1=csv.reader(open('disetulna/static/data/dise-sample.csv','r'),delimiter='|')
        fp2=csv.reader(open('disetulna/static/data/klp-sample.csv','r'),delimiter='|')       
        
        dise_district=[]
        dise_block=[]
        dise_cluster=[]
        
        schools=[row for row in fp1]
        for row in schools:
            if row[0] not in dise_district:
                dise_district.append(row[0])
        for row in schools:
            if [row[0],row[1]] not in dise_block:
                dise_block.append([row[0],row[1]])
        for row in schools:
            if [row[1],row[2]] not in dise_cluster:
                dise_cluster.append([row[1],row[2]])

        klp_district=[]
        klp_block=[]
        klp_cluster=[]
        
        schools=[row for row in fp2]
        for row in schools:
            if row[0] not in klp_district:
                klp_district.append(row[0])
        for row in schools:
            if [row[0],row[1]] not in klp_block:
                klp_block.append([row[0],row[1]])
        for row in schools:
            if [row[1],row[2]] not in klp_cluster:
                klp_cluster.append([row[1],row[2]])     
        return render_template('index.html', dise_district=dise_district,dise_block=dise_block,dise_cluster=dise_cluster,klp_district=klp_district,klp_block=klp_block,klp_cluster=klp_cluster)
    else:
        print request.form['dise']
        return redirect(url_for('clicked'), code=303)


@app.route('/clicked')
def clicked():
    return render_template('clicked.html')