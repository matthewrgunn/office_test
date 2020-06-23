# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from collections import Counter
from model import most_frequent
from model import determineChar
from model import returnChar

# from model import determineChar

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    answer_list = []
    name = request.form['name']
    activity = request.form['activity']
    pre = request.form['pre']
    news = request.form['news']
    song = request.form['song']
    series = request.form['series']
 
    answer_list.append(activity)
    answer_list.append(pre)
    answer_list.append(news)
    answer_list.append(song)
    answer_list.append(series)

    answer = most_frequent(answer_list)

    char = determineChar(answer)
    characteristics = returnChar(char)

    if request.method == 'GET':
        return "ERROR!"
    else:
        print(answer_list)
        return render_template('results.html', name = name, char=char, characteristics = characteristics)