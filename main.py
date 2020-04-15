from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

from flask_login import (LoginManager, login_user,
                            logout_user,login_required,current_user,
                            UserMixin)

from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")

db=SQLAlchemy(app)

bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    email=db.Column(db.String,unique=True)
    password=db.Column(db.String)

    def __repr__(self):
        return '<User {}>'.format(self.name)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


db.init_app()



@app.route("/signup",methods=['GET',"POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('users'))
    if request.method =='POST':
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']

        email_exists = db.session.query(db.exists().where(
            User.email == email)).scalar()
        if email_exists:
            return render_template("signup.html",error="EMAIL EXISTS")

        username_exists = db.session.query(db.exists().where(
            User.name == username)).scalar()
        if username_exists:
            return render_template("signup.html",error="USERNAME EXISTS")

        hash_password=bcrypt.generate_password_hash(password)

        user = User(name=username,password=hash_password,email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
        # handle post request here
    return render_template('signup.html')

@app.route("/login",methods=['get','post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users'))
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        email_exists = db.session.query(db.exists().where(
            User.email == email)).scalar()
        if email_exists:
            user = User.query.filter_by(email=email)
            if bcrypt.check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('users'))
            return render_template('login.html',error='Wrong password or email address')



        return render_template("login.html",error="EMAIL DOESN'T EXIST")


    return render_template('login.html')

@app.route("/user")
def users():
    if current_user.is_authenticated:
        return current_user.email
    return redirect(url_for('login'))

if __name__ =="__main__":
    app.run()
