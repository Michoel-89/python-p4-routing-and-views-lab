#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:num>')
def count(num):
    numbers = [str(n) for n in range(num)]
    return '\n'.join(numbers) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
        num1 = int(num1)
        num2 = int(num2)
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
            return 'Invalid operation'
        return str(result)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
