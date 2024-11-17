import sys
import os
sys.path.append(os.getcwd())



from flask import Flask
from flask_migrate import Migrate  
from shared.utils.db_utils import db
from config.config import Config

# Import Blueprints
from user_app.routes.user_routes import user_bp
from post_app.routes.post_routes import post_bp
from comment_app.routes.comment_routes import comment_bp
from notification_app.routes.notification_routes import notification_bp

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
migrate = Migrate(app, db)  


app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(notification_bp)

@app.route('/')
def index():
    return 'User Mention API is running'

if __name__ == '_main_':
    app.run(debug=True, port=5000)