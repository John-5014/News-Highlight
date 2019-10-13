import unittest
from models import news

News = news.News

class NewsTest(unittest.TestCase):

  '''
  Test class to test the behaviour of the News class
  '''
  def setUp(self):
    '''
    Setup() that will run before every test
    '''

    self.new_news = News(' ','A noun, a verb and Rudy Giuliani: Biden new punchline - POLITICO',' ','https://www.politico.com/news/2019/10/13/joe-biden-rudy-giuliani-2020-045163','https://static.politico.com/8f/41/eaa45a8e4aa7819748b65d8ce6ca/191012-joe-biden-gty-773.jpg',"2019-10-13T10:48:00Z","Biden this week decided to begin framing Giuliani and, by proxy, the president as a corrupt, bungling leader of a gang that couldnt shoot straight. Then came the arrests which reinforced Bidens Giuliani strategy. \r\nThey just got arrested at the airport, with … [+9834 chars]")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_news,News))




if __name__ == '__main__':
  unittest.main()