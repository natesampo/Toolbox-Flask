"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['Name']
        userage = request.form['Age']
        return redirect(url_for('user_profile', username=username, userage=userage))
    return render_template('index.html')

@app.route('/user')
def user_profile():
    return render_template('user.html', name=request.args.get('username'), age=request.args.get('userage'))

if __name__ == '__main__':
    app.run()
