import random
import time
from datetime import datetime, timedelta
from threading import Thread

def posteMessage(forum, personnage, autre_personnage, fin):
    while datetime.now() < fin:
        bit = random.choice([0, 1])
        message = personnage.nom if bit == 0 else autre_personnage.nom
        message_time = datetime.now()
        personnage.messages.append((message, message_time))
        temps_attente = random.uniform(0.1, 0.5)  # Attente de 1 à 10 ms
        time.sleep(temps_attente)
        forum.posterMessageAnonyme((message, message_time))

def genererSecretMultithread(forum, personnage1, personnage2, duree_protocol):
    
    fin = datetime.now() + timedelta(seconds=duree_protocol)
    alice_thread = Thread(target=posteMessage, args=(forum, personnage1, personnage2, fin))
    bob_thread = Thread(target=posteMessage, args=(forum, personnage2, personnage1, fin))

    alice_thread.start()
    bob_thread.start()

    alice_thread.join()
    bob_thread.join()

# Cette fonction devra être appelée pour les deux utilisateurs et comparer leurs messages
def extraireSecret(forum, debut_protocol, fin_protocol):
    messages = forum.recupererMessagesAnonymes(debut_protocol, fin_protocol)
    return messages
