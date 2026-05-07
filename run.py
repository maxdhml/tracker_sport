from app import create_app, db
from app.models import User, Programme, GroupeMusculaire
from werkzeug.security import generate_password_hash
import os

app = create_app()

with app.app_context():
    db.create_all()
    
    # 1. Création de l'admin s'il n'existe pas
    if not User.query.filter_by(username=os.environ.get('ADMIN_USER')).first():
        admin = User(
            username=os.environ.get('ADMIN_USER'),
            password_hash=generate_password_hash(os.environ.get('ADMIN_PASS'))
        )
        db.session.add(admin)
        
    # 2. Création d'un programme par défaut pour que tu puisses tester le formulaire
    if not Programme.query.first():
        p1 = Programme(nom="Sèche Été 2024", code="SEC-24")
        db.session.add(p1)
        db.session.flush() # Permet de récupérer p1.id tout de suite
        
        g1 = GroupeMusculaire(nom="Pectoraux / Triceps", code="PEC-TRI", programme_id=p1.id)
        g2 = GroupeMusculaire(nom="Dos / Biceps", code="DOS-BIC", programme_id=p1.id)
        db.session.add_all([g1, g2])
        
    db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)