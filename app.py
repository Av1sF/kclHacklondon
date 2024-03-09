'''
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
    return render_template('index.html')


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
'''


from flask import Flask, request, redirect, url_for, flash, render_template, send_file
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.secret_key = 'your_secret_key'

# upload file
UPLOAD_FOLDER = '/Users/chentingting/Desktop/Hackathon/kclHacklondon'
ALLOWED_EXTENSIONS = {'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))



if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
