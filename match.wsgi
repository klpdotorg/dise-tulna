import socket
import csv
import web
import json
import sys
import os
import traceback
sys.stdout = sys.stderr

abspath = os.path.dirname(os.path.abspath(__file__))
if abspath not in sys.path:
    sys.path.append(abspath)
if abspath+'/templates' not in sys.path:
    sys.path.append(abspath+'/templates')
import settings

os.chdir(abspath)
import settings

render = web.template.render('templates/')

db=web.database(dbn='postgres',user=settings.USERNAME,pw=settings.PASSWORD,db=settings.DBNAME)

urls = (
    '/', 'index',
    '/match','result',
    '/topframe','topframe',
    '/content','content'
)


queryvalues={"disecode":"","disename":"","klpcode":"","klpname":"","klpdisecode":"","district":"","block":"","cluster":""}
application = web.application(urls,globals()).wsgifunc()

class prints:
    def GET(SELF):
        return render.prints()

# class index:
#   def GET(SELF):
#       return render.index(dise_district,dise_block,dise_cluster,klp_district,klp_block,klp_cluster)

class index:

    def GET(SELF):
        fp1=csv.reader(open('data/dise-sample.csv','r'),delimiter='|')
        fp2=csv.reader(open('data/klp-sample.csv','r'),delimiter='|')       
        
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

        return render.index(dise_district,dise_block,dise_cluster,klp_district,klp_block,klp_cluster)

    def POST(self):
        # a = json.loads(clusters)
        dise_cluster = web.input().dise
        klp_cluster = web.input().klp
        # print dise_cluster, klp_cluster
        # print >> sys.stderr, clusters
        fp1=csv.reader(open('data/DISE.csv','r'),delimiter='|')
        dise_school_id=db.query('select distinct dise_code from dise_match_found')
        dise_school_ids=[str(row.dise_code) for row in dise_school_id]
        dise_schools=[row for row in fp1 if row[2].strip() == dise_cluster.strip() and row[3].strip() not in dise_school_ids]

        fp2=csv.reader(open('data/KLP.csv','r'),delimiter='|')
        klp_school_id=db.query('select distinct klp_code from dise_match_found')
        klp_school_ids=[str(row.klp_code) for row in klp_school_id]
        klp_schools=[row for row in fp2 if row[2].strip() == klp_cluster.strip() and row[3].strip() not in klp_school_ids]
        print klp_schools
       
        return render.content(dise_schools, klp_schools)
        # return render.main()
        # raise web.seeother('content', dise_schools, klp_schools)

        
class content:
  # def GET(SELF,dise_cluster,klp_cluster):
    def POST(self):
        # a = json.loads(clusters)
        dise_cluster = web.input().dise
        klp_cluster = web.input().klp
        # print dise_cluster, klp_cluster
        # print >> sys.stderr, clusters
        fp1=csv.reader(open('data/DISE.csv','r'),delimiter='|')
        dise_school_id=db.query('select distinct dise_code from dise_match_found')
        dise_school_ids=[str(row.dise_code) for row in dise_school_id]
        dise_schools=[row for row in fp1 if row[2].strip() == dise_cluster.strip() and row[3].strip() not in dise_school_ids]

        fp2=csv.reader(open('data/KLP.csv','r'),delimiter='|')
        klp_school_id=db.query('select distinct klp_code from dise_match_found')
        klp_school_ids=[str(row.klp_code) for row in klp_school_id]
        klp_schools=[row for row in fp2 if row[2].strip() == klp_cluster.strip() and row[3].strip() not in klp_school_ids]
        #print klp_schools
       
        return render.content(dise_schools, klp_schools)



class result:
    def POST(self):
        inputs=web.input()
        if str(inputs.dise_value)!='' and str(inputs.klp_value)!='':
            queryvalues["disecode"]=str(inputs.dise_value).split("|")[0]
            queryvalues["disename"]=str(inputs.dise_value).split("|")[1]
            queryvalues["klpcode"]=str(inputs.klp_value).split("|")[0]
            queryvalues["klpname"]=str(inputs.klp_value).split("|")[1]
            queryvalues["klpdisecode"]=str(inputs.klp_value).split("|")[2]
            db.query('insert into dise_match_found values($disecode,$disename,$klpcode,$klpname,$klpdisecode)',queryvalues)
            db.query('update dise_match_found set flag=case when cast(klp_dise_code as text) !=trim($disecode) then 1 else 0 end',queryvalues)
        raise web.seeother('/content/'+str(inputs.matched_value).split("|")[0]+'/'+str(inputs.matched_value).split("|")[1])

