import pickle
import pandas as pd

with open ('a2g.pkl', 'rb') as f:
    a2g = pickle.load(f)


def get_all_columns(a2g):
    all_genres = set([])
    for artist, genres in a2g.iteritems():
        try:
            genres = zip(*genres)[0]
        except:
            pass
        else:
            all_genres |= set(genres)
    columns = sorted(list(all_genres))
    return columns


def reorganize_a2g(a2g):
    data = {}
    for artist, genres in a2g.iteritems():
        g = dict(genres)
        data[artist] = g
    return data

a2g_dict = reorganize_a2g(a2g)

df = pd.DataFrame.from_dict(a2g_dict, 'index').fillna(0)

df.to_csv('data.csv')