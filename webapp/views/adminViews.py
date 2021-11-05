from flask import Blueprint, render_template, request, redirect, url_for
from flask_login.utils import login_required
from ..utils.adminDecorator import admin_protected
from ..models import Post
from .. import db

adminviews = Blueprint('adminviews', __name__)


@adminviews.route("/")
@login_required
@admin_protected
def home():
    unapprovedPosts = db.session.query(Post).filter_by(isApproved=False).all()
    return render_template("adminAccount.html", unapprovedPosts=unapprovedPosts)


@adminviews.route("/approve/<postid>")
@login_required
@admin_protected
def approvepost(postid):
    post = db.session.query(Post).filter_by(id=postid).first()
    post.isApproved = True
    db.session.commit()
    return redirect(url_for("adminviews.home"))