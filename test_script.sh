#!/bin/bash

# Tirer depuis GitHub (branche de test)
git pull origin testing

# Installer les dépendances Python
pip install -r requirement.txt

# Exécuter les tests (remplacez "commande_de_test" par la commande réelle pour exécuter vos tests)
flask run --port=5000
