'''
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'iam in first page'
@app.route('/user/<enduser>')
def user(enduser):
    return 'hello {enduser}'
app.run(debug=True,use_reloader=True)
'''



'''
##float

from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'iam in first page'
@app.route('/input/<float:number>')
def user(number):
    return f'the number entered is {number}'
app.run(debug=True,use_reloader=True)
'''


'''
#given a condition whether pass or fail

from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/fail')
def index():
    return 'you are failed'
@app.route('/input/<float:number>')
def user(number):
    if number>=35.0:
        return redirect ('http://127.0.0.1.5000/pass')
    else:
        return redirect ('http://127.0.0.1.5000/fail')

@app.route('/pass)
def third():
    return 'you are passed'
app.run(debug=True,use_reloader=True)
'''

'''
##url page##
from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/fail')
def index():
    return 'you are failed'
@app.route('/input/<float:number>')
def user(number):
    if number>=35.0:
        return redirect (url_for('third'))
    else:
        return redirect (url_for('index'))

@app.route('/pass)
def third():
    return 'you are passed'
app.run(debug=True,use_reloader=True)
''''''
#redirecting  the dynamic to dynamic
from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/userinput/<float:num>')
def uninput(num):

     if num>100:
        return 'invalid marks'
    else:
        return redirect(url_for('user',number=num))
@app.route('/fail')
def index():
    return 'you are failed'

@app.route('/input/<float:number>')
def user(number):
    if number>=35.0:
        return redirect ('http://127.0.0.1.5000/pass')
    else:
        return redirect ('http://127.0.0.1.5000/fail')
@app.route('/pass')
def third():
    return 'you are passed'
app.run(debug=True,use_reloader=True)










