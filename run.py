
from app import create_app, db #serveur
from app.models import User, Programme, GroupeMusculaire #tables BDD
from werkzeug.security import generate_password_hash #hashage mdp
import os #variables .env

#configuration de l'app flask
app = create_app()

with app.app_context(): #dans la bdd
    db.create_all() #crétion des tables (via models.py)
    
    # 1. Création du compte Admin
    if not User.query.filter_by(username=os.environ.get('ADMIN_USER')).first():
        admin = User( 
            username=os.environ.get('ADMIN_USER'), #id dans .env
            password_hash=generate_password_hash(os.environ.get('ADMIN_PASS')) #hachage
        )
        db.session.add(admin) #ajout
        
    # 2. Création d'un programme par défaut 
    if not Programme.query.first(): #si vide
        p1 = Programme(nom="Sèche Été 2026", code="SEC-26") #créer programme
        db.session.add(p1) #ajout
        db.session.flush() # id pour rattacher avec les groupes musculaires
        
        g1 = GroupeMusculaire(nom="Pectoraux / Triceps", code="PEC-TRI", programme_id=p1.id)
        g2 = GroupeMusculaire(nom="Dos / Biceps", code="DOS-BIC", programme_id=p1.id)
        db.session.add_all([g1, g2])
        
    db.session.commit() #commit final

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) #lancement