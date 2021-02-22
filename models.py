from app import db

class Show(db.Model):
  __tablename__ = 'Show'
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key = True)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key = True)
  start_time = db.Column(db.String, nullable=True)
  venue = db.relationship('Venue', back_populates='venue_shows')
  artist = db.relationship('Artist', back_populates='artist_shows')

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    website = db.Column(db.String(300))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))
    venue_shows = db.relationship('Show', back_populates='venue', lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    website = db.Column(db.String(300))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))
    artist_shows = db.relationship('Show', back_populates='artist', lazy=True)