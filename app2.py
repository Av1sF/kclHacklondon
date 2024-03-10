# socketIO Flask server
from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO
import requests

unitTopic = {
    
    "CCP":"""Find resources on the internet that are primarily related to structure and function of a processor, types of processor, input, output and storage, give links for A-level related resources for students""", 

    "SSD":"""Find resources on the internet that are primarily related to system software, application deneration, software development and types of programming languages, give links for A-level related resources for students""",
    
    "ED" :"""Find resources on the internet that are primarily related to compression, encryption and hashing, databases, networks and web technologies, give links for A-level related resources for students""",
   
    "DDA": """Find resources on the internet that are primarily related to boolean algebra, data types and data structures, give links for A-level related resources for students""",
    "LMCE":"""Find resources on the internet that are primarily related to computing-related legislation and moral and ethical issues, give links for A-level related resources for students""",

    "ECT": """Find resources on the internet that are primarily related to elements of computational thinking, give links for A-level related resources for students"""
}

API_URL = "https://www.stack-inference.com/inference/v0/run/3d4904b4-95d8-4f91-8413-598cd6ad6e28/65ec7764f55f2d6ba176042d"
headers = {'Authorization':
			 'Bearer d6c868e4-dd77-433a-b8f6-40264a0fd870',
			 'Content-Type': 'application/json'
		}

"""
Processing functions 
"""
def processMock(form):
    name = request.form['Name']
    email = request.form['Email']
    msg = request.form['Message']

    return (name, email, msg)

def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

def getResource(prompt):
    return query({"in-0":prompt,
                "user_id":"""d6c868e4-dd77-433a-b8f6-40264a0fd870"""})
    





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
    topic = ""

    if request.method == 'POST':
        form = request.form
        mockResults = processMock(form)
        # if request.form['submit_button'] == 'form':
            

        # elif request.form['submit_button'] == 'initalise':
        #     initaliseMock = True

        # elif request.form['submit_button'] in list(unitTopic.keys()):
        #     print(request.form['submit_button'])
        #     topics = unitTopic.get(request.form['submit_button'])
        #     prompt = """Find resources on the internet that are primarily related to "+ topics +", give links for A-level related resources for students"""
        #     topic = getResource(prompt)

    return render_template('home.html', mockResults=mockResults, 
                           initaliseMock=initaliseMock, topic=topic)


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