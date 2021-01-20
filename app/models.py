from app import db


helper = db.Table('association_director_episode', db.metadata,
    db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True),
    db.Column('episode_id', db.Integer, db.ForeignKey('episode.id'), primary_key=True))


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    episodes = db.relationship('Episode', secondary=helper, back_populates="directors", lazy='dynamic')


class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), index=True, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    viewed = db.relationship('Viewed', backref="wju", lazy='dynamic')
    directors = db.relationship('Director', secondary=helper, back_populates="episodes", lazy='dynamic')


class Viewed(db.Model):
    __tablename__ = 'viewed'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    viewed = db.Column(db.Boolean())
    episodes = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)

