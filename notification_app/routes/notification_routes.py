"""from flask import Blueprint
from notification_app.controllers.notification_controller import NotificationController

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/api/notifications/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    return NotificationController.get_notifications(user_id)"""


# notification_app/routes/notification_routes.py
from flask import Blueprint
from notification_app.controllers.notification_controller import NotificationController

notification_bp = Blueprint('notification_bp', __name__)

# Endpoint to create a notification (called when a mention is detected)
@notification_bp.route('/api/notifications', methods=['POST'])
def create_notification():
    return NotificationController.create_notification()

# Endpoint to fetch notifications for a user
@notification_bp.route('/api/notifications/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    return NotificationController.get_notifications(user_id)
