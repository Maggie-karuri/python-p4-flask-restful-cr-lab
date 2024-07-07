from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    price = db.Column(db.Float, default=0.0) 


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": float(self.price)  # Convert Decimal to float for JSON serialization
        }
    def __repr__(self):
        return f'<Plant {self.id}: {self.name}>'
