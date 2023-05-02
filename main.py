from ytmusicapi import YTMusic
import os
import io

def yt():
    channelID = 'UCrPe3hLA51968GwxHSZ1llw'
    #Verification and creation of headers_auth.json
    if not os.path.exists('headers_auth.json'):
        YTMusic.setup(filepath="headers_auth.json")
    
    ytmusic = YTMusic('browser.json')
    playlist_name = 'Teste'
    playlist_id = ytmusic.create_playlist(playlist_name, '',privacy_status="PRIVATE")
    with open('songs.txt','r',encoding='utf-8') as file:
        for line in file:
            search_results = ytmusic.search(line ,filter='songs')
            if search_results:
                song = search_results[0]
                video_id = song['videoId']
                ytmusic.add_playlist_items(playlist_id, [search_results[0]['videoId']])
    
    #Creation of a Playlist
    #YTMusic.get_artist(channelId='UCrPe3hLA51968GwxHSZ1llw')
    #print('Name playlist for modification:')
    #playlistID = input()
    #if not YTMusic.get_user_playlist(playlistID) :
    #    print('Playlist not found!')


if __name__ == '__main__':
    yt()

