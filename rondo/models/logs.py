from rondo import db
from rondo.models.users import Users

class Logs(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    meta_data = db.Column(db.String(350), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Logs %r>' % self.user_id