# PCA – Réduction de dimension

## Objectif de la branche

Cette branche implémente la méthode PCA (Principal Component Analysis) dans le cadre du projet collaboratif de réduction de dimension.

Chaque étudiant développe sa méthode dans une branche dédiée avant fusion dans `main`.

Objectifs :

- Réduire les données en 2 dimensions  
- Visualiser la projection obtenue  
- Exporter les coordonnées réduites  
- Préparer les résultats pour la comparaison finale (trustworthiness)

---

## Implémentation

Pipeline appliqué :

1. Sélection des variables numériques  
2. Standardisation des données avec `StandardScaler`  
3. Application de `PCA(n_components=2)`  
4. Visualisation 2D  
5. Export des données transformées  

Librairies utilisées :

- pandas  
- numpy  
- matplotlib  
- scikit-learn  

---

## Notebook

Le notebook contient :

- Projection des données en 2D  
- Graphique de visualisation  
- Observation sur la structure obtenue  
- Export des résultats  

---

## Résultats exportés

Les données réduites sont enregistrées dans :



Ce fichier sera utilisé dans la branche `main` pour calculer la métrique trustworthiness et comparer la PCA avec les autres méthodes (t-SNE, UMAP).

---

## Observation

La PCA maximise la variance expliquée selon des axes orthogonaux.  
Elle capture la structure globale des données mais peut déformer certains voisinages locaux.

L’évaluation quantitative sera réalisée via la métrique trustworthiness lors de la phase de comparaison.

---

## Commandes Git utilisées

Création de la branche :

```bash
git checkout main
git pull origin main
git checkout -b method/PCA
git push -u origin method/PCA


Ajout des fichiers :

git add notebooks/pca.ipynb
git commit -m " notebook Analyse PCA"
git push
git add outputs/pca_2d.csv README.md
git commit -m "Export PCA 2D"
git push
```  
