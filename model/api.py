from flask import request
from __main__ import app
@app.route('/api/jeopardy')
def data():
    category = request.args.get('category')
    points = request.args.get('points')
    print(category,points)
