from flask import Flask
import random

app = Flask(__name__)

words = ['amigo','bra','brah','bro','broski','brotha','brother','bud','buddy','compadre','dawg','dude','guy','homeboy','homie','mate','pal']

@app.route('/bro')
def broMe():
    return random.choice(words)
if __name__ == '__main':
    app.run()
