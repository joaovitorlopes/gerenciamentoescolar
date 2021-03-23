from app import app, db
from flask import render_template, request, redirect, url_for
from app.models.tables import Professor

@app.route('/professores')
def listar_professores():
    p = Professor.query.all()
    return render_template('listar_professores.html', professor=p)

@app.route('/professores/deletar/<int:professor_id>')
def deletar_professores():
    professor = Professor.query.filter_by(id=professor_id).first()
    db.session.delete(professor)
    db.session.commit()
    return redirect(url_for(listar_professores, msg='deletar'))