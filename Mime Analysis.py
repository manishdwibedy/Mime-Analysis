from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT_NUMBER'] )
