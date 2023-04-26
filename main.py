from ytmusicapi import YTMusic
import os
import io

def yt():
    channelID = 'UCrPe3hLA51968GwxHSZ1llw'
    #Verification and creation of headers_auth.json
    if not os.path.exists('headers_auth.json'):
        YTMusic.setup(filepath="headers_auth.json")
    
    ytmusic = YTMusic('headers_auth.json')
    playlist_name = 'Teste'
    playlist_id = ytmusic.create_playlist(playlist_name, description='',privacy_status="PRIVATE")['playlist_id']
    search_results = ytmusic.search('Naquela Mesa')
    #Creation of a Playlist
    #YTMusic.get_artist(channelId='UCrPe3hLA51968GwxHSZ1llw')
    #print('Name playlist for modification:')
    #playlistID = input()
    #if not YTMusic.get_user_playlist(playlistID) :
    #    print('Playlist not found!')


if __name__ == '__main__':
    yt()

