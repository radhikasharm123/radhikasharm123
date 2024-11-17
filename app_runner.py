import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen(["C:\\Users\\ANOOP KUMAR SHARMA\\user_mention_app\\venv\\Scripts\\python.exe", "user_app\\app.py"])

# Run the service corresponding to the post_app
def run_post_service():
    subprocess.Popen(["C:\\Users\\ANOOP KUMAR SHARMA\\user_mention_app\\venv\\Scripts\\python.exe", "post_app\\app.py"])
    
def run_comment_service():
    subprocess.Popen(["C:\\Users\\ANOOP KUMAR SHARMA\\user_mention_app\\venv\\Scripts\\python.exe", "comment_app\\app.py"])

def run_mention_service():
    subprocess.Popen(["C:\\Users\\ANOOP KUMAR SHARMA\\user_mention_app\\venv\\Scripts\\python.exe", "mention_app\\app.py"])

def run_notification_service():
    subprocess.Popen(["C:\\Users\\ANOOP KUMAR SHARMA\\user_mention_app\\venv\\Scripts\\python.exe", "notification_app\\app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()
    run_comment_service()
    run_mention_service()
    run_notification_service()
    
    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
