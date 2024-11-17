from shared.models.comment_model import Comment
from shared.utils.db_utils import db
from notification_app.services.notification_service import NotificationService

class CommentService:
    @staticmethod
    def create_comment(post_id, user_id, content):
        comment = Comment(post_id=post_id, user_id=user_id, content=content)
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def get_comments_by_post(post_id):
        return Comment.query.filter_by(post_id=post_id).all()

def create_comment_with_mentions(author_id, post_id, content, mentioned_user_ids):
    # Create the comment (existing logic)
    comment = Comment(author_id=author_id, post_id=post_id, content=content)
    db.session.add(comment)
    db.session.commit()

    # Create notifications for mentioned users
    for user_id in mentioned_user_ids:
        NotificationService.create_notification(user_id, f"You were mentioned in a comment: {content[:50]}")
