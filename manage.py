# manage.py
from flask import Flask
from flask_migrate import Migrate
from shared.utils.db_utils import db
from user_app.routes.user_routes import user_bp
from post_app.routes.post_routes import post_bp
from comment_app.routes.comment_routes import comment_bp
from mention_app.routes.mention_routes import mention_bp
from notification_app.routes.notification_routes import notification_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:radheybhai@localhost:3306/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(mention_bp)
app.register_blueprint(notification_bp)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return "Hello, Flask is running!"


