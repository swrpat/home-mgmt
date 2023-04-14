from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Catsarethebest'
Bootstrap(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cozy.db"
db.init_app(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    unit = db.Column(db.String(10), nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(250), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(250), nullable=True)
    vendor = db.Column(db.String(250), nullable=True)
    discount_from = db.Column(db.Float, nullable=True)

class AddForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    date = StringField('Bought on', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    category = StringField('Category')
    vendor = StringField('Vendor')
    discount_from = FloatField('Original Price')
    submit = SubmitField('Add')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grocery/add')
def add():
    return render_template('add.html')

@app.route('/grocery/ts')
def product():
    result = Transaction.query.paginate()
    print(result)
    return render_template('ts.html', query_results=result)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    buy = Transaction(
        date = '2023-02-11',
        product_id = 1,
        price = 40.5,        
    )
    # with app.app_context():
    #     db.session.add(buy)
    #     db.session.commit()

    app.run(debug=True)
    