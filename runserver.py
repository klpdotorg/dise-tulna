#!/usr/bin/env python
from disetulna import app
from disetulna.models import db
from os import environ

# environ['PEOPLEFLOW_ENV'] = 'dev'

if __name__=='__main__':
    db.create_all()
    app.config['ASSETS_DEBUG'] = True
    app.run('0.0.0.0', 8000, debug=True)