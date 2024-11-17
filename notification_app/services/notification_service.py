"""from shared.models.notification_model import Notification
from shared.utils.db_utils import db

class NotificationService:
    @staticmethod
    def create_notification(user_id, content):
        notification = Notification(user_id=user_id, content=content)
        db.session.add(notification)
        db.session.commit()
        return notification

    @staticmethod
    def get_notifications_by_user(user_id):
        return Notification.query.filter_by(user_id=user_id).all()



"""

from shared.models.notification_model import Notification
from shared.utils.db_utils import db
class NotificationService:
    @staticmethod
    def create_notification(user_id, content):
        # Create a new notification object
        new_notification = Notification(user_id=user_id, content=content)
        
        # Save it to the database
        db.session.add(new_notification)
        db.session.commit()
        
        return new_notification

    @staticmethod
    def get_notifications_by_user(user_id):
        # Fetch all notifications for the given user_id
        return Notification.query.filter_by(user_id=user_id).all()
