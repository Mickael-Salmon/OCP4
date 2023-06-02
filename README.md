<div align="center">
  <a href="" target="_blank" rel="noreferrer">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png">
  </a>
</div>

<h2 align="center"> Vous trouverez ici le Projet 4 du parcours<a href="https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python" target="_blank" rel="noreferrer"> Développeur d'application - Python</a> 👋
 </h2>

<h2 align="center" # Développez un programme logiciel en Python 💻 !>

 <p align="center" <a href="" target="_blank" rel="noreferrer"><img src="https://github.com/MicSa/OCP4/blob/main/chesspict.png"></a>>
</p>

</h2>

<h2> Scénario </h2>

Vous êtes un développeur junior depuis deux mois et vous travaillez en freelance pour écrire des scripts simples afin d’aider les petites entreprises locales à gérer leur inventaire. 

Elie, votre amie et elle aussi développeuse Python, est membre du club d'échecs local. Elle vous a expliqué que les tournois du club sont actuellement organisés à la main, mais que les membres du club aimeraient pouvoir les gérer avec un logiciel. Le club avait trouvé une application convenable, mais elle avait besoin d’une connexion Internet – qui n'est pas disponible pour tous les tournois – et l'abonnement mensuel était trop cher.

<p align="center" <a href="" class="oc-imageLink oc-imageLink--disabled"><img src="https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png" alt="Logo du club d'échecs"></a>>
</p>


</br>

- 💬 Vous suggérez que vous pourriez écrire un outil qui permette de gérer les tournois pour aider le club, mais qui fonctionne hors ligne. Elie aime bien votre idée et elle dit qu'elle en discutera la prochaine fois qu'elle se rendra au club. Comme elle s’occupe déjà de plusieurs contrats en freelance, elle accepte de vous recommander comme candidat idéal pour développer cette application.

 <h3>Livrables attendus 🔭 </h3> 
   

-   Le code de l'application, tel que prescrit dans la spécification technique 
-   Un répertoire contenant un fichier HTML, généré par **flake8-html**, ne montrant aucune erreur de peluchage dans le code 
-   Un fichier **README.md** contenant des instructions claires sur la manière d'exécuter le programme, de l'utiliser et de générer un nouveau fichier flake8-html

</br>


 <h3>Structure de dossiers du projet</h3>  

```
├── controllers
│   ├── __init__.py
│   ├── menu_controller.py
│   ├── reports_controller.py
│   └── tournament_controller.py
│   └── user_Input_validation.py
├── models
│   ├── __init__.py
│   ├── player_model.py
│   ├── round_model.py
│   └── tournament_model.py
└── views
│   ├── __init__.py
│   ├── menu_view.py
│   ├── reports_view.py
│   └── round_view.py
└── database
│   ├── players.json
│   ├── tournaments.json

```

Les fichiers `__init__.py` sont nécessaires pour que Python reconnaisse le dossier comme un module.

Le dossier `controllers`, contient la logique de contrôle, tels que la gestion des tournois, la génération de rapports et le menu principal.

Le dossier `models` contient les modèles pour les entités dans votre programme, tels que les tournois, les rondes et les joueurs.

Le dossier `views` contient tous les fichiers qui concernent l'interface utilisateur, tels que les vues pour les rondes, les rapports et le menu principal.
Le dossier `database` contient tous les fichiers relatifs aux stockage d'information pour les joueurs et les tournois par TinyDB au format JSON.

<h2> Installation et démarrage du projet</h2> 
<h3>Windows  </h3> 

Depuis un terminal , se déplacer dans le dossier applicatif souhaité :

<h3>Récupération du projet</h3> 

```
git clone https://github.com/Mickael-Salmon/OCP4/
```

<h3>Activer l'environnement virtuel </h3> 

```
cd OCP4
```
``` 
python -m venv .envOCP4
```
``` 
~env\scripts\activate
```


<h3>Installer les paquets requis </h3>

```
pip install -r requirements.txt
```

<h3>Lancer le programme</h3>

```
python main.py
```

<h2>MacOS et Linux : </h2>

Depuis un terminal, se déplacer dans dossier souhaité. 

<h3>Récupération du projet</h3>

```
git clone https://github.com/Mickael-Salmon/OCP4/
```

<h3>Activer l'environnement virtuel </h3>

```
cd OCP4
```

```
python3 -m venv .envOCP4
```

```
source .envOCP4/bin/activate
```

<h3>Installer les paquets requis </h3>

```
pip install -r requirements.txt
```

<h3>Lancer le programme </h3>

```
python main.py
```

<h3>Générer un nouveau rapport flake8 </h3>

```
flake8 --format=html --htmldir=flake8_report
```

OU pour exclure un environnement virtuel, ajouter --exclude=nom de l'environnement</br>

Exemple : </br>

```
flake8 --format=html --htmldir=flake8_report --exclude=.env
```