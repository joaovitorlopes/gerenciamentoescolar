from app import app, db
from flask import render_template, request
from app.models.tables import Professor

@app.route('/professores')
def listar_professores():
    p = Professor.query.all()
    return render_template('listar_professores.html', professor=p)