from forum import Forum
from personnage import Personnage
from générationSecret import genererSecretMultithread, extraireSecret
from datetime import datetime, timedelta

def main():

    canal = Forum()
    alice = Personnage("Alice")
    bob = Personnage("Bob")
    duree_protocol = 5  # Durée de 60 secondes

    # Génération du secret
    genererSecretMultithread(canal, alice, bob, duree_protocol)

    # Supposons que la génération commence maintenant
    debut_protocol = datetime.now() - timedelta(seconds=duree_protocol)
    fin_protocol = datetime.now()

    # Extraction du secret
    secret = extraireSecret(canal, debut_protocol.strftime("%Y-%m-%d %H:%M:%S"), fin_protocol.strftime("%Y-%m-%d %H:%M:%S"))
    print("Le secret partagé est :", secret)

    # Vérification du secret
    SecretAlice = alice.verifierSecret(secret)
    SecretBob = bob.verifierSecret(secret)

    print(SecretAlice)
    print(SecretBob)

    if SecretAlice == SecretBob:
        print("Alice et Bob ont le même secret")
    else:
        print("Alice et Bob n'ont pas le même secret")


if __name__ == "__main__":
    main()
