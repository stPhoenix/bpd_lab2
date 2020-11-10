#-*- coding: utf8 -*-

from flask import Flask, request, render_template
from rsa import RSA

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {'error': False, 'message': None, 'data': None, 'action': None}
    if request.method == 'GET':
        return render_template('index.html', name='index', result=result)
    else:
        try:
            result['action'] = request.form['action']
            if request.form['action'] == 'encrypt':
                N = int(request.form['N'])
                E = int(request.form['E'])
                text = request.form['text']
                result['data'] = RSA().encrypt(E, N, text)
            elif request.form['action'] == 'decrypt':
                N = int(request.form['N'])
                D = int(request.form['D'])
                text = request.form['text']
                result['data'] = RSA().decrypt(D, N, text)
                print(result['data'])
            elif request.form['action'] == 'keys':
                result['data'] = RSA().generate_keys()
        except Exception as e:
            result['action'] = ''
            result['error'] = True
            result['message'] = e
        return render_template('index.html', name='index', result=result)