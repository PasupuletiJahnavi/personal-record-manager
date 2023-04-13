#first route
''''
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
app.run(debug=True)
''''''
#second route
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
@app.route('/second')
def second():
    return 'i am in codegnan'
app.run(debug=True,use_reloader=True)
''''''
#another method(when we passing arguments)
from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
@app.route('/second')
def second():
    print(request.method)
    print(request.args['user'])
    return 'i am in codegnan'
app.run(debug=True,use_reloader=True)
'''
#####################
from flask import Flask,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
@app.route('/input/<name>/<place>')
def input(name,place):
    return redirect(url_for('second',user=name,city=place))
@app.route('/details')
def second():
    user=request.args.get('user')
    city=request.args.get('city')
    return f'hello,{user} you are in {city}'
app.run(debug=True,use_reloader=True)



