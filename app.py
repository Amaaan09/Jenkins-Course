from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'message': 'Welcome to the Flask API!'}

@app.route('/<name>')
def hello_name(name):
    return {'message': f'Hello, {name}!'}


if __name__ == '__main__':
    app.run()