"""from datetime import datetime
from shared.utils.db_utils import db

class Mention(db.Model):
    __tablename__ = 'mentions'

    mention_id = db.Column(db.Integer, primary_key=True)
    mentioned_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    """
from datetime import datetime
from shared.utils.db_utils import db

class Mention(db.Model):
    __tablename__ = 'mentions'

    mention_id = db.Column(db.Integer, primary_key=True)
    mentioned_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), nullable=True)  # Nullable for post mentions
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=True)  # Nullable for comment mentions
    created_at = db.Column(db.DateTime, default=datetime.utcnow)



    mentioned_user = db.relationship('User', backref='mentions', lazy=True)
    comment = db.relationship('Comment', backref='mentions', lazy=True)
    post = db.relationship('Post', backref='mentions', lazy=True)
    def __init__(self, mentioned_user_id, comment_id=None, post_id=None):
        self.mentioned_user_id = mentioned_user_id
        self.comment_id = comment_id
        self.post_id = post_id
