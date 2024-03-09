# socketIO Flask server
from flask import Flask, render_template, send_file
from flask_socketio import SocketIO

"""
Flask server 
"""

# initiate flask and socketio 
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'fLd+D8YQ&i' 
sio = SocketIO(app)

# templates to serve for each webpage 

@app.route('/')
def home_page():
    return render_template('home.html')


"""
SocketIO event handlers 
socketIO basically allows data to be passed from flask to python
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