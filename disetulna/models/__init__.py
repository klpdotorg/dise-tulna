from flask.ext.sqlalchemy import SQLAlchemy
from disetulna import app

db= SQLAlchemy(app)

from disetulna.models.match import *