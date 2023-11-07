import random
import time
from datetime import datetime, timedelta
from threading import Thread

def posteMessage(forum, nom, autre_nom, fin):
    while datetime.now() < fin:
        bit = random.choice([0, 1])
        message = nom if bit == 0 else autre_nom
        temps_attente = random.uniform(0.1, 0.5)  # Attente de 1 à 10 ms
        time.sleep(temps_attente)
        print(message + " from " + nom + " at " + str(datetime.now()))
        if (nom == "Alice") and (message == "Alice"):
            forum.posterMessageAnonyme(0)
        elif (nom == "Alice") and (message == "Bob"):
            forum.posterMessageAnonyme(1)
        elif (nom == "Bob") and (message == "Bob"):
            forum.posterMessageAnonyme(0)
        elif (nom == "Bob") and (message == "Alice"):
            forum.posterMessageAnonyme(1)

def genererSecretMultithread(forum, duree_protocol):
    fin = datetime.now() + timedelta(seconds=duree_protocol)
    alice_thread = Thread(target=posteMessage, args=(forum, "Alice", "Bob", fin))
    bob_thread = Thread(target=posteMessage, args=(forum, "Bob", "Alice", fin))

    alice_thread.start()
    bob_thread.start()

    alice_thread.join()
    bob_thread.join()

# Cette fonction devra être appelée pour les deux utilisateurs et comparer leurs messages
def extraireSecret(forum, debut_protocol, fin_protocol):
    messages = forum.recupererMessagesAnonymes(debut_protocol, fin_protocol)
    return messages
    for message in messages:
        if "Alice" in message:
            print("null")
            # Ceci est un exemple, la logique exacte pour générer le bit secret doit être définie
            # secret += '0' if nom == "Alice" else '1'

    return secret
