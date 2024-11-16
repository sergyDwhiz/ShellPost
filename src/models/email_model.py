from utils.db import db

class Email(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    classification = db.Column(db.String(50), nullable=False)

    def __init__(self, content, classification):
        self.content = content
        self.classification = classification

    def __repr__(self):
        return f'<Email {self.id}>'