
from bcrypt import hashpw, checkpw, gensalt
from urlApp import db
from datetime import datetime
from sqlalchemy.orm import relationship

BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE62_LENGTH = len(BASE62_ALPHABET)

def encode_base62(num):
        """Encode an integer to a Base62 string."""
        if num == 0:
            return BASE62_ALPHABET[0]
        
        encoded_str = ""
        while num > 0:
            remainder = num % BASE62_LENGTH 
            num = num // BASE62_LENGTH  
            encoded_str = BASE62_ALPHABET[remainder] + encoded_str
        return encoded_str


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    urls = relationship('URL', back_populates='user', cascade='all, delete-orphan')
    
    

    def __repr__(self):
        return f"Name : {self.username}, Email {self.email}, Date created {self.created_at}"


    def set_password(self, password):
        bytes = password.encode('utf-8') 
        salt = gensalt() 
        self.password_hash = hashpw(bytes, salt)
        

    def check_password(self, password):
        bytes = password.encode('utf-8') 
        return checkpw(bytes, self.password_hash)
    



class Url_shorts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(120), nullable=False)
    short_url = db.Column(db.String(120), nullable=True)
    visit = db.Column(db.Integer, default=0)
    last_visited = db.Column(db.DateTime, default=datetime.now)

    user = relationship('User', back_populates='urls')

    
    
    def shorten_url(self):
         code = encode_base62(self.id)
         self.short_url = "http://127.0.0.1:5000/"+code


