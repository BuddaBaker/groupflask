
from flask import Flask,jsonify,request

app = Flask(_name_)
questions = [
    {
        'category': 'UFC',
        'question': 'Who won the Welterweight title from Tyron Woodley',
        'answer': 'Kamaru Usman',
        'points' : '100'
    },
    {
        'category': 'UFC',
        'question': 'Who has most title defenses of all time?',
        'answer': 'Demetrius Johnson',
        'points' : '200'
    },
    {    
        'category': 'UFC',
        'question': 'Who was the first UFC Champ from England',
        'answer': 'Michael Bisping',
        'points' : '300'
    },
    {
        'category': 'UFC',
        'question': 'Who beat Connor Mcgregor at UFC 229?',
        'answer': 'Khabib',
        'points' : '400'
    },
    
    {
        'category': 'UFC',
        'question': 'Who has most wins in the UFC all time before a champsionship fight?',
        'answer': 'Jorge Masvidal',
        'points' : '500'
    },
    {
        'category': 'NFL',
        'question': 'Which round was Tom Brady Drafted in?',
        'answer': '6th',
        'points' : '100'
    },
    {
        'category': 'NFL',
        'question': 'Which NFL player has most rings?',
        'answer': 'Tom Brady',
        'points' : '200'
    },
    {    
        'category': 'NFL',
        'question': 'Which team won the first superbowl',
        'answer': 'Packers',
        'points' : '300'
    },
    {
        'category': 'NFL',
        'question': 'Which player retired during halftime',
        'answer': 'Vontae Davis',
        'points' : '400'
    },
    
    {
        'category': 'NFL',
        'question': 'Which overall pick was traded for AJ Brown',
        'answer': '18th',
        'points' : '500'
    },
    {
        'category': 'NBA',
        'question': 'Which team did Kareem Abdul Jabar play for as a rookie',
        'answer': 'Bucks',
        'points' : '100'
    },
    {
        'category': 'NBA',
        'question': 'Who leads in all time assits',
        'answer': 'John Stockton',
        'points' : '200'
    },
    {    
        'category': 'NBA',
        'question': 'When did Lebron leave Cleveland the first time',
        'answer': '2010',
        'points' : '300'
    },
    {
        'category': 'NBA',
        'question': 'Who was the most recent back to back MVP winner',
        'answer': 'Nikola Jokic',
        'points' : '400'
    },
    
    {
        'category': 'NBA',
        'question': 'How many career 3pts has Steph Curry made',
        'answer': '3302',
        'points' : '500'
    }
]

@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/check_answer", methods=["POST"])
def check_answer():
    answer = request.get_json()["answer"]
    for question in questions:
        if answer == question["answer"]:
            return jsonify({"result": "Correct"})
    return jsonify({"result": "Incorrect"})

if name == 'main':
    app.run()
