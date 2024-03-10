# socketIO Flask server
from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO


"""
Processing functions 
"""
def processMock(form):
    name = request.form['Name']
    email = request.form['Email']
    msg = request.form['Message']

    return (name, email, msg)



"""
Flask server 
"""

# initiate flask and socketio 
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'fLd+D8YQ&i' 
sio = SocketIO(app)

# templates to serve for each webpage 

@app.route('/', methods=['GET', 'POST'])
def index():
    initaliseMock = False
    mockResults = False

    if request.method == 'POST':

        if request.form['submit_button'] == 'form':
            form = request.form
            mockResults = processMock(form)

        elif request.form['submit_button'] == 'initalise':
            initaliseMock = True
            

    return render_template('home.html', mockResults=mockResults, 
                           initaliseMock=initaliseMock)


"""
SocketIO event handlers 
socketIO basically allows data to be passed from flask to python, and vice versa
"""

@sio.on('connect')
def connect():
    print('connected')

@sio.on('disconnect')
def disconnect():
    print('disconnect')



"""
Main 
"""


if __name__ == "__main__":

    # initalise flask server 
    sio.run(app, host='localhost', debug=True)