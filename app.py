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

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    '''display a message to the user that changes based on their favorite animal'''
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def desserts(users_dessert):
    '''display a message to user that changes based on favorite dessert'''
    return f'How did you know that I liked {users_dessert} too?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    '''displays funny story using adjective and noun'''
    return f'That is a really {adjective} {noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    '''multiplies the two numbers provided and displays results'''
    if number1.isdigit() and number2.isdigit(): 
        return f'{number1} times {number2} is {int(number1) * int(number2)}'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

if __name__ == '__main__':
    app.run(debug=True, port=3000)