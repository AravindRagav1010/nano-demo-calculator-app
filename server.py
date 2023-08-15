from flask import Flask, request, jsonify

app = Flask(_name_)


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

if _name_ == '_main_':
    app.run(port=8080,host='0.0.0.0')