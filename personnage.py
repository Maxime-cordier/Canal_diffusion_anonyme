class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.messages = []
        self.code_secret = []

    def verifierSecret(self, secret):
        print("verifier secret")
        for message, timestamp in secret:
            print(self.messages)
            if timestamp in self.messages:
                if message == self.nom:
                    
                    self.code_secret.append(0)
                else:
                    self.code_secret.append(1)
            else:
                if message == self.nom:
                    self.code_secret.append(1)
                else:
                    self.code_secret.append(0)

        return self.code_secret