from flask import Blueprint
from user_app.controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_bp.route('/api/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/api/users/login', methods=['POST'])
def login_user():
    return UserController.login_user()
@user_bp.route('/api/users', methods=['GET'])
def get_all_users():
    print("ss")
    return UserController.get_all_users()

