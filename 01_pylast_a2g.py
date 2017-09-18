#
# Application name	pylast_test
# API key	f61a8039c0b69eed56928144faf775ac
# Shared secret	447992fb795c313aa217117bb04d4a7d
# Registered to	birdmw

import os
import random
import time
import pickle

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account/create for Last.fm
API_KEY = "f61a8039c0b69eed56928144faf775ac"  # this is a sample key
API_SECRET = "447992fb795c313aa217117bb04d4a7d"

# In order to perform a write operation you need to authenticate yourself
username = "birdmw"
password_hash = pylast.md5("Bubba123$")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# Now you can use that object everywhere
artist = network.get_artist("System of a Dpwn").get_top_tags()


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
