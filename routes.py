from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

from models import Post, Category
from app import db

@app.route('/')
def index():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template("index.html",
                           posts=posts,
                           categories=categories)



@app.route('/addcategory', methods=['POST', 'GET'])
def addcategory():
    name = request.form['name']
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('app.index'))

@app.route('/addpost', methods=['POST', 'GET'])
def addpost():
    content = request.form['content']
    post = Post(content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('app.index'))

@app.route('/addtags', methods=['POST', 'GET'])
def addtags():
    tags = request.form.getlist('tags')
    post_id = request.form['post']
    post = db.session.query(Post).get(post_id)

    for tag in tags:
        category = db.session.query(Category).get(tag)
        post.tags.append(category)
    db.session.commit()
    return redirect(url_for('app.index'))