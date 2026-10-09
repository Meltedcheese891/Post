import flask
from flask import request

app = flask.Flask(__name__)

general_post = []
game_post = []
tv_post = []
book_post = []

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/games', methods = ["GET","POST"])
def games():

  if request.method == "POST":
    name = request.form["name"]
    subject = request.form["subject"]
    post = request.form["post"]

    post_obj = {"name":name, "subject": subject, "post":post}
    game_post.append(post_obj)
    return flask.render_template('game.html',posts = game_post)

@app.route('/general', methods = ["GET", "POST"])
def general():

  if request.method == "POST":
    name = request.form["name"]
    subject = request.form["subject"]
    post = request.form["post"]

    post_obj = {"name":name, "subject": subject, "post":post}
    general_post.append(post_obj)
  return flask.render_template('general.html',posts = general_post)

@app.route('/post')
def post():
  return flask.render_template('post.html')

@app.route('/tv')
def tv():
  return flask.render_template('tv.html')

@app.route('/books')
def books():
  return flask.render_template('books.html')

@app.route('/about')
def about():
  return flask.render_template('about.html')

if __name__ == "__main__":
  app.run()