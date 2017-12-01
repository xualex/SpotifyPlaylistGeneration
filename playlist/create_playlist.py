
import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util

#Utility function. songList is a list of songIDs, everything else is Spotify data.

def createPlaylist(songList, username, client_id, client_secret, playlist_id, redirect_uri):

    scope = 'playlist-modify-public'
    #Get token
    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        #playlists = sp.user_playlist_create(username, playlist_name,playlist_description)
        #pprint.pprint(playlists)
        results = sp.user_playlist_add_tracks(username, playlist_id, song_List)
        #print(results)
    else:
        print("Can't get token for", username)
