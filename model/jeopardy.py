from flask import Flask, jsonify

app = Flask(name)

questions = [
    {
        'category': 'History',
        'question': 'Who was the first president of the United States?',
        'answer': 'George Washington'
    },
    {
        'category': 'Science',
        'question': 'What is the chemical symbol for hydrogen?',
        'answer': 'H'
    }
]

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})

if name == 'main':
    app.run(debug=True)