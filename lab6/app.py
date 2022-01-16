from flask import Flask,request,render_template
import pickle
from task_1 import  registration, check_user

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    list_login_pas = [name1, pwd]
    return render_template('login.html', info=check_user(list_login_pas))


@app.route('/form_register',methods=['POST','GET'])
def register():
    name1=request.form['username_registration']
    pwd=request.form['password_registration']
    list_login_pass = [name1, pwd]
    return render_template('login.html', info=registration(list_login_pass))


if __name__ == '__main__':
    app.run()
