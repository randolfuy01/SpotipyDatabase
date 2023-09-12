from flask import Flask, session, url_for, redirect, request
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import time

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'Cookie'
app.secret_key = 'asdjkvsdcxmnaslkjjf^74'
TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('saveTopSongs', external = True))


@app.route('/saveTopSongs')
# Get the rest of the top songs saved
def saveTopSongs():

    try:
        token_info = getToken()
    except:
        print("User not logged in")
        return redirect('/')

def getToken():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external = False))
    now = int(time.time)
    expired_token = token_info['expires_at'] - now < 60
    if(expired_token):
        spotify_oauth = SpotifyOAuth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(client_id= "86a30b295d3d4a7db3f98f4048a45a69", 
                        client_secret= "ea80109390c24cf6b48a9f36c28d3be2",
                        redirect_uri=url_for('/redirect', _external = True),
                        scope = 'user-top-read'
                        )


app.run(debug=True)