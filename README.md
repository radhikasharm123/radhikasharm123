User Mention App
This is a simple social media app where users can create posts, comment on them, mention other users, and receive notifications.
The app is divided into separate parts (or sub-apps), each handling a specific feature like users, posts, comments, mentions, and notifications.
# here bash stands for terminal

Features
Users: Create and manage user accounts.
Posts: Add, update, delete, and view posts.
Comments: Add comments to posts.
Mentions: Mention other users in posts or comments.(in this case(app) you dont use @ but write the comment id and post id )
Notifications: Get alerts when you are mentioned.(but in ths you have to create a notification)
Requirements
Before starting, make sure you have these installed:

Python (version 3.8 or later) - To run the app.
Postman - To test the app.
MySQL - For storing app data.
How to Set Up and Run the App
Step 1: Download the App
Download the project files from the repository or copy them to your computer.
Open your terminal or command prompt and go to the project folder:
bash
Copy code
cd path/to/user-mention-app
Step 2: Create a Virtual Environment
This step helps keep the app’s files organized.

Create the environment:
bash
Copy code
python -m venv venv
Activate it:
Windows:
bash
Copy code
venv\Scripts\activate
Mac/Linux:
bash
Copy code
source venv/bin/activate
Step 3: Install Required Libraries
Install the necessary tools for the app to work:

bash
Copy code
pip install -r requirements.txt
Step 4: Set Up the Database
The app uses MySQL to save its data.

Open the app.py file in each sub-app folder (like user_app, post_app, etc.).
Look for this line:
python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/social_media_app_db'
Replace username and password with your MySQL details.
Step 5: Initialize the Database
In the terminal, run these commands:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Step 6: Start Each Sub-App
Each sub-app runs separately on a different port. Open a terminal for each and start them:

User App (Port: 5005):
bash
Copy code
python -m user_app.app
Post App (Port: 5004):
bash
Copy code
python -m post_app.app
Comment App (Port: 5001):
bash
Copy code
python -m comment_app.app
Notification App (Port: 5003):
bash
Copy code
python -m notification_app.app
Mention App (Port: 5002):
bash
Copy code
python -m mention_app.app
How to Use the App with Postman
Open Postman.
Import the Collection:
In Postman, go to File > Import.
Upload the Postman collection file provided with the project.
Set the Base URLs:
Go to the Postman environment and set the URLs for each sub-app:
User App: http://localhost:5001
Post App: http://localhost:5002
Comment App: http://localhost:5003
Notification App: http://localhost:5004
Mention App: http://localhost:5005
API Endpoints
You can test these actions in Postman:

# for running on postman everything has been specified in new collection postman collection

User App (Port: 5005)
Action	Method	URL	What it Does
Get all users	GET	/users	Lists all users
Create a user	POST	/users	Adds a new user
Get a specific user	GET	/users/<id>	Shows details of one user
Update a user	PUT	/users/<id>	Updates user information
Delete a user	DELETE	/users/<id>	Removes a user
Post App (Port: 5004)
Action	Method	URL	What it Does
Get all posts	GET	/posts	Lists all posts
Create a post	POST	/posts	Adds a new post
Get a specific post	GET	/posts/<id>	Shows details of one post
Update a post	PUT	/posts/<id>	Updates post content
Delete a post	DELETE	/posts/<id>	Removes a post
Comment App (Port: 5001)
Action	Method	URL	What it Does
Get all comments	GET	/comments	Lists all comments
Add a comment	POST	/comments	Adds a comment to a post
Get comments by post	GET	/comments/<post_id>	Lists comments for one post
Notification App (Port: 5003)
Action	Method	URL	What it Does
Get notifications	GET	/notifications/<user_id>	Lists notifications for a user
Create a notification	POST	/notifications	Creates a new notification
Mention App (Port: 5002)
Action	Method	URL	What it Does
Add a mention	POST	/mentions	Mentions a user in a post
Get user mentions	GET	/mentions/<user_id>	Lists all mentions for a user
Troubleshooting
App doesn’t start: Check that each sub-app is running on its correct port.
Database errors: Verify your MySQL details in the app.py file.
404 Errors: Double-check the URL and HTTP method (GET, POST, etc.).
IntegrityError: Ensure all required data is included in your requests.