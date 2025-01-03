from rondo import db
from rondo.defaults import DEFAULT_ROLES

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Role %r>' % self.name
    
    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()
    
    @staticmethod
    def add_default_roles():
        for role in DEFAULT_ROLES:
            db.session.add(Role(role=role))
            db.session.commit()
           