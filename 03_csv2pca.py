import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def csv_2_pca(n_components=10):
    df = pd.read_csv('data.csv')
    df['artist'] = df["Unnamed: 0"]
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df = df.set_index('artist').fillna(0)

    pca = PCA(n_components=n_components)
    X_new = pca.fit_transform(df)

    df_pca = pd.DataFrame(data=X_new, index=df.index)
    return df_pca

if __name__ == "__main__":
    n_components = 40
    df_pca = csv_2_pca(n_components=n_components)
    df_pca.to_csv('df_pca_'+str(n_components)+".csv")

