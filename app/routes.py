from flask import render_template, request, redirect, url_for, session, current_app as app
from werkzeug.security import check_password_hash
from . import db
from .models import User, Programme, GroupeMusculaire, Exercice
from .config import PROFILE

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            session['user_id'] = user.id
            return redirect(url_for('recap'))
        return "Identifiants incorrects", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('profile'))

@app.route('/')
def profile():
    return render_template('profile.html', profile=PROFILE)

@app.route('/recap')
def recap():
    if 'user_id' not in session: return redirect(url_for('login'))
    programmes = Programme.query.all()
    return render_template('recap.html', programmes=programmes)

@app.route('/ajouter', methods=['GET', 'POST'])
def form():
    if 'user_id' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Sauvegarde en Base de Données
        nouvel_exo = Exercice(
            nom=request.form.get('nom'),
            code=request.form.get('code'),
            groupe_id=request.form.get('groupe_id'),
            niveau_maitrise=request.form.get('niveau_maitrise')
        )
        db.session.add(nouvel_exo)
        db.session.commit()
        return redirect(url_for('recap'))
        
    groupes = GroupeMusculaire.query.all()
    return render_template('form.html', groupes=groupes)