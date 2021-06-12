from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Whats up boss'

@app.route('/<string: name>')
def greet(name): 
    return f'Hello {name}'

if __name__ == '__main__':
    app.run(debug=True)

