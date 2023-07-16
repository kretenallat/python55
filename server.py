from flask import Flask
from random import randint

secret_number = randint(0, 9)
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>Guess a number between 0 and 9! Add it to the end of the URL</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='300'>"


@app.route("/<int:number>")
def guess(number):
    if number < secret_number:
        return "<h1>NEED TO GO HIGHERRR!</h1>" \
               "<img src='https://media.giphy.com/media/iIppd7C1OmVNKwuHZB/giphy.gif' width='300'>"
    elif number > secret_number:
        return "<h1>Not so fast.</h1>" \
               "<img src='https://media.giphy.com/media/vexp4GOO5r0OI/giphy.gif' width='300'>"
    elif number == secret_number:
        return "<h1>You win! This time.</h1>" \
               "<img src='https://media.giphy.com/media/haqRLKxKYC79MzCjIC/giphy.gif' width='300'>"


app.run(debug=True)
