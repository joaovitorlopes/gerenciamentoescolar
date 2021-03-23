from app import db
from app.models.tables import Aluno
from app.models.tables import Disciplina
from app.models.tables import Etapa
from app.models.tables import Nota
from app.models.tables import Professor
from app.models.tables import ProfessorDisciplina
import bcrypt

# Criando Aluno
senha_plana = 'Suporte99'
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
a1 = Aluno(nome='Joao', email='joao@gmail.com', senha=senha_encriptada)
a2 = Aluno(nome='Bruno', email='bruno@gmail.com', senha=senha_encriptada)
a3 = Aluno(nome='Pedro', email='pedro@gmail.com', senha=senha_encriptada)
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)
db.session.commit()

# Criando Disciplinas
d1 = Disciplina(nome='Front-END', calculo='soma')
d2 = Disciplina(nome='Lógica', calculo='soma')
d3 = Disciplina(nome='TCC', calculo='soma')
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.commit()

# Criando Etapas
dDisciplina = Disciplina.query.filter_by(nome='Tcc').first()
d1 = Disciplina(disciplina_id=dDisciplina.id, descricao='Uma materia de info')
d2 = Disciplina(disciplina_id=dDisciplina.id, descricao='Uma materia de info2')
db.session.add(d1)
db.session.add(d2)
db.session.commit()

#Criando Notas
n1 = Disciplina(aluno_id=aa,etapa_id=aa nota=10)
n2 = Disciplina(aluno_id=aa,etapa_id=aa nota=10)
n3 = Disciplina(aluno_id=aa,etapa_id=aa nota=10)
db.session.add(n1)
db.session.add(n2)
db.session.add(n3)
db.session.commit()

# Criando Professores
senha_plana = 'Suporte99'
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
p1 = Professor(nome='Marco', email='marco@gmail.com', senha=senha_encriptada)
p2 = Professor(nome='Juliano', email='juliano@gmail.com', senha=senha_encriptada)
p3 = Professor(nome='Edilberto', email='Edilberto@gmail.com', senha=senha_encriptada)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()