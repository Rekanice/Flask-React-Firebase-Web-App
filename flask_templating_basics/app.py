from flask import Flask, render_template

app = Flask(__name__)

# Render a html file & pass variables
@app.route('/')
def index():
    return render_template('hello.html', list_of_names = ['Ho', 'Chris', 'Nick'])

# Pass variables to a page
@app.route('/<string:name>')
def greet(name): 
    return f'Hello {name}'

# Extending a base html
@app.route('/about')
def about(): 
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

