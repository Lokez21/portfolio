from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        if password:
            self.set_password(password)

    def __repr__(self):
        return f'<User {self.username}>'

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # User's name
    job_title = db.Column(db.String(200), nullable=False)  # User's job title
    email = db.Column(db.String(120), nullable=True)  # User's email for contact
    linkedin_url = db.Column(db.String(200), nullable=True)  # LinkedIn profile URL
    github_url = db.Column(db.String(200), nullable=True)  # GitHub profile URL
    text = db.Column(db.Text, nullable=False)
    profile_image = db.Column(db.String(120), nullable=True) # Path to image
    
    def __repr__(self):
        return f'<About {self.id}>'

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    year_start = db.Column(db.Integer, nullable=False)
    year_end = db.Column(db.Integer, nullable=True) # Null if current
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Education {self.degree}>'

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    year_start = db.Column(db.Integer, nullable=False)
    year_end = db.Column(db.Integer, nullable=True) # Null if current
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Experience {self.role}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    blurb = db.Column(db.Text, nullable=False)  # Short description for the card
    description = db.Column(db.Text, nullable=True)  # Long description for the detail page
    image_url = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(200), nullable=True)
    link_visibility = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Project {self.title}>'

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Contact {self.name}>'
