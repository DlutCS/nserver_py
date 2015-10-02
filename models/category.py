from models import db

class Category(db.Model):

    __tablename__ = 'tbl_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    newses = db.relationship('News', backref='category', lazy='dynamic')

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Category %r>' % self.name

