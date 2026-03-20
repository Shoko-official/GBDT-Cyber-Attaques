# 🚀 Roadmap du PFE : Détection d'Intrusion Réseau

Ce document divise le projet en **4 sous-projets autonomes**. Chaque étape doit être validée avant de passer à la suivante pour garantir la qualité du système final.

---

## 🏗️ Sous-Projet 1 : Data Mastery & EDA
**Objectif** : Transformer les données brutes en un ensemble exploitable et comprendre les signaux d'attaque.

- [ ] **Acquisition** : Téléchargement et chargement du dataset NSL-KDD.
- [ ] **Nettoyage** : Traitement des valeurs manquantes et types de données.
- [ ] **Ingénierie** : Encodage (One-Hot/Label) des protocoles et services.
- [ ] **Exploration (EDA)** : Visualisation de la distribution des classes (Normal vs Attaques) et identification des caractéristiques les plus corrélées aux attaques.

✅ **Critère de Validation** : Un notebook ou script propre qui produit un dataset "prêt pour le ML" avec un rapport visuel des corrélations.

---

## 🤖 Sous-Projet 2 : Architecture de Modélisation
**Objectif** : Trouver l'algorithme le plus robuste pour la détection.

- [ ] **Baselines** : Entraînement de modèles simples (Régression Logistique, Arbre de Décision) pour fixer un score de référence.
- [ ] **Advanced Models** : Implémentation de GBDT (Random Forest, XGBoost ou LightGBM).
- [ ] **Optimisation** : Recherche d'hyperparamètres (GridSearch/RandomSearch).
- [ ] **Gestion du Déséquilibre** : Si nécessaire, utiliser SMOTE ou ajuster les poids des classes.

✅ **Critère de Validation** : Atteindre un **Recall > 95%** (priorité à la détection des attaques) sur l'ensemble de test.

---

## 📊 Sous-Projet 3 : Évaluation & Interprétabilité
**Objectif** : Justifier pourquoi le modèle prend ses décisions (crucial en sécurité).

- [ ] **Métriques Avancées** : Matrice de confusion détaillée, Precision-Recall Curve, AUROC.
- [ ] **Importance des Features** : Identifier quels types de trafic (ex: ICMP, ports spécifiques) déclenchent les alertes.
- [ ] **Analyse d'Erreur** : Étudier les "Faux Négatifs" (attaques manquées) pour comprendre les limites.

✅ **Critère de Validation** : Un document de synthèse montrant que le modèle est fiable et explicable.

---

## 🌐 Sous-Projet 4 : Interface & Simulation "Temps Réel"
**Objectif** : Rendre le projet concret pour un utilisateur final.

- [ ] **API/Backend** : Créer une fonction de prédiction robuste qui prend des données brutes en entrée.
- [ ] **Frontend Streamlit** : Interface avec formulaires de saisie ou upload de fichier CSV.
- [ ] **Dashboard** : Visualisation dynamique des alertes (ex: Rouge pour Danger, Vert pour Normal).
- [ ] **Bonus** : Simulation d'un flux continu de données.

✅ **Critère de Validation** : Une application fonctionnelle où n'importe qui peut tester une ligne de log réseau et obtenir une réponse instantanée.
