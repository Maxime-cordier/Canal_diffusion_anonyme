from forum import Forum
from générationSecret import genererSecretMultithread, extraireSecret
from datetime import datetime, timedelta

def main():
    canal = Forum()

    nom1 = "Alice"
    nom2 = "Bob"

    duree_protocol = 5  # Durée de 60 secondes

    # Génération du secret
    genererSecretMultithread(canal, duree_protocol)

    # Supposons que la génération commence maintenant
    debut_protocol = datetime.now() - timedelta(seconds=duree_protocol)
    fin_protocol = datetime.now()

    # Extraction du secret
    secret = extraireSecret(canal, debut_protocol.strftime("%Y-%m-%d %H:%M:%S"), fin_protocol.strftime("%Y-%m-%d %H:%M:%S"), [nom1, nom2])
    print("Le secret partagé est :", secret)

if __name__ == "__main__":
    main()
