#Shout out to drshey
#https://github.com/drshrey/spotify-flask-auth-example

# Import All Neccesary Modules
import json
from flask import Flask, request, redirect, g, render_template
import requests
import base64
import urllib
import urllib.parse

# Authentication Steps, paramaters, and responses are defined at https://developer.spotify.com/web-api/authorization-guide/
# Visit this url to see all the steps, parameters, and expected response.


app = Flask(__name__)

#  Client Keys
CLIENT_ID = "9ace5319778f41bab23efb30e7c19d94"
CLIENT_SECRET = "3c471b527a084c4389e370f4eeee828c"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)


# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)

#Modify Scope to Add in for other functions
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()


auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

@app.route("/")
def index():
    # Auth Step 1: Authorization
    url_args = "&".join(["{}={}".format(key,urllib.parse.quote(val)) for key,val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@app.route("/callback/q")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    temp1 = CLIENT_ID + ":"+ CLIENT_SECRET
    temp2 = temp1.encode('utf-8','strict')
    HEADER_64 = base64.standard_b64encode(temp2)
    PARAMS = {'grant_type':'client_credentials'}				# Requested by Spotify for this particular authorization format
    AUTH_HEADERS = {'Authorization':b'Basic '+HEADER_64}
    r = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=AUTH_HEADERS)
    """
    base64encoded = base64.b64encode(b"{%a}:{%a}"%(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {%a}"%(base64encoded)}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)
    """
    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(r.content)
    access_token = response_data['access_token']
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}

    # Get profile data
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    # Get user playlist data
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    playlist_data = json.loads(playlists_response.text)

    # Combine profile and playlist data to display
    display_arr = [profile_data] + playlist_data["items"]
    return render_template("index.html",sorted_array=display_arr)
    # Grab this data and make a dict of name and id for playlist. Present user with choices of playlist and allow them to choose
    # Grab api for choosen playlist
    # Create array for playlist songs nad info from songs

if __name__ == "__main__":
    app.run(debug=True,port=PORT)
