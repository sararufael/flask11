from app import db

tags = db.Table('tags',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))

    tags = db.relationship('Category', secondary=tags,
                           backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.content


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name