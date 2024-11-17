import sys
import os
sys.path.append(os.getcwd())

# app.py
from flask import Flask
from flask_migrate import Migrate
from shared.utils.db_utils import db
from notification_app.routes.notification_routes import notification_bp  # Import the notification blueprint

app = Flask(__name__)

# Configure the app's database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:radheybhai@localhost:3306/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migrations
db.init_app(app)
migrate = Migrate(app,db)

# Register the notification blueprint with a `url_prefix`
app.register_blueprint(notification_bp,)  # '/api' will be the prefix for all routes

@app.route('/')
def index():
    return 'Notification App is running'

if __name__ == '__main__':
    app.run(debug=True, port=5003)
