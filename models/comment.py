from models import db

class Comment(db.Model):

    __tablename__ = 'tbl_comment'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    news_id = db.Column(db.Integer, db.ForeignKey('tbl_news.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_user.id'))


    def __init__(self, title, content, create_time, news_id, author_id):
        self.title = title
        self.content = content
        self.create_time = create_time
        self.news_id = news_id
        self.author_id = author_id

    def __repr__(self):
        return '<Comment %r>' % self.title

