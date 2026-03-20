# 🛡️ GBDT - Détection d'Intrusion Réseau

Système d'IA basé sur les Gradient Boosting Decision Trees (GBDT) pour identifier les menaces réseau en utilisant le dataset NSL-KDD.

## 📊 Dataset : NSL-KDD
Le dataset NSL-KDD est une version améliorée du KDD'99 original. Il contient 41 caractéristiques par connexion, incluant :
- **Features intrinsèques** (duration, protocol_type, etc.)
- **Features de contenu** (num_failed_logins, etc.)
- **Features de trafic temporel** (count, srv_count, etc.)

### Classification
- **Binaire** : Normal vs Attaque
- **Multi-classe** : DoS, Probe, R2L, U2R

## 🚀 Structure du projet
- `data/`: Datasets bruts et transformés.
- `notebooks/`: Analyses exploratoires et expérimentations.
- `src/`: Scripts de preprocessing, entraînement et utilitaires.
- `Roadmap.md`: Suivi des étapes du PFE.

## 🛠️ Installation
```bash
pip install -r requirements.txt
```
