from flask import Flask
from flask import Response
app = Flask(__name__)


@app.route("/health")
def health():
    return Response("{'status': 'ok'}", mimetype='application/json')


if __name__ == "__main__":
    app.run()
