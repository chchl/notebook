from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    import logging
    try:
        manager.run()
    except KeyboardInterrupt:
        logging.debug('rtmp services exit')