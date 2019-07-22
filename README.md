# Outil de chiffrement/déchiffrement de vault

Composant de chiffrement/déchiffrement de vault mis à disposition des projets n'ayant pas ansibe installé sur leur poste.

## Fonctionnement

Saisir la clé dans le champ obligatoire de saisie de mot de passe.
Saisir le contenu à chiffre/dechiffrer dans la zone de saisie de gauche.
Utiliser le bouton pour faire la conversion.
Le résultat sera affiché dans la zone de saisie en lecture seule sur la droite.
Les messages d'erreurs sont affichés sous la zone de saisie de la clé de chiffrement.
Un bouton permet de copier dans le presse papier le résultat de la conversion.

## Installation

### Pré-requis

- Installer python3, pip3
- Installer virtualenv et créer un environnement, puis l'activer

```bash
# Installer virtualenv
$ pip install virtualenv
# Création de l'environnement env
$ virtualenv env
# Activation de l'environnement env
$ source env/bin/activate 
```

### Installation

- Telecharger et installer les dépendances nécessaires au projet
```bash
pip install -r requirements.txt
```

- Lancement du projet en local. Voir le fichier de config .env

```bash
# Voir les options disponibles
$ make help

# Lancement du projet en local
$ make run
# Lancement manuel
$ PORT=8080 python3 main.py
```

## Configuration run en local (mod dev)

| Parametre     | Type/Value      | Description                         |
| :-            | :-:             | :-                                  |
| DEBUG         | Entier (0 ou 1) | Activation du mode debug de bottle  | 
| RELOAD        | Entier (0 ou 1) | Activation du hot reload (mod dev)  |
| PORT          | Port applicatif | Port applicatif                     |

## Configuration en run prod

- Pas de paramètre, le conteneur expose sur le port 8080 l'application
- L'entrypoint /health permet de checker l'état de l'application
- Lancé par gunicorn avec 3 workers
