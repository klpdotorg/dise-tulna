from disetulna.models import db

class Match(db.Model):
    __tablename__ = 'match'
    dise_code = db.Column(db.Numeric(20,0), primary_key=True)
    dise_name = db.Column(db.String(200))
    klp_code = db.Column(db.Numeric(20,0))
    klp_name = db.Column(db.String(200))
    klp_dise_code = db.Column(db.Numeric(20,0))
    flag = db.Column(db.Numeric(10,0))


    def __init__(self, dise_code, dise_name, klp_code, klp_name, klp_dise_code, flag):
        self.dise_code = dise_code
        self.dise_name = dise_name
        self.klp_code = klp_code
        self.klp_name = klp_name
        self.klp_dise_code = klp_dise_code
        self.flag = flag

