from flask import Flask, render_template, request, redirect, url_for
from forms import Todo
app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

# What kind of request method (GET or POST) you are asking when you call the url
@app.route('/', methods=['GET', 'POST'])
def index():
    request_method = request.method
    if request_method == 'POST': 
        first_name = request.form['first_name']
        return redirect(url_for('name', first_name = first_name))  #Note: we append the url terms with a variable string
    
    return render_template('hello.html', request_method = request_method)

@app.route('/name/<string:first_name>')  # Note: we generate a page based on the variable from the form 
def name(first_name): 
    return f'{first_name}'

@app.route('/todo', methods=['GET','POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        print(todo_form.content.data)
        return redirect('/')
    return render_template('todo.html', form=todo_form)


if __name__ == '__main__':
    app.run(debug=True)

