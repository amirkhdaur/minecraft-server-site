from flask import Flask, Response, render_template
from minecraft_status import get_status
from timeweb import Timeweb

app = Flask(__name__)

timeweb = Timeweb()


@app.route('/')
def index():
    status = get_status()
    server = timeweb.get_server()
    return render_template('index.html', status=status, server=server)


if __name__ == '__main__':
    app.run(host='localhost')