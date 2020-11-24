from flask import Flask, render_template, request, redirect ,url_for, flash, session
from flask_cors import CORS
import pymysql

DEBUG = True
app = Flask(__name__)
# enable CORS
app.config.from_object(__name__)
app.secret_key = 'some_secret'
CORS(app)


### Routes for customer part start ###
@app.route('/')
@app.route('/index')
def index():
    return render_template('customer/index.html')

@app.route('/indexEng')
def indexEng():
    return render_template('customer/indexEng.html')

@app.route('/reservation')
def reservation():
    return render_template('customer/reservation.html')

@app.route('/about')
def about():
    return render_template('customer/about.html')

@app.route('/blog')
def blog():
    return render_template('customer/blog.html')

@app.route('/contact')
def contact():
    return render_template('customer/contact.html')

@app.route('/room-details')
def roomdetails():
    return render_template('customer/room-details.html')

@app.route('/rooms')
def rooms():
    return render_template('customer/rooms.html')

@app.route('/reservationcheck')
def reservationcheck():
    return render_template('customer/reservationcheck.html')
### Routes for customer part end ###

### Routes for manager part start ###
@app.route('/manager')
@app.route('/manager/')
@app.route('/manager/index')
def mindex():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/index.html')

@app.route('/manager/charts')
def mcharts():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/charts.html')

@app.route('/manager/customer')
def mcustomer():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/customer.html')

@app.route('/manager/employee')
def memployee():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/employee.html')

@app.route('/manager/login')
def mlogin():
    session.clear()
    return render_template('manager/login.html')

@app.route('/manager/parking')
def mparking():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/parking.html')

@app.route('/manager/password')
def mpassword():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/password.html')

@app.route('/manager/product')
def mproduct():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/product.html')

@app.route('/manager/profile')
def mprofile():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/profile.html')

@app.route('/manager/pure')
def mpure():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/pure.html')

@app.route('/manager/register')
def mregister():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/register.html')

@app.route('/manager/reservation')
def mreservation():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/reservation.html')

@app.route('/manager/room')
def mroom():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/room.html')

@app.route('/manager/survey')
def msurvey():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/survey.html')

@app.route('/manager/task')
def mtask():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/task.html')

@app.route('/home')
def home():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/index.html')





@app.route('/login', methods=['post', 'get'])
def login():
    error = None
    if request.method == 'POST':

        email = request.form['email']
        pw = request.form['password']

        print(email,pw)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT username FROM userinfo WHERE email = %s AND password = %s"
        value = (email, pw)
        cursor.execute("set names utf8")
        cursor.execute(query, value)
        data = (cursor.fetchall())

        cursor.close()
        conn.close()

        for row in data:
            data = row[0]

        if data:
            print ('login success')
            session['username'] = email
            return redirect(url_for('mindex'))
        else:
            error = 'Invalid input data detected!'
            flash("Login Failed")

        #return redirect(url_for('success', name=user))

    return render_template('manager/login.html', error=error)
@app.route('/manager/register', methods=['post', 'get'])
def regist():
    error = None
    if request.method == 'POST':

        name = request.form['username']
        email = request.form['email']
        pw = request.form['password']

        print (name, email, pw)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT 1 FROM userinfo WHERE email = '%s' " % (email)
        #value = (email)
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print ('user other email')
            error = "The email is already used. please use another one"
        else:
            print ('use it okay')
            query = "INSERT INTO userinfo (username, password, email) values (%s, %s, %s)"
            value = (name, pw, email)
            cursor.execute(query, value)
            data = cursor.fetchall()
            print (data)
            if not data:
                conn.commit()
                print (data)
                return render_template('manager/register_success.html', error=error)
            else:
                conn.rollback()
                print (data)
                return render_template('manager/register_fail.html', error=error)


        cursor.close()
        conn.close()
    return render_template('manager/register.html', error=error)

@app.route('/manager/delete', methods=['post', 'get'])
def delete():
    error = None
    if request.method == 'POST':

        name = request.form['username']
        email = request.form['email']
        pw = request.form['password']

        print (name, email, pw)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT id FROM userinfo WHERE email = '%s' " % (email)

        cursor.execute(query)
        data = cursor.fetchall()
        print(data)

        if data:
            print("start delete")
            query = "DELETE FROM userinfo where email = %s "
            value = (email)
            cursor.execute(query,value)
            data = cursor.fetchall()
            print (data)
            if not data:
                conn.commit()
                print (data)
                return render_template('manager/delete_success.html', error=error)
            else:
                conn.rollback()
                print (data)
                return render_template('manager/delete_fail.html', error=error)
        else:
            print("NO")
            return render_template('manager/delete_fail.html', error=error)


        cursor.close()
        conn.close()
    return render_template('/manager/delete.html', error=error)



### Routes for manager part end ###

if __name__ == '__main__':
    app.run()
