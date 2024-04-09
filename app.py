from flask import Flask, render_template
from pylogix import PLC
import threading
import time

# Create a Flask app
app = Flask(__name__, template_folder='templates')

# Global variable to control the loop
SHOULD_CONTINUE = False

# Create a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Create a route to start the loop
@app.route('/start')
def start():
    global SHOULD_CONTINUE
    if not SHOULD_CONTINUE:
        SHOULD_CONTINUE = True
        thread = threading.Thread(target=loop_function)
        thread.start()
        # print("Loop has started!")
        return "Loop has started!"
    else:
        # print("Loop is already running.")
        return "Loop is already running."

# Create a route to stop the loop
@app.route('/stop')
def stop():
    global SHOULD_CONTINUE
    SHOULD_CONTINUE = False
    # print("Loop has stopped!")
    return "Loop has stopped!"

# Function to run in the loop
def loop_function():
    global SHOULD_CONTINUE
    while SHOULD_CONTINUE:
        print("Loop is running")
        time.sleep(1)  # Simulate work by sleeping
    print("Loop has stopped")

if __name__ == '__main__':
    app.run()