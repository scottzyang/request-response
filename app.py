# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!) 

# import the Flask library
from flask import Flask
# set app variable to start writing routes
app = Flask(__name__)

@app.route('/')
def homepage():
    '''Shows a greeting to the user'''
    return '<h1>Are you there, world? It\'s me, Ducky</h1>'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    '''display a message to the user that changes based on their favorite animal'''
    return f'<h1>Wow, {users_animal} is my favorite animal, too!</h1>'

@app.route('/dessert/<users_dessert>')
def desserts(users_dessert):
    '''display a message to user that changes based on favorite dessert'''
    return f'<h1>How did you know that I liked {users_dessert} too?</h1>'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    '''displays funny story using adjective and noun'''
    return f'<h1>That is a really {adjective} {noun}</h1>'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    '''multiplies the two numbers provided and displays results'''
    if number1.isdigit() and number2.isdigit(): 
        return f'<h1>{number1} times {number2} is {int(number1) * int(number2)}</h1>'
    else:
        return f'<h1>Invalid inputs. Please try again by entering 2 numbers!</h1>'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    '''repeats word a number of times'''
    statement = ''
    if n.isdigit():
        number = int(n)
        while number > 0:
            statement += f'{word} '
            number -= 1
        return f'<h1>{statement}</h1>'
    else:
        return f'<h1>Invalid input. Please try again by entering a word and a number!</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=3000)