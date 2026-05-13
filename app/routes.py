from flask import render_template, request, redirect, url_for, session, flash, current_app as app
from werkzeug.security import check_password_hash
from . import db
from .models import User, Programme, GroupeMusculaire, Exercice
from .config import PROFILE, NIVEAUX


# --- Authentification ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            session['user_id'] = user.id
            flash("Connexion réussie.", "success")
            return redirect(url_for('recap'))
        flash("Identifiants incorrects.", "error")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Déconnexion réussie.", "success")
    return redirect(url_for('profile'))


# --- Pages ---

@app.route('/')
def profile():
    return render_template('profile.html', profile=PROFILE)


@app.route('/recap')
def recap():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    programmes = Programme.query.all()
    return render_template('recap.html', programmes=programmes, niveaux=NIVEAUX)


@app.route('/ajouter', methods=['GET', 'POST'])
def form():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nom = request.form.get('nom', '').strip()
        code = request.form.get('code', '').strip()
        groupe_id = request.form.get('groupe_id')
        niveau = request.form.get('niveau_maitrise')

        # Validation côté serveur
        if not nom or not code or not groupe_id or not niveau:
            flash("Tous les champs sont obligatoires.", "error")
            return redirect(url_for('form'))

        if int(niveau) not in NIVEAUX:
            flash("Niveau de maîtrise invalide.", "error")
            return redirect(url_for('form'))

        nouvel_exo = Exercice(
            nom=nom,
            code=code,
            groupe_id=int(groupe_id),
            niveau_maitrise=int(niveau)
        )
        db.session.add(nouvel_exo)
        db.session.commit()
        flash("Exercice ajouté avec succès.", "success")
        return redirect(url_for('recap'))

    groupes = GroupeMusculaire.query.all()
    return render_template('form.html', groupes=groupes, niveaux=NIVEAUX)


# --- Suppression ---

@app.route('/supprimer/<int:exercice_id>', methods=['POST'])
def supprimer(exercice_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    exercice = Exercice.query.get_or_404(exercice_id)
    db.session.delete(exercice)
    db.session.commit()
    flash("Exercice supprimé.", "success")
    return redirect(url_for('recap'))