DOCKERFILE = "Dockerfile" #fichier à modifier
PROXY = "http://cache-etu.univ-artois.fr:3128" #addresse proxy IUT

# Les 2 versions de la commande
LIGNE_AVEC_PROXY = f'RUN pip install --proxy={PROXY} -r requirements.txt'
LIGNE_SANS_PROXY = 'RUN pip install -r requirements.txt'

with open(DOCKERFILE, "r") as f: #lire le fichier 
    contenu = f.read() #copier contenu dans variable

if LIGNE_AVEC_PROXY in contenu: #si avec proxy 
    contenu = contenu.replace(LIGNE_AVEC_PROXY, LIGNE_SANS_PROXY) #remplacer avec sans proxy
    print("Proxy DÉSACTIVÉ (mode maison)")
else:
    contenu = contenu.replace(LIGNE_SANS_PROXY, LIGNE_AVEC_PROXY) #remplacer avec proxy
    print("Proxy ACTIVÉ (mode IUT)")

with open(DOCKERFILE, "w") as f: #ecrire dans le fichier
    f.write(contenu)

print(f"   Fichier '{DOCKERFILE}' mis à jour.")
print("   Relance : docker-compose up --build")
