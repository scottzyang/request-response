# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!) 

# import the Flask library
from flask import Flask
# set app variable to start writing routes
app = Flask(__name__)

@app.route('/')
def homepage():
    '''Shows a greeting to the user'''
    return 'Are you there, world? It\'s me, Ducky'

if __name__ == '__main__':
    app.run(debug=True)