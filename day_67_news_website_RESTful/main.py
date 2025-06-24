"""
main.py

A Flask-based blog application with RESTful routes, using SQLAlchemy for ORM, Flask-WTF for forms, and CKEditor for rich text editing.

Modules and Extensions:
- Flask: Web framework.
- Flask-Bootstrap: For Bootstrap 5 integration.
- Flask-SQLAlchemy: Database ORM.
- Flask-WTF: Form handling and validation.
- Flask-CKEditor: Rich text editor for blog content.
- WTForms: Form fields and validators.
- SQLAlchemy: ORM base and column types.
- datetime: For date handling.
- os: For file path management.

Database:
- SQLite database located in the instance folder.
- BlogPost model represents a blog post with fields: id, title, subtitle, date, body, author, img_url.

Forms:
- CreatePostForm: Form for creating and editing blog posts, with fields for title, subtitle, author, image URL, and body.

Routes:
- '/': Home page displaying all blog posts.
- '/post/<int:post_id>': Displays a single blog post.
- '/new-post': Form to create a new blog post.
- '/edit-post/<int:post_id>': Form to edit an existing blog post.
- '/delete-post/<int:post_id>': Deletes a blog post.
- '/about': About page.
- '/contact': Contact page.

Templates:
- Renders templates for index, post, make-post, about, and contact pages.

Other:
- Sets current year as a global Jinja variable for templates.
- Runs the app in debug mode on port 5003.
"""
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
# Current year
app.jinja_env.globals['current_year'] = date.today().year

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{current_dir}/instance/posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# CONFIGURE FORMS
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    with app.app_context():
        posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.query(BlogPost).get(post_id)
    return render_template("post.html", post=requested_post)


# add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

# edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=True, post_id=post_id)

# delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:post_id>", methods=["GET", "POST"])
def delete_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Additional routes for about and contact pages
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
