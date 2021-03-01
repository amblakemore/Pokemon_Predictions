def create_classes(db):
    class Pokemon(db.Model):
        __tablename__ = 'pokemon'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))

        def __repr__(self):
            return '<Pokemon %r>' % (self.name)
    return Pokemon

# Database Setup

from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL will contain the database connection string:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connects to the database using the app config
db = SQLAlchemy(app)

Pokemon = create_classes(db)