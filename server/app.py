#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return f'<h1>{text}</h1>'

@app.route('/count/<int:num>')
def count(num):
    numbers = '<br>'.join(str(i) for i in range(1, num + 1))
    return f'<h1>{numbers}</h1>'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Invalid operation</h1>'

    return f'<h1>Result: {result}</h1>'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
