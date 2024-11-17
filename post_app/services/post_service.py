from shared.models.post_model import Post
from shared.utils.db_utils import db
from notification_app.services.notification_service import NotificationService


class PostService:
    @staticmethod
    def create_post(user_id, content):
        new_post = Post(user_id=user_id, content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def update_post(post_id, new_content):
        
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            # Update the post content
            post.content = new_content
            db.session.commit()  # Commit the changes to the database
            return post  # Return the updated post
        return None  # 

    @staticmethod
    def delete_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
        return None



def create_post_with_mentions(author_id, content, mentioned_user_ids):
    # Create the post (existing logic)
    post = Post(author_id=author_id, content=content)
    db.session.add(post)
    db.session.commit()

    # Create notifications for mentioned users
    for user_id in mentioned_user_ids:
        NotificationService.create_notification(user_id, f"You were mentioned in a post: {content[:50]}")
