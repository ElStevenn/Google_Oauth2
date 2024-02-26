from flask import Flask, request, redirect
from routes import oauth2_authorization
import os

app = Flask(__name__)
"""
Documentation:
https://developers.google.com/identity/protocols/oauth2/web-server#python_2
https://developers.google.com/identity/protocols/oauth2/web-server
"""

@app.route("/")
def root():
    return "<h1>OAUTH 2 authentication</h1>"


@app.route("/oauth_autentication")
def oauth_authentication():
    return redirect(oauth2_authorization.authorization_url)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
