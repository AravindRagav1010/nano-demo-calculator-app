from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'
@app.route("/calculator/add", methods=['POST'])
def add():
    num = request.json
    result = {'result': num['first'] + num['second']}
    return jsonify(result)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num = request.json
    result = {'result':num['first'] - num['second']}
    return jsonify(result)

if __name__ == '_main_':
    app.run(port=8080,host='0.0.0.0')
