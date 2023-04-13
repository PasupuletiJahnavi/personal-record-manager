#first route
'''''
from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
app.run(debug=True,use_reloader=True)
'''
#session log on
''''
from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']
        if user=='admin' and password=='admin':
            return redirect(url_for('home'))
        else:
            return 'wrong password'
    else:
            return render_template('login.html')
@app.route('/home')
def home():
            return render_template('index.html')
app.run(debug=True,use_reloader=True)
'''
#another session
'''
from flask import Flask,render_template,url_for,redirect,request,session
from flask_session import Session
app=Flask(__name__)
app.secret_key='P@supuleti1302'
app.config['SESSION_TYPE']='filesystem'
Session(app)
@app.route('/',methods=['GET','POST'])
def index():
    if session.get('user'):
        return redirect(url_for('home'))
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']
        if user=='admin' and password=='admin':
            session['user']=user
            return redirect(url_for('home'))
        else:
            return 'wrong password'
    else:
            return render_template('login.html')
@app.route('/home')
def home():
    if session.get('user'):
        return render_template('index.html')
    else:
        return redirect(url_for('index'))
                        
app.run(debug=True,use_reloader=True)
''''''
#log out route
from flask import Flask,render_template,url_for,redirect,request,session
from flask_session import Session
app=Flask(__name__)
app.secret_key='P@supuleti1302'
app.config['SESSION_TYPE']='filesystem'
Session(app)
@app.route('/',methods=['GET','POST'])
def index():
    if session.get('user'):
        return redirect(url_for('home'))
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']
        if user=='admin' and password=='admin':
            session['user']=user
            return redirect(url_for('home'))
        else:
            return 'wrong password'
    else:
            return render_template('login.html')
@app.route('/home')
def home():
    if session.get('user'):
        return render_template('index.html')
    else:
        return redirect(url_for('index'))
@app.route('/logout')
def logout():
    if session.pop('user'):
        session.pop('user')
        return  redirect(url_for('index'))
    else:
        return 'sesssionalreadt popped'
app.run(debug=True,use_reloader=True)
    

