#registration
'''
from flask import Flask,render_template,url_for,redirect,request,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='P@supuleti1302'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='stu'
Session(app)
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def registration():
    if request.method=='POST':
        id=request.form['id']
        name=request.form['name']
        course=request.form['course']
        address=request.form['address']
        mobile=request.form['mobile']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into stu values(%s,%s,%s,%s,%s)',(id,name,course,address,mobile))
        mysql.connection.commit()
        cursor.close()
        return 'Details registered!'
    return render_template('register.html')
app.run(debug=True,use_reloader=True)
'''
#registration2
from flask import Flask,flash,render_template,url_for,redirect,request,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='P@supuleti1302'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='stu'
Session(app)
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('eindex.html')
@app.route('/login')
def login():
    return render_template('login.html')
def home():
    return render_template('eindex.html')
@app.route('/eregistration',methods=['GET','POST'])
def registration():
    if request.method=='POST':
        eid=request.form['eid']
        ename=request.form['ename']
        erole=request.form['erole']
        dept=request.form['dept']
        mobile=request.form['mobile']
        salary=request.form['salary']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s)',(eid,ename,erole,dept,mobile,salary))
        mysql.connection.commit()
        cursor.close()
        flash('Details registered successfully')
        return redirect(url_for('login'))
    return render_template('register1.html')
app.run(debug=True,use_reloader=True)


