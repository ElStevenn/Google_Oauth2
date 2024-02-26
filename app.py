from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def root():
    return "<h1>OAUTH 2 authentication</h1>"


