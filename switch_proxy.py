"""
Script pour switcher le Dockerfile entre mode IUT (avec proxy) et mode maison (sans proxy).
Usage : python switch_proxy.py
"""

DOCKERFILE = "Dockerfile"
PROXY = "http://cache-etu.univ-artois.fr:3128"

LIGNE_AVEC_PROXY = f'RUN pip install --proxy={PROXY} -r requirements.txt'
LIGNE_SANS_PROXY = 'RUN pip install -r requirements.txt'

with open(DOCKERFILE, "r") as f:
    contenu = f.read()

if LIGNE_AVEC_PROXY in contenu:
    contenu = contenu.replace(LIGNE_AVEC_PROXY, LIGNE_SANS_PROXY)
    print("✅ Proxy DÉSACTIVÉ (mode maison)")
else:
    contenu = contenu.replace(LIGNE_SANS_PROXY, LIGNE_AVEC_PROXY)
    print("✅ Proxy ACTIVÉ (mode IUT)")

with open(DOCKERFILE, "w") as f:
    f.write(contenu)

print(f"   Fichier '{DOCKERFILE}' mis à jour.")
print("   Relance : docker-compose up --build")
