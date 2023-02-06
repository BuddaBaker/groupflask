

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
        'category': 'Science',
        'question': 'What is the chemical symbol for hydrogen?',
        'answer': 'H'
    },
]

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})

if name == 'main':
    app.run(debug=True)