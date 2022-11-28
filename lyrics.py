import json
import pandas as pd
import collections
import sys

try:
    import lyricsgenius
except:
    import subprocess
    subprocess.run(['pip3','install','lyricsgenius'])
    import lyricsgenius

client_access_token = "HpIYpWE8urYEimLXmjRsNBXLUERWVVS85HHCQEWrSKBedFN0b7OxCweWpLbk7CT-"
LyricsGenius = lyricsgenius.Genius(client_access_token,timeout=40)
LyricsGenius.excluded_terms = ["Live", "(Live)", "MTV Unplugged", "Demo"]

def getSongs(artist, album_name=None, max_songs=None):
    clean_name = artist.replace(' ', '')
    lyrics_dict = collections.defaultdict(str)
    if album_name is None:
        artist_obj = LyricsGenius.search_artist(artist, max_songs=max_songs)
        artist_obj.save_lyrics(filename=f'Lyrics_{clean_name}', overwrite=True)
        print('Data saved')
        with open(f'Lyrics_{clean_name}.json') as f:
            data = json.load(f)
        print('Data loaded')
        for song in data['songs']:
            lyrics_dict[song['title']] += song['lyrics']
    else:
        clean_album = album_name.replace(' ', '').replace("'","").replace('!','')
        album_obj = LyricsGenius.search_album(album_name, artist)
        album_obj.save_lyrics(filename=f'Lyrics_{clean_album}', overwrite=True)
        print('Data saved')
        with open(f'Lyrics_{clean_album}.json') as f:
            data = json.load(f)
        print('Data loaded')
        for song in data['tracks']:
            lyrics_dict[song['song']['full_title'].split('by')[0].strip()] += song['song']['lyrics']
 
    lyrics_df = pd.DataFrame.from_dict(dict(lyrics_dict), orient='index').reset_index().rename(columns={'index':'song_title',0:'lyrics'})
    return lyrics_df

lyrics_df = getSongs(sys.argv[1], sys.argv[2])
lyrics_df.to_csv(f'{sys.argv[1]}-{sys.argv[2]}_lyrics.csv',index=False)
