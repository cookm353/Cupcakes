"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Cupcake(db.Model):
    __tablename__ = 'cupcakes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default='https://tinyurl.com/demo-cupcake')
    
    def get_cupcakes():
        # return Cupcake.query.all().order_by(Cupcake.id.desc())
        return Cupcake.query.order_by(Cupcake.id.asc()).all()
        
    def get_cupcake(id):
        return Cupcake.query.get_or_404(id)
        
    def serialize_cupcake(cupcake):
        return {
            'id': cupcake.id,
            'flavor': cupcake.flavor,
            'size': cupcake.size,
            'rating': cupcake.rating,
            'image': cupcake.image
            }
        
    def make_cupcake(data):
        if data.get('image'):
            cupcake = Cupcake(flavor=data['flavor'], size=data['size'],
                          rating=data['rating'], image=data['image'])
        else:
            cupcake = Cupcake(flavor=data['flavor'], size=data['size'],
                          rating=data['rating'])
        
        db.session.add(cupcake)
        db.session.commit()
        
        return cupcake
        
    def edit_cupcake(cupcake, new_data):
        """Update a cupcake"""
        cupcake.flavor = new_data.json.get('flavor', cupcake.flavor)
        cupcake.size = new_data.json.get('size', cupcake.size)
        cupcake.rating = new_data.json.get('rating', cupcake.rating)
        cupcake.image = new_data.json.get('image', cupcake.image)
        
        # cupcake.flavor = new_data.get('flavor', cupcake.flavor)
        # cupcake.size = new_data.get('size', cupcake.size)
        # cupcake.rating = new_data.get('rating', cupcake.rating)
        # cupcake.image = new_data.get('image', cupcake.image)
                
        db.session.commit()
        
    def delete_cupcake(id):
        Cupcake.query.filter_by(id=id).delete()
        db.session.commit()  
        
    def __repr__(self):
        return f'<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image}>'