from flask import Flask,request,render_template
import pickle
from task_1 import  registration

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name1)

@app.route('/form_register',methods=['POST','GET'])
def register():
    name1=request.form['username_registration']
    pwd=request.form['password_registration']
    list_login_pass = [name1, pwd]
    return render_template('login.html', info=registration(list_login_pass))


if __name__ == '__main__':
    app.run()
