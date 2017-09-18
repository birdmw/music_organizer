import json
from collections import defaultdict
import pandas as pd

def tag_clusters(n_tags):
    cluster_tags = {}
    for c in clusters.keys():
        s_mean = df.ix[clusters[c]].mean()
        cluster_tags[str(c)] = s_mean.nlargest(n=n_tags).index.tolist()
    return cluster_tags

def are_these_unique(list_of_items):
    sets = [str(sorted(_)) for _ in list_of_items]
    if len(sets) > len(set(sets)):
        return False
    else:
        return True

def unique_tags():
    for i in range(10)[1:]:
        cluster_tags = tag_clusters(n_tags=i)
        if are_these_unique(cluster_tags.values()):
            return {k: " ".join(v) for k,v in cluster_tags.iteritems()}
    return None

def rename_clusters():
    pass

if __name__ == "__main__":

    n_clusters = 20
    df = pd.DataFrame.from_csv('data.csv')

    cluster_json = 'cluster' + str(n_clusters) + '.json'

    with open(cluster_json, 'rb') as f:
        clusters = json.load(f)

    tags = unique_tags()
    tagged_clusters = {}
    for cluster_id in clusters.keys():
        tagged_clusters[tags[cluster_id]] = clusters[cluster_id]
    tagged_clusters
    with open('tagged_clusters'+str(n_clusters)+'.json', 'wb') as f:
        json.dump(tagged_clusters, f, sort_keys=True, indent=4, separators=(',', ': '))
