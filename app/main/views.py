from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_articles
from ..models import Articles


# Views

@main.route('/')
def index():

  '''

  View root page that returns the index page and its data
  '''

  # Getting news source

  news_source = get_news('source')
  news_trending = get_news('trending')


  title = 'Home - Welcome to the best news app'

  return render_template('index.html',title = title,source = news_source, trending = news_trending)


@main.route('/news/<id>')
def news(id):

  '''
  View news page function that returns the movie details page and its data
  '''

  news = get_articles(id)
  # description = f'{id} | All Articles'

  return render_template('news.html',news = news)