from flask import render_template
from app import app

# Views

@app.route('/')
def index():

  '''

  View root page that returns the index page and its data
  '''

  title = 'Home - Welcome to the best news app'

  return render_template('index.html',title = title)


@app.route('/news/<int:news_id>')
def news(news_id):

  '''
  View news page function that returns the movie details page and its data
  '''

  return render_template('news.html',id = news_id)