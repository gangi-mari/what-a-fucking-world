from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'What a fucking world Heroku_Flask'

if __name__ == '__main__':
    app.run()