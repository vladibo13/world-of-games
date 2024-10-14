from flask import Flask, jsonify, render_template
from score import add_score, get_current_score

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def test():
    return jsonify({"healthcheck": "ok"})

@app.route('/', methods=['GET'])
def score_server():
    res = get_current_score()
    if res == -1:
        res = "something went wrong"
    return render_template('index.html', score=res)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4999)
