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

API_URL1 = "https://www.stack-inference.com/inference/v0/run/87a0f031-97dd-4577-a4c9-93c4ae154122/65ed800431b5c269a6c0b018"
headers1 = {'Authorization':
			 'Bearer 5064899d-f14e-4837-877f-e2b700d63f70',
			 'Content-Type': 'application/json'
		}

"""
Processing functions 
"""
def processMock(form):
    ans1 = request.form['Name']
    ans2 = request.form['Email']
    ans3 = request.form['Message']
    string = f"{ans1}, {ans2}, {ans3}"
    file = open('C:\\Users\\ROG\\kclHacklondon\\txtOutputs\\11.1.1. Structure and Function of the Processor','r')
    str=''
    for x in file:
        str+=x
    output = query1({"string-1":string,'int-0':'Generate 5 A level type question with options','in-0':"Give a detailed summary of all the topics"
                    ,'string-0':str})
    
    print(output['outputs']['out-2'] )
    return (output['outputs']['out-2'],output['outputs']['out-0'] )



def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

def query1(payload):
 response = requests.post(API_URL1, headers=headers1, json=payload)
 return response.json()

def getQuestion():
    output = query1({"in-2": """Generate 5 A-level objective type questions from the following information
(give A ,B,C,D). List all the questions below Add a slash after listing all options to seperate each question from the previous one.""", 
"user_id": """<USER or Conversation ID>"""})
    
    lst = output['outputs']['out-3'].split(" /")
    print(lst)
    return tuple(lst)

def getResource(prompt):
    output = query1({"in-3":prompt,
                "user_id":"""<USER or Conversation ID>"""})
    return (output['outputs']['out-4'])


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
    topic = False
    question = False

    if request.method == 'POST':
        form = request.form
        mockResults = processMock(form)

    return render_template('test.html', mockResults=mockResults, topic=topic, question=question)

@app.route('/topic', methods=['GET', 'POST'])
def topic():
    mockResults = False 
    topic = False
    question = False

    if request.method == 'POST':
        form = request.form
        topics = unitTopic.get(request.form['submit_button'])
        topic = getResource(topics)
        print(topic)

    return render_template('test.html', mockResults=mockResults, topic=topic, question=question)

@app.route('/question', methods=['GET', 'POST'])
def question():
    mockResults = False 
    topic = False
    question = False

    if request.method == 'POST':
        form = request.form
        question = getQuestion()

    return render_template('test.html', mockResults=mockResults, topic=topic, question=question)

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