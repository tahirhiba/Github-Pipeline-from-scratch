#!/bin/bash

# Tirer depuis GitHub (branche principale)
git pull origin main

# Installer les dépendances Python
pip install -r requirement.txt

# Lancer votre application (remplacez "commande_de_lancement" par la commande réelle pour lancer votre application)
flask run --port=5001

