import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from collections import defaultdict
import json

def pca_2_clusters(n_components=20, n_clusters=15):
    df = pd.read_csv('df_pca_'+str(n_components)+'.csv', index_col='artist')

    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(df)

    labels = kmeans.labels_

    cluster_ids = set(labels)

    clusters = zip(df.index.tolist(), labels)

    clusters_inv = defaultdict(list)

    for item in clusters:
        clusters_inv[item[1]].append(item[0])
    clusters_inv = dict(clusters_inv)

    with open('cluster'+str(n_clusters)+'.json', 'wb') as f:
        json.dump(clusters_inv, f)

if __name__ == '__main__':
    pca_2_clusters(n_components=40, n_clusters=20)