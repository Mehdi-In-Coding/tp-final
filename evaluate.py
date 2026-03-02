import pandas as pd
import numpy as np
from sklearn.manifold import trustworthiness
from sklearn.preprocessing import StandardScaler
import os

def run_evaluation():
    # 1. Chargement des données sources
    df = pd.read_csv('city_lifestyle_dataset.csv')

    df_orig = pd.read_csv('city_lifestyle_dataset.csv')
    X = df_orig.select_dtypes(include=[np.number])
    X_scaled = StandardScaler().fit_transform(X)

    # 2. Fichiers à comparer (ceux générés par vos 3 méthodes)
    methods = {
        'PCA': 'pca_emb_2d.csv',
        't-SNE': 'tsne_emb_2d.csv',
        'UMAP': 'umap_emb_2d.csv'
    }

    print("=== Comparaison des méthodes (Trustworthiness) ===")
    results = {}

    for name, path in methods.items():
        if os.path.exists(path):
            df_emb = pd.read_csv(path)
            # Calcul du score
            score = trustworthiness(X_scaled, df_emb.values, n_neighbors=15)
            results[name] = score
            print(f"{name} : {score:.4f}")
        else:
            print(f"{name} : Fichier {path} manquant.")

    if results:
        best = max(results, key=results.get)
        print(f"\nRésultat final : La meilleure méthode est {best}")

if __name__ == "__main__":
    run_evaluation()