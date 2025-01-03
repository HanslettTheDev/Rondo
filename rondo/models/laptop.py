from rondo import db

class LaptopTable(db.Model):
    __tablename__ = "laptop"

    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(80), nullable=False, unique=True)
    brand_model_name = db.Column(db.String(80), nullable=False, unique=True)
    brand_specifications = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer)
    date_entered = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Laptop %r>' % self.brand_name
    

class laptopIventory(db.Model):
    __tablename__ = "laptop_inventory"

    id = db.Column(db.Integer, primary_key=True)
    laptop_id = db.Column(db.Integer, db.ForeignKey("laptop.id"), nullable=False)
    defects_info = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Laptop %r>' % self.laptop_id