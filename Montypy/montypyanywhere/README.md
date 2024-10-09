# README.md
# Monty Python Chatbot - Instructions de déploiement

1. Créez un compte gratuit sur PythonAnywhere (www.pythonanywhere.com)

2. Une fois connecté :
   - Cliquez sur "Dashboard"
   - Allez dans la section "Web"
   - Cliquez sur "Add a new web app"
   - Choisissez "Flask" et "Python 3.8"

3. Configuration :
   - Dans "Source code", mettez le chemin : /home/votre_username/mysite/
   - Dans "WSGI configuration file", le chemin sera automatiquement configuré

4. Uploadez vos fichiers :
   - Utilisez l'onglet "Files" pour créer les dossiers nécessaires
   - Uploadez tous vos fichiers (app.py, templates/index.html, modèle, etc.)
   - Créez les fichiers requirements.txt et wsgi.py avec le contenu fourni

5. Installez les dépendances :
   - Ouvrez un terminal "Bash console"
   - Activez l'environnement virtuel : workon votre_env_name
   - Installez les dépendances : pip install -r requirements.txt

6. Redémarrez l'application web

NOTES IMPORTANTES :
- L'offre gratuite de PythonAnywhere a des limitations :
  * 512 MB de RAM
  * CPU partagé
  * 500 MB d'espace disque
- Vérifiez la taille de votre modèle. Si c'est plus que 500 MB, vous devrez :
  1. Soit utiliser un modèle plus petit
  2. Soit opter pour un hébergeur payant