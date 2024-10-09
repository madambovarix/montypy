# 🐍 Monty Python Chatbot

un chatbot basé sur un distilgpt2 fine-tuned sur les scripts des Monty Python's Flying Circus, 
scrapés avec scrapy sur https://www.ibras.dk/montypython/justthewords.htm 



 Prompt système personnalisable pour ajuster (?) le comportement du chatbot



![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask Version](https://img.shields.io/badge/Flask-2.0.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Spam](https://img.shields.io/badge/Spam-A%20Lot-red)


## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- 500 MB d'espace disque libre pour le modèle
- Un ministère des marches stupides

## 🛠️ Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-username/monty-python-chatbot.git
cd monty-python-chatbot
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```
3-et-demi. Entrainez le modèle : 
```bash
python ./montypy/montypy/train_model.py
```
4. Lancez l'application :
```bash
python ./montypyweb/app2.py
```

5. Ouvrez votre navigateur et accédez à `http://localhost:5000`

## 🎮 Utilisation

1. Entrez votre message dans la zone de texte
2. Appuyez sur "Envoyer" ou sur Entrée
3. Attendez la réponse du chatbot
4. Riez (optionnel mais recommandé)

### Personnalisation du prompt système

1. Cliquez sur "⚙️ Paramètres du prompt système"
2. Modifiez le texte dans la zone de prompt
3. Cliquez sur "Mettre à jour le prompt"


## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

Assurez-vous que vos contributions sont aussi absurdes que possible.

## 📜 Licence

Ce projet est sous licence gratuite. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## ⚠️ Avertissement

Ce chatbot est destiné au divertissement. Il peut parfois produire des réponses absurdes, inexactes ou totalement loufoques. Ne l'utilisez pas pour des conseils médicaux, juridiques ou concernant les perroquets.

## 🙏 Remerciements

- Les Monty Python pour leur humour inégalé
- La communauté Hugging Face pour les outils transformers
- Le ministère des marches stupides

## 📬 Contact

Pour toute question, suggestion ou si vous voulez simplement discuter des écureuils albinos, vous pouvez :
- Ouvrir une issue sur GitHub
- Me contacter sur X @BorgGreg

---

Fait avec ❤️ et beaucoup de spam
