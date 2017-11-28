
import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util

import auth_info
import markovPlaylistGen

CLIENT_ID = auth_info.CLIENT_ID
CLIENT_SECRET = auth_info.CLIENT_SECRET
username = auth_info.username
scope = 'playlist-modify-public'

if len(sys.argv) > 1:
    playlist_id = sys.argv[1]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='http://127.0.0.1:5000/callback/q')

track_ids = markovPlaylistGen.sl

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    #playlists = sp.user_playlist_create(username, playlist_name,playlist_description)
    #pprint.pprint(playlists)
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    #print(results)
else:
    print("Can't get token for", username)
