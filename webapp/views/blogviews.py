from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import desc
from webapp.forms.addPost import AddPostForm 
from ..utils.fileUploader import FileUploader
from .. import db
# from ..models.post import Post
from ..models import Post, Comment

blogviews = Blueprint('blogviews', __name__)


@blogviews.route("/")
def home():
    topRatedPosts = db.session.query(Post).filter_by(isApproved=True).order_by(desc(Post.views)).limit(6).all()
    newPosts = db.session.query(Post).filter_by(isApproved=True).order_by(desc(Post.publishedDate)).limit(12).all()
    return render_template("index.html", topRatedPosts=topRatedPosts, newPosts=newPosts)


@blogviews.route("/post/<postid>/<postname>")
@login_required
def viewPost(postid, postname):
    if not postid or not postname:
        return redirect(url_for("blogviews.home"))
    selectedPost = db.session.query(Post).filter_by(id=postid).first()
    selectedPost.views += 1
    db.session.commit()
    readTime = round(len(selectedPost.postBody.split()) / 250)
    if(readTime == 0):
        readTime = 1

    return render_template("post.html", post=selectedPost, readTime=readTime)


@blogviews.route("/add-post", methods=["GET", "POST"])
@login_required
def addPost():
    form = AddPostForm() 
    if request.method == 'POST' and form.validate_on_submit():
        postHeading = form.heading.data
        image = form.postImage.data
        postBody = form.postContent.data
         
        fileUploader = FileUploader(image) 

        if(fileUploader.isImage()):
            uploadedUrl = fileUploader.uploadToCloudinary()

        if fileUploader.isUploaded:
            newPost = Post(headline=postHeading, image=uploadedUrl, postBody=postBody, user_id=current_user.get_id())
            db.session.add(newPost)
            db.session.commit()
            return redirect(url_for("blogviews.home"))

        else:
            return "Something went wrong!" 
        
    return render_template("addPost.html", form=form)


@blogviews.route("/comment/<postid>/<postname>", methods=["POST"])
@login_required
def addComment(postid,postname):
    comment = request.form.get("comment")
    newComment = Comment(comment_body=comment, post_id=postid, user_id=current_user.get_id())
    db.session.add(newComment)
    db.session.commit()
    return redirect(url_for('blogviews.viewPost', postid=postid, postname=postname))


@blogviews.route("/post/delete/<postid>", methods=["GET", "POST"])
@login_required
def deletePost(postid):
    postToDelete = db.session.query(Post).filter_by(id=postid).first()
    publicID = 'WeirdDiary/uploads/' + postToDelete.image.rsplit('/', 1)[-1].rsplit(".")[0]
    FileUploader.deleteFileFromCloudinary(publicid=publicID)
    db.session.query(Post).filter_by(id=postid).delete()
    db.session.commit()
    return redirect(url_for("authviews.myaccount"))
