import random
from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>Guess a number betwwen 0 and 9</h1><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXk5NWRheGJxMHQyeHUwZjJxcm5zcnFoZG94MGt4dm1qM2Q4OHY3dyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/AVeaHNlErgf2UxflsL/giphy.webp" />'

@app.route('/<int:guess>')
def guessed(guess):
    answer= random.randint(0,9)
    if guess==answer:
        return '<h1>You got it right<h1><img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzdvc3ZwanN6cjVjaHVucHVsbjB1ZzB6NmI0YTRrbjk4ODdlaGk3NCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/kKeJ4JuNkaEZbkPOOL/giphy.webp"/>'
    elif guess>answer:
        return '<h1>too high, try agin</h1><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzJnc3kyMjhuM3RmNDhtdXEzNXR4NjBybW5tejFhYzR0eXRnYnE2cSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/dETuRKqhouBdDevSAA/giphy.webp"/>'
    elif guess<answer:
        return  '<h1>too low, try agin</h1><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzJnc3kyMjhuM3RmNDhtdXEzNXR4NjBybW5tejFhYzR0eXRnYnE2cSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/dETuRKqhouBdDevSAA/giphy.webp"/>'    

if __name__=="__main__":
    app.run(debug=True)