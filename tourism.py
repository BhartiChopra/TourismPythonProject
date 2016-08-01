from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourism.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
mail=Mail(app)

app.config.update(
   DEBUG=True,
   #EMAIL SETTINGS
   MAIL_SERVER='smtp.gmail.com',
   MAIL_PORT=465,
   MAIL_USE_SSL=True,
   MAIL_USERNAME = 'bharteechopra3@gmail.com',
   MAIL_PASSWORD = 'gituchopra3'
   )

mail = Mail(app)
class room(db.Model):
   id = db.Column('homeID', db.Integer, primary_key = True)
   accomodation = db.Column(db.String(100))
   size = db.Column(db.String(50))
   bed = db.Column(db.String(200)) 
   info = db.Column(db.String(200))
   location = db.Column(db.String(50))
   wifi= db.Column(db.String(10))
   tv = db.Column(db.String(10))
   bar = db.Column(db.String(10))
   kitchen = db.Column(db.String(10))
   laundry = db.Column(db.String(10))

class person(db.Model):
   id = db.Column('personID', db.Integer, primary_key = True)
   fname = db.Column(db.String(100))
   lname = db.Column(db.String(50))
   phone = db.Column(db.String(200)) 
   email = db.Column(db.String(200))
   card = db.Column(db.String(50))
   cvv= db.Column(db.String(10))
   date = db.Column(db.String(10))
   month = db.Column(db.String(10))
   Ncard = db.Column(db.String(10))
   

def __init__(self,accomodation,size,bed,infor,location,wifi,tv,bar,kithen,laundary):
   self.accomodation=accomodation
   self.size=size
   self.bed=bed
   self.infor=infor
   self.location=location
   self.wifi=wifi
   self.tv=tv
   self.bar=bar
   self.kitchen=kitchen
   self.laundry=laundry

def __init__(self,fname,lname,phone,email,card,cvv,date,month,Ncard):
   self.fname=fname
   self.lname=lname
   self.phone=phone
   self.email=email
   self.card=card
   self.cvv=cvv
   self.date=date
   self.month=month
   self.Ncard=Ncard

@app.route('/')
def show():
   return render_template('index.html')

@app.route('/van', methods=['GET', 'POST'])
def van():
   return render_template('Vancouver.html', methods=['GET', 'POST'])

@app.route('/vic', methods=['GET', 'POST'])
def vic():
   return render_template('victoria.html', methods=['GET', 'POST'])


@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['accomodation'] or not request.form['size'] or not request.form['bed'] or not request.form['info'] or not request.form['location'] or not request.form['wifi'] or not request.form['tv'] or not request.form['bar'] or not request.form['kitchen'] or not request.form['laundry']:
         flash('enter fields', 'error')
      else:
         rooms = room(accomodation=request.form['accomodation'], size=request.form['size'], bed=request.form['bed'], info=request.form['info'], location=request.form['location'], wifi=request.form['wifi'], tv=request.form['tv'], bar=request.form['bar'], kitchen=request.form['kitchen'], laundry=request.form['laundry'])
         
         db.session.add(rooms)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('room-info.html')

 

@app.route('/result')
def result():
   return render_template('result.html', methods=['GET', 'POST'])

@app.route('/account', methods = ['GET', 'POST'])
def account():
   if request.method == 'POST':
      if not request.form['fname'] or not request.form['lname'] or not request.form['phone'] or not request.form['email'] or not request.form['card'] or not request.form['cvv'] or not request.form['date'] or not request.form['month'] or not request.form['Ncard']:
         flash('enter fields', 'error')
      else:
         persons = person(fname=request.form['fname'], lname=request.form['lname'], phone=request.form['phone'], email=request.form['email'], card=request.form['card'], cvv=request.form['cvv'], date=request.form['date'], month=request.form['month'], Ncard=request.form['Ncard'])
         

         msg = Message(
              'Hello, this is a confirmation mail of your room booking',
             sender='bharteechopra3@gmail.com',
             recipients=[request.form['email']])
         msg.body="test"
         mail.send(msg)

         db.session.add(persons)
         db.session.commit()
         flash('Payment Done Successfully !!')
         return redirect(url_for('result'))
   return render_template('transaction.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug=True,host='0.0.0.0',port=5000)


