from flask import render_template
from app import app

@app.route("/")
def Home_page():
    return render_template('index.html')

@app.route("/signup")
def Signup_page():
    return render_template('signup.html')

@app.route("/topfive")
def topfive_page():
    people = ['BTS', 'Jay Park', 'Paul Blanco', 'Steph Curry', 'James Harden']
    images = [
        'blanco.jpg'
        'Bts.jpg'
        'harden.jpg'
        'Jaypark.jpg'
        'steph.jpg'
    ]
    return render_template('topfive.html', p = people, i = images)