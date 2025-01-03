from rondo import db
from rondo.defaults import DEFAULT_PERMISSIONS

class Permissions(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Permission %r>' % self.name
    
    @staticmethod
    def add_default_permissions():
        for permission in DEFAULT_PERMISSIONS:
            db.session.add(Permissions(permission=permission))
            db.session.commit()