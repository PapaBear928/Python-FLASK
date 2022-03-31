from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    discount = db.Column(db.Integer)
    active = db.Column(db.Boolean)

    products = db.relationship('Product', backref='vendor', lazy='dynamic')

    def __repr__ (self):
        return 'Vendor: {} / {}'.format(self.id, self.name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))

    def __repr__ (self):
        return 'Prod: {}/ {}'.format(self.id, self.name)

@app.route('/')
def index():
    db.create_all()

    #v1 = Vendor(id=1, name='Microsoft', discount=3, active=True)
    #db.session.add(v1)
    #db.session.commit()

    #v2 = Vendor(id=2, name='KluczPOL', discount=-1, active=True)
    #db.session.add(v2)
    #db.session.commit()

    vendors = Vendor.query.all()

    ret = ''
    for v in vendors:
        ret += str(v) + '<br>'

    return 'Hello <br> {} <br>'.format(ret)



    
    


if __name__ == '__main__':
    app.run()