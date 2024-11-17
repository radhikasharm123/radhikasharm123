"""from flask import request
from notification_app.services.notification_service import NotificationService
from notification_app.views.notification_views import NotificationView

class NotificationController:
    @staticmethod
    def get_notifications(user_id):
        notifications = NotificationService.get_notifications_by_user(user_id)
        return NotificationView.render_notifications(notifications), 200
"""
from flask import request, jsonify
from notification_app.services.notification_service import NotificationService
from notification_app.views.notification_views import NotificationView

class NotificationController:
    @staticmethod
    def create_notification():
        # Get the incoming JSON data from the request body
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')

        # Check if the user_id and content are provided
        if not user_id or not content:
            return jsonify({"error": "user_id and content are required"}), 400

        # Create the notification using the service layer
        notification = NotificationService.create_notification(user_id, content)
        
        # Return a JSON response using the NotificationView to render the notification
        return jsonify(NotificationView.render_notification(notification)), 201

    @staticmethod
    def get_notifications(user_id):
        # Get notifications for the specific user from the service layer
        notifications = NotificationService.get_notifications_by_user(user_id)
        
        # Return a JSON response with all notifications for the user
        return jsonify(NotificationView.render_notifications(notifications))
