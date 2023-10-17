"""
John Doe's Flask API.
"""

from configparser import ConfigParser
from flask import Flask, send_from_directory, abort

PORT = 0
DEBUG = False

parser = ConfigParser()
parser.read("credentials.ini")

try:
    PORT = parser["SERVER"]["PORT"]
    DEBUG = parser["SERVER"]["DEBUG"]
except KeyError:
    parser.read("default.ini")
    PORT = parser["SERVER"]["PORT"]
    DEBUG = parser["SERVER"]["DEBUG"]

app = Flask(__name__)

@app.route("/")
def default():
    return send_from_directory("pages/", "trivia.html"), 200

@app.route("/<string:filename>")
def load_page(filename):
    for c in "()_-,/~":
        if c in filename:
            abort(403)
    if(".." in filename):
        abort(403)
    return send_from_directory("pages/", filename), 200

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory("pages/", "403.html"), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory("pages/", "404.html"), 404

if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
