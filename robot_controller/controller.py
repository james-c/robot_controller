from flask import Flask, render_template, url_for

app = Flask(__name__)

# url_for('static', filename='css/style.css')

@app.route('/')
def index():
    return render_template('index.html')
