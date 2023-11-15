# Canal de Communication Anonyme et Génération de Secret

## Vue d'ensemble
Ce projet implémente un mécanisme de génération de secret partagé entre deux utilisateurs, Alice et Bob, via un canal de communication anonyme. Il simule un forum anonyme où les messages sont échangés pour établir un secret commun. Le processus est conçu de manière à ce que même si un attaquant passif observe la conversation, seul Alice et Bob peuvent déduire le secret partagé.

## Structure

- **forum.py** : Implémente la classe **Forum**, simulant un canal de communication anonyme. Elle permet de poster et de récupérer des messages anonymes dans un intervalle de temps spécifié.
- **personnage.py** : Définit la classe **Personnage** pour les utilisateurs (Alice et Bob), chacun ayant un nom unique et la capacité de vérifier le secret partagé.
- **générationSecret.py** : Contient des fonctions pour le processus de génération de secret en utilisant le multithreading, y compris la publication de messages et l'extraction du secret partagé.
- **main.py** : Le script principal qui utilise les composants ci-dessus pour simuler le protocole de génération de secret entre Alice et Bob.

## Fonctionnement

1. **Génération du Secret :**

- Alice et Bob postent des messages anonymement sur le forum.
- Les messages contiennent les noms "Alice" ou "Bob", choisis en fonction d'un bit généré aléatoirement.
- La publication se fait sur une durée prédéterminée.

2. **Extraction du Secret :**

- Après la durée du protocole, Alice et Bob extraient la séquence de messages du forum.
- Les messages extraits sont utilisés pour construire le secret partagé.

3. **Vérification du Secret :**

- Les deux participants vérifient s'ils ont dérivé le même secret.
- Seuls Alice et Bob peuvent déterminer le secret partagé, car chacun sait quels messages il a envoyés et peut ainsi déduire les messages de l'autre.

## Usage
1. Exécutez le script **main.py**.
2. Le script simule l'ensemble du processus : génération, extraction et vérification du secret.
3. Le secret partagé et les résultats de la vérification seront affichés dans la console.

## Acteurs
- Alice et Bob : Les deux participants qui génèrent et vérifient le secret partagé.
- Un attaquant passif : Peut observer la conversation mais ne peut pas déduire le secret partagé.

## Prérequis
- Python 3.x
- Support du multithreading

## Auteurs 
- **Maxime CORDIER**
- **Sylvain MESTRE**