import unittest
from app.models import News

class NewsTest(unittest.TestCase):

  '''
  Test class to test the behaviour of the News class
  '''
  def setUp(self):
    '''
    Setup() that will run before every test
    '''

    self.new_news = News("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general","en","us")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_news,News))