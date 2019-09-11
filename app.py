from random import choice

compliments = ['cute','funny','charming']

def get_compliment():
    compliment = choice(compliments)
    return f'Hello there user! You are so {compliment}!'
