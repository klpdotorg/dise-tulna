# -*- coding: utf-8 -*-

import csv
from flask import render_template, request, redirect, url_for
from .. import app
from disetulna.models import db, Match


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
        dise = request.form['dise']
        klp = request.form['klp']
        return redirect(url_for('match', dise=dise, klp=klp))


@app.route('/match', methods=['GET'])
def match():
    dise_cluster = request.args['dise']
    klp_cluster = request.args['klp']
    fp1=csv.reader(open('disetulna/static/data/dise-sample.csv','r'),delimiter='|')
    dise_school_ids = Match.query.order_by('dise_code').distinct().all()
    dise_school_ids = [str(row.dise_code).strip() for row in dise_school_ids]
    dise_schools=[row for row in fp1 if row[2].strip() == dise_cluster.strip() and row[3].strip() not in dise_school_ids]
    dise_schools.sort()
    fp2=csv.reader(open('disetulna/static/data/klp-sample.csv','r'),delimiter='|')
    klp_school_ids = Match.query.order_by('klp_code').distinct().all()
    klp_school_ids = [str(row.klp_code).strip() for row in klp_school_ids]
    klp_schools=[row for row in fp2 if row[2].strip() == klp_cluster.strip() and row[3].strip() not in klp_school_ids]
    klp_schools.sort()
    return render_template('match.html', klp_schools=klp_schools, dise_schools=dise_schools)

@app.route('/content', methods=['POST'])
def content():
    dise = request.form['dise_clust']
    klp = request.form['klp_clust']
    dise_code=request.form['dise'].split('|')
    klp_code=request.form['klp'].split('|')
    db.session.add(Match(dise_code[0].strip(), dise_code[1].strip(), klp_code[0].strip(), klp_code[1].strip(), klp_code[2].strip(), 1))
    db.session.commit()
    return url_for('match', dise=dise, klp=klp)


@app.route('/login', methods=['GET'])
def log():
    return render_template('login.html')