from datetime import datetime, timedelta
import time
from forum import Forum  # Assurez-vous d'importer la classe Forum du module forum

# Exemple d'utilisation
if __name__ == "__main__":
    canal = Forum()  # Créez une instance de la classe Forum

    # Poster quelques messages
    canal.posterMessageAnonyme("Premier message")
    time.sleep(1)  # Attendre 1 seconde
    canal.posterMessageAnonyme("Deuxième message")
    time.sleep(1)
    canal.posterMessageAnonyme("Troisième message")

    # Récupérer les messages dans l'intervalle
    debut = (datetime.now() - timedelta(seconds=5)).strftime("%Y-%m-%d %H:%M:%S")
    fin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = canal.recupererMessagesAnonymes(debut, fin)

    print("Messages récupérés entre {} et {}:".format(debut, fin))
    for msg in messages:
        print(msg)
