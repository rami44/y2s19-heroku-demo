# from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('personalproject.html')

if __name__ == '__main__':
    app.run(debug=True)

