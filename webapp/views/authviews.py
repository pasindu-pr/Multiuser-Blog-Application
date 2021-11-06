from flask import Blueprint, render_template,request, redirect, url_for, flash
from flask_login.utils import login_required
from ..utils.fileUploader import FileUploader
from ..models import User
from ..forms.loginForm import LoginForm
from ..forms.registerForm import RegisterForm
from .. import db
import bcrypt
from flask_login import login_user, current_user, logout_user

authviews = Blueprint('authviews', __name__)

@authviews.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm() 
    
    if request.method == "POST" and form.validate_on_submit(): 
        name = form.name.data
        email = form.email.data
        userImage = form.userImage.data 
        password = form.password.data
        confirmPw = form.confirmPassword.data 


        if password == confirmPw:
            fileuploader = FileUploader(userImage)
            
            if fileuploader.isImage():
                uploadedUrl = fileuploader.uploadToCloudinary()
            
            else:
                flash("Your uploaded image format is not supported!", category="error")
                return redirect(url_for("authviews.register"))

            hashedPassword = bcrypt.hashpw(password=password.encode('utf8'), salt=bcrypt.gensalt(12))
            newUser = User(username=name, email=email, password=hashedPassword, profilePicture=uploadedUrl)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for("authviews.login")) 

        else:
            return "Something went wrong!"

    return render_template("register.html", form=form)


@authviews.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data 

        userExist = db.session.query(User).filter_by(email=email).count()

        if userExist > 0:
            user = db.session.query(User).filter_by(email=email).first()
            passToCheck = user.password.encode('utf8')

            try:
                if bcrypt.checkpw(password.encode('utf8'), passToCheck):
                    login_user(user=user, remember=True)
                    return redirect(url_for("blogviews.home"))

            except ValueError:
                    flash("Your username or password is incorrect!", category="error")
                    return redirect(url_for("authviews.login"))

        else:
            flash("We coundn't find your account! Create an account if you are not registered!", category="error")
            return redirect(url_for("authviews.login"))

    return render_template("login.html", form=form)


@authviews.route("/myaccount")
@login_required
def myaccount():
    return render_template("myaccount.html")


@authviews.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("authviews.login")) 