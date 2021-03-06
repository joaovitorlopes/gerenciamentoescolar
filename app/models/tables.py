from app import db

class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    senha = db.Column(db.String(200))

    def __repr__(self):
        return '<Professor %s>' % self.nome


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    calculo = db.Column(db.String(20))

    def __repr__(self):
        return '<Disciplina %s>' % self.nome


class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    senha = db.Column(db.String(200))

    def __repr__(self):
        return '<Aluno %s>' % self.nome


class ProfessorDisciplina(db.Model):
    __tablename__ = 'professores_disciplinas'
    
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)

    def __repr__(self):
        return '<Professor Disciplina %s>' % self.professor_id


class Etapa(db.Model):
    __tablename__ = 'etapas'

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Etapa %s>' % self.descricao


class Nota(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    etapa_id = db.Column(db.Integer, db.ForeignKey('etapas.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return '<Nota %s>' % self.nota