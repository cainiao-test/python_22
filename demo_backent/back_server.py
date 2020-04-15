from flask import Flask, jsonify, redirect, make_response, Response, Request, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if not request.cookies.get('user'):
        return 'login'
    return jsonify({"msg": "hello world"})


@app.route('/login', methods=['GET', 'POST'])
def login():
    resp = Response('login success')
    resp.set_cookie('user', 'yuz')
    return resp


app.run(debug=True)
