from flask import Flask
from flask_script import Manager
import logging

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    logging.getLogger('rtmp').debug('xxx')
    return 'Hello World!'


if __name__ == '__main__':
    import logging
    from logging.config import fileConfig
    fileConfig('logging.conf')
    try:
        manager.run()
    except KeyboardInterrupt:
        logging.getLogger('rtmp').debug('rtmp services exit')
