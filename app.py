from flask import Flask, render_template, request, redirect ,url_for
import pymysql

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('manager/index.html')


@app.route('/login', methods=['post', 'get'])
def login():
    error = None
    if request.method == 'POST':
        
        email = request.form['email']
        pw = request.form['password']

        print(email,pw)
        
        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='flask_test', charset='utf8')
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
            return redirect(url_for('home', username=data))
        else:
            error = 'Invalid input data detected!'
            
        #return redirect(url_for('success', name=user))
    
    return render_template('manager/login.html', error=error)
@app.route('/register', methods=['post', 'get'])
def regist():
    error = None
    if request.method == 'POST':
        
        name = request.form['username']
        email = request.form['email']
        pw = request.form['password']
        
        print (name, email, pw)
        
        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='flask_test', charset='utf8')
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
                return "Register Success"
            else:
                conn.rollback()
                print (data)
                return "Register Failed"
        
        
        cursor.close()
        conn.close()
    return render_template('manager/register.html', error=error)
    
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
### Routes for customer part end ###

### Routes for manager part start ###
@app.route('/manager')
@app.route('/manager/')
@app.route('/manager/index')
def mindex():
    return render_template('manager/index.html')

@app.route('/manager/charts')
def mcharts():
    return render_template('manager/charts.html')

@app.route('/manager/customer')
def mcustomer():
    return render_template('manager/customer.html')

@app.route('/manager/employee')
def memployee():
    return render_template('manager/employee.html')

@app.route('/manager/login')
def mlogin():
    return render_template('manager/login.html')

@app.route('/manager/parking')
def mparking():
    return render_template('manager/parking.html')

@app.route('/manager/password')
def mpassword():
    return render_template('manager/password.html')

@app.route('/manager/product')
def mproduct():
    return render_template('manager/product.html')

@app.route('/manager/profile')
def mprofile():
    return render_template('manager/profile.html')

@app.route('/manager/pure')
def mpure():
    return render_template('manager/pure.html')

@app.route('/manager/register')
def mregister():
    return render_template('manager/register.html')

@app.route('/manager/reservation')
def mreservation():
    return render_template('manager/reservation.html')

@app.route('/manager/room')
def mroom():
    return render_template('manager/room.html')

@app.route('/manager/survey')
def msurvey():
    return render_template('manager/survey.html')

@app.route('/manager/task')
def mtask():
    return render_template('manager/task.html')
### Routes for manager part end ###

if __name__ == '__main__':
    app.run(debug=True)

