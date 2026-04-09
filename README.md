# Santorin — Pipeline de Traduction Automatique FR → EN

Projet généré avec [Cookiecutter](https://github.com/cookiecutter/cookiecutter) dans le cadre du Master Big Data, Analyse & Business Intelligence — Sorbonne Paris Nord.

![CI](https://github.com/spidersweep/santorin/actions/workflows/CI.yml/badge.svg)

---

## 🎯 Objectif

Ce projet met en place un pipeline complet de traduction automatique français → anglais et d'évaluation de la qualité des traductions via le score BLEU.

Le modèle utilisé est [`Helsinki-NLP/opus-mt-fr-en`](https://huggingface.co/Helsinki-NLP/opus-mt-fr-en) disponible sur HuggingFace.

---

## 🗂️ Structure du projet

```
santorin/
├── src/
│   ├── loaders/        # Chargement des données (CSV, JSON)
│   ├── processors/     # Prétraitement des données
│   ├── translators/    # Interface avec le modèle de traduction
│   ├── evaluators/     # Calcul des métriques (BLEU, chrF)
│   ├── orchestrator/   # Coordination du pipeline
│   ├── config.py       # Configuration centralisée
│   └── main.py         # Point d'entrée principal
├── data/               # Données d'entrée
├── output/             # Résultats produits par le pipeline
├── tests/              # Tests unitaires
├── pyproject.toml
└── requirements.txt
```

---

## ⚙️ Installation

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux

pip install -U pip
pip install -r requirements.txt
```

---

## 🚀 Lancer le pipeline

```bash
python src/main.py
```

Résultat attendu :

```
Loaded 20 rows.
Traduction: 100%|████████████| 15/15
Saved translated file to: output/translated.csv
BLEU: 41.61
chrF: 70.46
```

---

## 🧪 Tests

```bash
pytest
```

---

## 👩‍💻 Auteur

**Lara Grilo** — [GitHub](https://github.com/spidersweep) · [LinkedIn](https://linkedin.com/in/Lagrilo)

---

## 🐍 Version Python

Compatible avec Python 3.10+