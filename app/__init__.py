from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:Suporte99@localhost/gerenciamentoescolar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models.tables import Professores

from app.controllers import alunos
from app.controllers import disciplinas
from app.controllers import etapas
from app.controllers import notas
from app.controllers import professores