#!/usr/bin/env python3
from flask import Flask, request, render_template, Response
import os, pickle, base64
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

app = Flask(__name__)
app.secret_key = os.urandom(32)

INFO = ['name', 'username', 'password']

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50000 per hour"],
    storage_uri="memory://",
)


@app.route('/')
def index():
    return render_template('create_session.jinja2')


@app.route('/create_session', methods=['GET', 'POST'])
@limiter.limit("5/second")
def create_session():
    if request.method == 'GET':
        return render_template('create_session.jinja2')
    elif request.method == 'POST':
        info = {}
        for _ in INFO:
            info[_] = request.form.get(_, '')
        try:
            data = base64.b64encode(pickle.dumps(info)).decode('utf8')
        except:
            data = "Invalid data!"
        return render_template('create_session.jinja2', data=data)


@app.route('/check_session', methods=['GET', 'POST'])
@limiter.limit("5/second")
def check_session():
    if request.method == 'GET':
        return render_template('check_session.jinja2')
    elif request.method == 'POST':
        session = request.form.get('session', '')
        try:
            info = pickle.loads(base64.b64decode(session))
        except:
            info = "Invalid session!"
        return render_template('check_session.jinja2', info=info)


@app.route('/source')
def source():
    return Response(open(__file__).read(), mimetype="text/plain")


app.run(host='0.0.0.0', port=1337)