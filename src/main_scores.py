from flask import Flask, jsonify, render_template
from score import add_score, get_current_score

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "price": 10.99},
    {"id": 2, "name": "Item 2", "price": 20.99}
]

@app.route('/ping', methods=['GET'])
def test():
    return jsonify(items)

@app.route('/', methods=['GET'])
def score_server():
    score = get_current_score()
    return render_template('index.html', score=score)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
