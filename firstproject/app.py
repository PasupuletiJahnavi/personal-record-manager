from flask import Flask
app=Flask(__name__)
@app.route('/first/<name>')
def home(name):
    print(type(name))
    return f'hello {name}!'
@app.route('/second')
def second():
    return 'I am in second page'
@app.route('/third')
def third():
    return 'I am in third page'
app.run(debug=True,use_reloader=True)


