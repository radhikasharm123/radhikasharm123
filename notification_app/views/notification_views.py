"""class NotificationView:
    @staticmethod
    def render_notification(notification):
        return{ {
            "notification_id": notification.notification_id,
            "user_id": notification.user_id,
            "content": notification.content,
            "created_at": notification.created_at
        }
               for n in notification
               }

    @staticmethod
    def render_notifications(notifications):
        return [NotificationView.render_notification(notification) for notification in notifications]"""


class NotificationView:
    @staticmethod
    def render_notification(notification):
        # Render a single notification as a dictionary
        return {
            "id": notification.notification_id,
            "user_id": notification.user_id,
            "content": notification.content,
            "created_at": notification.created_at,
            "is_read": notification.is_read
        }

    @staticmethod
    def render_notifications(notifications):
        # Render a list of notifications
        return [NotificationView.render_notification(notification) for notification in notifications]
