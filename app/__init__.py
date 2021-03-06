from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ os.getenv("DB_USUARIO") + ':'+ os.getenv("DB_PASSWORD") +'@'+ os.getenv("DB_LOCAL") + '/' + os.getenv("DB_DATABASE")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models.tables import Aluno
from app.models.tables import Disciplina
from app.models.tables import Etapa
from app.models.tables import Nota
from app.models.tables import Professor
from app.models.tables import ProfessorDisciplina

from app.controllers import alunos
from app.controllers import disciplinas
from app.controllers import etapas
from app.controllers import notas
from app.controllers import professores