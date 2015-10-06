from flask import Flask, jsonify
import random

app = Flask(__name__)

#add new terms as new lines, makes it easier to merge in git

words = ['amigo',
         'bra',
         'brah',
         'bro',
         'broski',
         'brotha',
         'brother',
         'bud',
         'buddy',
         'compadre',
         'dawg',
         'dude',
         'guy',
         'hermano',
         'hombre',
         'homeboy',
         'homie',
         'mate',
         'pal']

@app.route('/bro', methods=['GET'], strict_slashes=False)
def broMe():
    return jsonify({'bro': random.choice(words)})

@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run()
