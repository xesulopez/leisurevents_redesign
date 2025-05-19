
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/events/spain')
def event_spain():
    return render_template('event_spain.html')

@app.route('/events/monaco')
def event_monaco():
    return render_template('event_monaco.html')

@app.route('/events/canada')
def event_canada():
    return render_template('event_canada.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
