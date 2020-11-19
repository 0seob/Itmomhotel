from flask import Flask, render_template
app = Flask(__name__)

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
