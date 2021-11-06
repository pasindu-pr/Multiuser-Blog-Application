from datetime import datetime
from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500), nullable=False)
    profilePicture = db.Column(db.String(900))
    email = db.Column(db.String(500), nullable=False,unique=True)
    password = db.Column(db.String(900), nullable=False)
    confirmed_at = db.Column(db.DateTime())
    posts = db.relationship('Post', back_populates="user")
    role = db.Column(db.String(500), nullable=False, default="bloguser")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(500), nullable=False)
    postBody = db.Column(db.String(500000), nullable=False)
    image = db.Column(db.String(2000), nullable=False)
    views = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment')
    isApproved = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship("User", back_populates="posts")
    publishedDate = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.String(500), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),
        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship("User", foreign_keys=user_id)  