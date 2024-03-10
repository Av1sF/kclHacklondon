# socketIO Flask server
from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO
import requests
import os



unitTopic = {
    
    "CCP":"structure and function of a processor, types of processor, input, output and storage", 

    "SSD":"system software, application deneration, software development and types of programming languages",
    
    "ED" :"compression, encryption and hashing, databases, networks and web technologies",
   
    "DDA": "boolean algebra, data types and data structures",
    "LMCE":"computing-related legislation and moral and ethical issues",

    "ECT": "elements of computational thinking"
}



"""
API keys 
"""

# StackAI/perplexity API 
# another interface is used because perplexity AI tokens limit is lower 
PERPLEX_API_URL = "https://www.stack-inference.com/inference/v0/run/3d4904b4-95d8-4f91-8413-598cd6ad6e28/65ec7764f55f2d6ba176042d"
perplex_headers = {'Authorization':
			 'Bearer d6c868e4-dd77-433a-b8f6-40264a0fd870',
			 'Content-Type': 'application/json'
		}

#StackAI API
API_URL = "https://www.stack-inference.com/inference/v0/run/87a0f031-97dd-4577-a4c9-93c4ae154122/65ed800431b5c269a6c0b018"
headers = {'Authorization':
			 'Bearer 5064899d-f14e-4837-877f-e2b700d63f70',
			 'Content-Type': 'application/json'
		}

"""
Processing functions 
"""

# process user's mock answers 
def processMock(form):

    ans1 = request.form['q1']
    ans2 = request.form['q2']
    ans3 = request.form['q3']

    answers = f"{ans1}, {ans2}, {ans3}"

    # concatenate lines in file into  string
    file = open(os.path.abspath("knowledgebase\\11.1.1. Structure and Function of the Processor"),'r')
    context=''
    for x in file:
        context+=x

    # query StackAI to compare student answers to markscheme, identify weak areas; providing a summary on weak topics.  
    output = query({"string-1":answers,'int-0':'Generate 3 A level type question with options','in-0':"Give a detailed summary of all the topics"
                    ,'string-0':context})
 
    return (output['outputs']['out-2'],output['outputs']['out-0'] )

# query with perplexity AI 
def plex_query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

# query with stackAI
def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

# Suggests and provides resources to user about specific topics of an 
def getResource(prompt):

    # concatenate lines in file into single string
    file = open(os.path.abspath("knowledgebase\\163.4. Searching Algorithms - Concise"), encoding='utf-8')
    context=''
    for x in file:
        context+=x

    # query genAI to generate a list of suitable resources 
    output = query({"in-1":"Find A-level resources (including links) for the following topics",'string-0':context,
                "user_id":"""<USER or Conversation ID>"""})
    
    return (output['outputs']['out-1'])


"""
Flask server 
"""

# initiate flask and socketio 
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'fLd+D8YQ&i' 
sio = SocketIO(app)

# templates to serve for each webpage 

# main page
@app.route('/', methods=['GET', 'POST'])
def index():
    # function handles form data from mocks only
    mockResults = False
    topic = False

    if request.method == 'POST':
        form = request.form
        mockResults = processMock(form)

    return render_template('test.html', mockResults=mockResults, topic=topic)

@app.route('/topic', methods=['GET', 'POST'])
def topic():
    # function only handles form data from the topic subsection 
    mockResults = False 
    topic = False

    if request.method == 'POST':
        form = request.form
        topics = unitTopic.get(request.form['submit_button'])
        topic = getResource(topics)
        topic = [i for i in topic]
        for i in range(0, len(topic)-1, 112):
            topic.insert(i, "\n")
        topic = ''.join(e for e in topic)
        print(topic)

    return render_template('test.html', mockResults=mockResults, topic=topic)


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