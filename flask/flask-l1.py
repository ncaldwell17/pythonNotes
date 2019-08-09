from flask import Flask
app = Flask(__name__)

# route is the way I access the website, in Flask I create this using decorators
# assigning two decorators to a single function allows me to mimic the index mentality of github or FutureQuest
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"
# keep in mind that nothing will update unless you quit out of the flask run
#   and restart everything from the beginning. CTRL + C quits the program.

# I can run this online in a mock development environment like Brackets by:
#   1. going to this python file's directory
#   2. running the following command  $ export FLASK_APP=name_of_py.py
#   3. running the next command $ flask run

# Debug Mode allows me to do changes in realtime.

# this is the way to produce new pages
@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)

# I can quit by CNTRL + C


