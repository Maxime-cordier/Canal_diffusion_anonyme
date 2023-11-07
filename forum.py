from datetime import datetime

class Forum:
    def __init__(self):
        self.messages = []

    def posterMessageAnonyme(self, message):
        self.messages.append(message)
        #self.messages.sort(key=lambda x: x[0])  # Assurez-vous que la liste est triée chronologiquement

    def recupererMessagesAnonymes(self, debut, fin):
        debut = datetime.strptime(debut, "%Y-%m-%d %H:%M:%S")
        fin = datetime.strptime(fin, "%Y-%m-%d %H:%M:%S")
        messages_dans_intervalle = [
            (msg, timestamp) for msg, timestamp in self.messages if debut <= timestamp <= fin
        ]
        return messages_dans_intervalle
