from flask import Flask
#adding comment and committing to validate pipeline
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
