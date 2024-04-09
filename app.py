from flask import Flask, render_template
from pylogix import PLC
import threading
import time

# Create a Flask app
app = Flask(__name__, template_folder='templates')


# Create a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

should_continue = False

def loop_function():
    global should_continue
    while should_continue:
        print("Loop is running")
        time.sleep(1)  # Simulate work by sleeping



@app.route('/start')
def start():
    global should_continue
    if not should_continue:
        should_continue = True
        thread = threading.Thread(target=loop_function)
        thread.start()
        print("Loop has started!")
        return "Loop has started!"
    else:
        print("Loop is already running.")
        return "Loop is already running."

@app.route('/stop')
def stop():
    global should_continue
    should_continue = False
    print("Loop has stopped!")
    return "Loop has stopped!"



if __name__ == '__main__':
    app.run()