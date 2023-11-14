class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.messages = []
        self.code_secret = []

    def verifierSecret(self, secret):
        print("verifier secret")
        timestamps = [timestamp for message, timestamp in self.messages]
        print(timestamps)
        print(len(secret))
        print(len(self.messages))
        for message, timestamp in secret:
            if timestamp in timestamps:
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