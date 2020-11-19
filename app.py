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
                return "Register Success"
            else:
                conn.rollback()
                print (data)
                return "Register Failed"
        
        
        cursor.close()
        conn.close()
    return render_template('manager/register.html', error=error)
