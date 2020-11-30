from flask import Flask, render_template, request, redirect ,url_for, flash, session
from flask_cors import CORS
import pymysql
import time

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

@app.route('/reservation', methods=['post', 'get'])
def reservation():
    print("a")
    error = None
    indate = 0
    outdate = 0
    ind = ""
    outd = ""
    if request.method == 'POST':
        indate = request.form['date']
        outdate = request.form['date1']
    ind += indate[7:11]
    month = indate[3:6]
    if month == "Jan":
        ind += "01"
    elif month == "Feb":
        ind += "02"
    elif month == "Mar":
        ind += "03"
    elif month == "Apr":
        ind += "04"
    elif month == "May":
        ind += "05"
    elif month == "Jun":
        ind += "06"
    elif month == "Jul":
        ind += "07"
    elif month == "Aug":
        ind += "08"
    elif month == "Sep":
        ind += "09"
    elif month == "Oct":
        ind += "10"
    elif month == "Nov":
        ind += "11"
    elif month == "Dec":
        ind += "12"
    ind += indate[0:2]

    outd += outdate[7:11]
    month1 = outdate[3:6]
    if month1 == "Jan":
        outd += "01"
    elif month1 == "Feb":
        outd += "02"
    elif month1 == "Mar":
        outd += "03"
    elif month1 == "Apr":
        outd += "04"
    elif month1 == "May":
        outd += "05"
    elif month1 == "Jun":
        outd += "06"
    elif month1 == "Jul":
        outd += "07"
    elif month1 == "Aug":
        outd += "08"
    elif month1 == "Sep":
        outd += "09"
    elif month1 == "Oct":
        outd += "10"
    elif month1 == "Nov":
        outd += "11"
    elif month1 == "Dec":
        outd += "12"
    outd += outdate[0:2]

    print(int(ind), int(outd))

    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
    cursor = conn.cursor()

    query = "SELECT room_id FROM reservation WHERE (({0} >= check_in_date and {1} <= check_out_date) or ({2} >= check_in_date and {3} <= check_out_date) or ({4} <= check_in_date and {5} >= check_out_date)) ".format (int(ind), int(ind), int(outd), int(outd), int(ind), int(outd))
    #value = (email)
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()

    if data:
        for i in data:
            print(i)

    else:
        print("can reservation")


    query1 = "SELECT room_id from room order by room_id"
    cursor.execute(query1)
    data1 = cursor.fetchall()
    conn.commit()
    arr= []
    for i in data1:
        arr.append(i)

    for i in data:
        for j in arr:
            if i[0] == j[0]:
                arr.remove(i)
    print("ㅡㅡㅡㅡㅡㅡㅡ")

    arr1 = []
    for i in arr:
        jinquery = "select Room_id, Class, room_type, Capacity from room natural join room_info where room_id = {}".format(i[0])
        cursor.execute(jinquery)
        data2 = cursor.fetchall()
        arr1.append(data2)
        conn.commit()

    for i in arr1:
        print(i)

    return render_template('customer/reservation.html', arr1 = arr1)

@app.route('/reservationEng')
def reservationEng():
    return render_template('customer/reservationEng.html')

@app.route('/about')
def about():
    return render_template('customer/about.html')

@app.route('/aboutEng')
def aboutEng():
    return render_template('customer/aboutEng.html')

@app.route('/blog')
def blog():
    return render_template('customer/blog.html')

@app.route('/contact')
def contact():
    return render_template('customer/contact.html')

@app.route('/contactEng')
def contactEng():
    return render_template('customer/contactEng.html')

@app.route('/room-details')
def roomdetails():
    return render_template('customer/room-details.html')

@app.route('/rooms')
def rooms():
    return render_template('customer/rooms.html')

@app.route('/roomsEng')
def roomsEng():
    return render_template('customer/roomsEng.html')

@app.route('/reservationcheck', methods=['post', 'get'])
def reservationcheck():
    error = None
    if request.method == 'POST':

        Reservation_id = request.form['Reservation_id']

        print (Reservation_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT Reservation_id,Customer_Name,Room_id,Class,Room_Type,Capacity,Fee,check_in_Date,Check_Out_Date from Reservation natural join Room_Info where Reservation_id = '%s'" %(Reservation_id)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        if data:
            return render_template('customer/search_cus_reserv.html', data = data)
        else:
            return render_template('customer/search_fail_reserv.html', error = error)

        cursor.close()
        conn.close()


    return render_template('customer/reservationcheck.html')
@app.route('/reservationcheck_1', methods=['post', 'get'])
def reservationcheck_1():
    error = None
    if request.method == 'POST':

        Customer_Name = request.form['Customer_Name']
        Phone_number = request.form['Phone_number']

        print(Customer_Name,Phone_number)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT Reservation_id,Customer_Name,Room_id,Class,Room_Type,Capacity,Fee,check_in_Date,Check_Out_Date from Reservation natural join Room_Info where Phone_number = '%s'"%(Phone_number)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        if data:
            return render_template('customer/search_cus_reserv.html', data = data)
        else:
            return render_template('customer/search_fail_reserv_1.html', error = error)

        cursor.close()
        conn.close()


    return render_template('customer/reservationcheck_1.html')

@app.route('/reservationcheckEng')
def reservationcheckEng():
    return render_template('customer/reservationcheckEng.html')
### Routes for customer part end ###

### Routes for manager part start ###
@app.route('/manager')
@app.route('/manager/')
@app.route('/manager/index')
def mindex():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/index.html')

@app.route('/manager/customer')
def mcustomer():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/customer.html')

@app.route('/manager/employee')
def memployee():
    if not session.get('username'):
        return render_template('manager/login.html')
    db = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
    cur = db.cursor()

    sql = "select Employee_id, Employee_Name  , Gender , Account_Number  , Salary  , On_work , Department , Grade, Room_Floor from Employee natural join Employee_Info order by Salary DESC"
    cur.execute(sql)

    data_list = cur.fetchall()

    return render_template('manager/employee.html', data_list=data_list)


@app.route('/manager/login')
def mlogin():
    session.clear()
    return render_template('manager/login.html')

@app.route('/manager/parking')
def mparking():
    if not session.get('username'):
        return render_template('manager/login.html')

    db = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
    cur = db.cursor()

    sql = "SELECT car_num, room_id, parking_location from parking"
    cur.execute(sql)
    tm = time.strftime('%Y%m%d')
    print (tm)

    data_list = cur.fetchall()
    return render_template('manager/parking.html',data_list = data_list)

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

@app.route('/manager/register')
def mregister():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/register.html')

@app.route('/manager/reservation')
def mreservation():
    if not session.get('username'):
        return render_template('manager/login.html')

    db = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
    cur = db.cursor()

    sql = "select Reservation_id,Room_id,check_in_Date,Check_Out_Date,Customer_Name,Phone_number,Car_num,Parking_location from reservation order by Check_in_Date ASC"
    cur.execute(sql)
    data = cur.fetchall()

    tm = int(time.strftime('%Y%m%d'))



    for i in data:
        if tm == i[3]:
            sql = "delete from reservation where Check_Out_Date = '%s'" %(i[3])
            cur.execute(sql)
            data2 = cur.fetchall()
            db.commit()
            sql2 = "update room set room_on = 0 where Room_id = '%s'" %(i[1])
            cur.execute(sql2)
            data3 = cur.fetchall()
            db.commit()
        elif tm >= i[2] and tm < i[3]:
            print("ok")
            sql = "update room set room_on = 1 where Room_id = '%s'" %(i[1])
            cur.execute(sql)
            data1 = cur.fetchall()
            db.commit()

    cur.close()
    db.close()


    return render_template('manager/reservation.html',data = data)
@app.route('/manager/update')
def mupdate():
    if not session.get('username'):
        return render_template('manager/login.html')
    return render_template('manager/update.html')

@app.route('/manager/room')
def mroom():
    if not session.get('username'):
        return render_template('manager/login.html')
    db = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
    cur = db.cursor()

    sql = "select Room_id, Room_floor, Capacity from room natural join room_info order by Room_id ASC"
    cur.execute(sql)
    tm = time.strftime('%Y%m%d')
    print (tm)

    data_list = cur.fetchall()
    return render_template('manager/room.html',data_list = data_list)

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

        query = "SELECT email FROM userinfo WHERE email = %s AND password = %s"
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

@app.route('/check_id1', methods=['post', 'get'])
def check_id1():
    error = None
    if request.method == 'POST':

        global Employee_id
        Employee_id = request.form['Employee_id']
        print(Employee_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT email FROM userinfo WHERE Employee_id = '%s' " %(Employee_id)
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print(data)
            print("success")
            return render_template('manager/search_email.html', data = data)
        else:
            print("failed")
            return render_template('manager/id_mismatch1.html', error=error)

        cursor.close()
        conn.close()
    return render_template('manager/check_id1.html', error=error)

@app.route('/check_id2', methods=['post', 'get'])
def check_id2():
    error = None
    if request.method == 'POST':

        global Employee_id
        Employee_id = request.form['Employee_id']
        email = request.form['email']
        print(Employee_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT email FROM userinfo WHERE Employee_id = '%s' " %(Employee_id) + "and email = '%s'" %(email)
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print(data)
            print("success")
            return render_template('manager/update_password.html', data = data)
        else:
            print("failed")
            return render_template('manager/id_mismatch1.html', error=error)

        cursor.close()
        conn.close()
    return render_template('manager/check_id2.html', error=error)

@app.route('/manager/update_password', methods=['post', 'get'])
def update_password():
    error = None
    if request.method == 'POST':

        password = request.form['password']

        print(password)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "UPDATE userinfo SET password = '%s'" %(password) + " where Employee_id = '%s'" %(Employee_id)
        cursor.execute(query)
        data = cursor.fetchall()

        print(data)
        conn.commit()

        return render_template('manager/update_success1.html', error=error)

        cursor.close()
        conn.close()
    return render_template('manager/update_password.html', error=error)

@app.route('/check_id', methods=['post', 'get'])
def check_id():
    error = None
    if request.method == 'POST':

        global Employee_id
        Employee_id = request.form['Employee_id']
        print(Employee_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT * FROM Employee WHERE Employee_id = '%s' " %(Employee_id)
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print(data)
            print("success")
            return render_template('manager/register.html', error=error)
        else:
            print("failed")
            return render_template('manager/id_mismatch1.html', error=error)

        cursor.close()
        conn.close()
    return render_template('manager/check_id.html', error=error)

@app.route('/manager/search', methods=['post', 'get'])
def search():
    error = None
    if request.method == 'POST':

        Employee_Name = request.form['Employee_Name']

        print (Employee_Name)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT Employee_id, Employee_Name  , Gender , Account_Number  , Salary  , On_work , Department , Grade, Room_Floor FROM Employee natural join Employee_info WHERE Employee_Name = '%s' " % (Employee_Name)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        if data:
            return render_template('manager/search1.html', data = data)
        else:
            return render_template('manager/search_fail.html', error = error)

        cursor.close()
        conn.close()
    return render_template('manager/search.html', error=error)


@app.route('/manager/search_parking', methods=['post', 'get'])
def psearch():
    error = None
    if request.method == 'POST':

        search_room_id = request.form['search_room_id']

        print (search_room_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT car_num, room_id, parking_location from parking where room_id = '%s'" % (search_room_id)
        cursor.execute(query)
        data_list = cursor.fetchall()
        print(data_list)
        if data_list:
            return render_template('manager/search_success_parking.html', data_list = data_list)
        else:
            return render_template('manager/search_fail_parking.html', error = error)

        cursor.close()
        conn.close()
    return render_template('manager/search_parking.html', error=error)

@app.route('/manager/search_reserv', methods=['post', 'get'])
def search_reserv():
    error = None
    if request.method == 'POST':

        Customer_Name = request.form['Customer_Name']

        print (Customer_Name)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT Room_id,Room_Type,Class,Capacity,Fee,check_in_Date,Check_Out_Date,Customer_Name,Phone_number,Car_num,Parking_location FROM reservation natural join Room_info WHERE Customer_Name = '%s' " % (Customer_Name)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        if data:
            return render_template('manager/search1_reserv.html', data = data)
        else:
            return render_template('manager/search_fail.html', error = error)

        cursor.close()
        conn.close()
    return render_template('manager/search_reserv.html', error=error)

@app.route('/manager/update', methods=['post', 'get'])
def update():
    error = None
    if request.method == 'POST':

        global Employee_id
        Employee_id = request.form['Employee_id']
        print(Employee_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT * FROM Employee WHERE Employee_id = '%s' " %(Employee_id)
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print(data)
            print("success")
            return render_template('manager/update_info.html', error=error)
        else:
            print("failed")
            return render_template('manager/id_mismatch.html', error=error)

        cursor.close()
        conn.close()
    return render_template('manager/update.html', error=error)

@app.route('/manager/update_info', methods=['post', 'get'])
def update_info():
    error = None
    if request.method == 'POST':

        Employee_Name = request.form['Employee_Name']
        Gender = request.form['Gender']
        Account_Number = request.form['Account_Number']
        Salary = request.form['Salary']
        On_work = request.form['On_work']
        Employee_Info_Id = request.form['Employee_Info_Id']

        print(Employee_Name, Gender, Account_Number, Salary, On_work, Employee_Info_Id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "UPDATE Employee SET Employee_Name = '%s'" %(Employee_Name) + ", Gender = '%s'" %(Gender) + ", Account_Number = '%s'" %(Account_Number) + ", Salary = '%s'" %(Salary) + ", On_work = '%s'" %(On_work) + ", Employee_Info_Id = '%s'" %(Employee_Info_Id) + " where Employee_id = '%s'" %(Employee_id)
        cursor.execute(query)
        data = cursor.fetchall()

        print(data)
        conn.commit()

        return render_template('manager/update_success.html', error=error)

        cursor.close()
        conn.close()
    return render_template('manager/update_info.html', error=error)

@app.route('/manager/register', methods=['post', 'get'])
def regist():
    error = None
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']


        print (email, password, Employee_id)

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
            query = "INSERT INTO userinfo (password, email, Employee_id) values (%s, %s, %s)"
            value = (password, email, Employee_id)
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
    return render_template('manager/register.html')

@app.route('/manager/delete', methods=['post', 'get'])
def delete():
    error = None
    if request.method == 'POST':

        email = request.form['email']
        pw = request.form['password']
        Employee_id = request.form['Employee_id']

        print (email, pw, Employee_id)

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
@app.route('/manager/register_info', methods=['post', 'get'])
def regist_info():
    error = None
    if request.method == 'POST':

        Employee_Name = request.form['Employee_Name']
        Gender = request.form['Gender']
        Account_Number = request.form['Account_Number']
        Salary = request.form['Salary']
        On_work = request.form['On_work']
        Employee_Info_Id = request.form['Employee_Info_Id']

        print (Employee_Name, Gender, Account_Number, Salary, On_work, Employee_Info_Id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT 1 FROM Employee WHERE Account_Number = '%s' " % (Account_Number)
        #value = (email)
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print ('user other Account_Number')
            error = "The Account_Number is already used. please use another one"
        else:
            print ('use it okay')
            query = "INSERT INTO Employee (Employee_Name, Gender, Account_Number, Salary, On_work, Employee_Info_Id) values (%s, %s, %s, %s, %s, %s)"
            value = (Employee_Name, Gender, Account_Number, Salary, On_work, Employee_Info_Id)
            cursor.execute(query, value)
            data = cursor.fetchall()
            print (data)
            if not data:
                conn.commit()
                print (data)
                return render_template('manager/register_success1.html', error=error)
            else:
                conn.rollback()
                print (data)
                return render_template('manager/register_fail.html', error=error)


        cursor.close()
        conn.close()
    return render_template('manager/register_info.html', error=error)

@app.route('/manager/delete_info', methods=['post', 'get'])
def delete_info():
    error = None
    if request.method == 'POST':

        Employee_id = request.form['Employee_id']

        print (Employee_id)

        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='jmk', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT Employee_id FROM Employee WHERE Employee_id = '%s' " % (Employee_id)

        cursor.execute(query)
        data = cursor.fetchall()
        print(data)

        if data:
            print("start delete")
            query = "DELETE FROM Employee where Employee_id = %s"
            value = (Employee_id)
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
    return render_template('/manager/delete_info.html', error=error)### Routes for manager part end ###

if __name__ == '__main__':
    app.run()
