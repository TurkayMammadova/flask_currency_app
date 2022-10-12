from extensions import db
from app import app


class Currency(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    code = db.Column(db.String(4))
    status = db.Column(db.String(50))



    
    def __init__(self, name, code, status):
            self.name = name
            self.code = code
            self.status = status

    def __repr__(self):
            return self.name

    def save(self):
            db.session.add(self)
            db.session.commit()

class CurrencyRate(db.Model):
     id = db.Column( db.Integer(),primary_key=True)
     code = db.Column(db.String(4))
     date = db.Column(db.String(15))
     rate = db.Column(db.String(200))

     def __init__(self,code,date,rate):
        self.code = code
        self.date = date
        self.rate = rate

     def __repr__(self) :
            return self.code

     def save(self):
            db.session.add(self)
            db.session.commit()
