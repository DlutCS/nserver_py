from models import db

class News(db.Model):

    __tablename__ = 'tbl_news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    comment_count = db.Column(db.Integer)
    read_count = db.Column(db.Integer)
    like_count = db.Column(db.Integer)
    dislike_count = db.Column(db.Integer)
    cover_url = db.Column(db.String(4096))
    category_id = db.Column(db.Integer, db.ForeignKey('tbl_category.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_user.id'))
    _comments = db.relationship('Comment', backref='news', lazy='dynamic')


    def __init__(self, title, content, create_time, comment_count, read_count, 
                 like_count, dislike_count, cover_url, category_id, author_id):
        self.title = title
        self.content = content
        self.create_time = create_time
        self.comment_count = comment_count
        self.read_count = read_count
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.cover_url = cover_url
        self.category_id = category_id
        self.author_id = author_id

    def __repr__(self):
        return '<User %r>' % self.username


