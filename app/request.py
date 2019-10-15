import urllib.request,json
from .models import News,Articles



# Getting api key

api_key = None

# Getting the base url

base_url = None

#Getting the articles base url

articles_base_url = None


def configure_request(app):

  global api_key,base_url,articles_base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']
  articles_base_url = app.config["ARTICLE_BASE_URL"]





def get_news(category):
  '''
  function that gets the json response to our url request
  '''

  get_news_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None


    if get_news_response['sources']:
      news_results_list = get_news_response['sources']
      news_results = process_results(news_results_list)


  return news_results



def process_results(news_list):
  '''
  Function that processes the news result and transform them to a list of objects

  Args: 
      news_results: a list of dictionaries that contain details

  Returns :
      news_reults : A list of news objects
  
  '''

  news_results = []
  for news_item in news_list:
    id = news_item.get('id')
    name = news_item.get('name')
    description = news_item.get('description')
    url = news_item.get('url')
    category = news_item.get('category')
    language = news_item.get('language')
    country = news_item.get('country')

    if description:
      news_object = News(id,name,description,url,category,language,country)
      news_results.append(news_object)
  

  return news_results


def get_articles(id):

  get_articles_url = articles_base_url.format(id)

  with urllib.request.urlopen(get_articles_url)as url:

    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)


    articles_results = None


    if get_articles_response['articles']:
      articles_results_list =get_articles_response['articles']
      articles_results = process_results_articles(articles_results_list)

  return articles_results



def process_results_articles(articles_list):
  '''
  Function that processes the articles result and transform them to a list of objects

  Args: 
      articles_results: a list of dictionaries that contain details

  Returns :
      articles_reults : A list of articles objects
  
  '''


  articles_results = []
  for articles_item in articles_list:
    id = articles_item.get('id')
    name = articles_item.get('name')
    author = articles_item.get('author')
    title = articles_item.get('title')
    description = articles_item.get('description')
    url = articles_item.get('url')
    urlToImage = articles_item.get('urlToImage')
    publishedAt = articles_item.get('publishedAt')
    content = articles_item.get('content')

    if description:
      articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
      articles_results.append(articles_object)

  return articles_results

    

       