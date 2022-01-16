from flask import Flask,request,render_template
import pickle
from task_1 import  registration, check_user

app = Flask(__name__)
#app.run(ssl_context = ("SSC.crt", "private.key", "pass.bin"))
app.run(ssl_context = ("SSC.crt", "private.key"))


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    user_to_check = request.form['user_to_check']
    list_login_pas_usertocheck = [name1, pwd, user_to_check]
    return render_template('login.html', info=check_user(list_login_pas_usertocheck))


@app.route('/form_register',methods=['POST','GET'])
def register():
    name1=request.form['username_registration']
    pwd=request.form['password_registration']
    home_city = request.form['home_city_registration']
    phone_number = request.form['phone_number_registration']
    list_login_pass_homecity_phonenumber = [name1, pwd, home_city, phone_number]
    return render_template('login.html', info=registration(list_login_pass_homecity_phonenumber))


if __name__ == '__main__':
    app.run()
