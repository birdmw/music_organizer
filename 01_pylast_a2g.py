
import os
import random
import time
import pickle
import json
import pylast


with open ("credentials.json", 'rb') as f:
    credentials = json.load(f)

API_KEY = credentials["API_KEY"]  # this is a sample key
API_SECRET = credentials["API_SECRET"]

# In order to perform a write operation you need to authenticate yourself
username = credentials["usrename"]
password_hash = pylast.md5(credentials["password"])

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)


def lastfm_artist_to_tags(artist):
    tag_weight = {}

    result = network.get_artist(artist).get_top_tags()

    for tag in result:
        tag_weight[str(tag.item.get_name())] = str(tag.weight)

    tag_weight = {k: int(v) for k, v in tag_weight.items()}

    return sorted(tag_weight.items(), key=lambda x: x[1], reverse=True)


# print lastfm_artist_to_tags('system of a down')

def dirOfArtists_to_genres(DIR_PATH):
    dirs = [d for d in os.listdir(DIR_PATH) if os.path.isdir(os.path.join(DIR_PATH, d))]
    return dirs

if __name__ == '__main__':
    path = 'C:\Users\\birdm\Desktop\Organized Artist'
    artists = dirOfArtists_to_genres(path)

    artist_2_genre = {}
    a_count = len(artists)
    walk = 0
    for a in artists:

        try:
            genres = lastfm_artist_to_tags(a)
        except Exception as e:
            print str(e)
        else:
            artist_2_genre[a] = genres
        time.sleep(random.random() / 100.)
        walk += 1
        print round(float(walk) / float(a_count), 2), a

    with open ('a2g.pkl', 'wb') as f:
        pickle.dump(artist_2_genre, f)
