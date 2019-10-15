import unittest
from app.models import Articles  

class ArticlesTest(unittest.TestCase):

  '''
  Test class to test the behaviour of the News class
  '''
  def setUp(self):
    '''
    Setup() that will run before every test
    '''

    self.new_article = Articles("cnn","CNN","s.ghazal","The greatnes of the mind"," we are a limit to our selves","https://arabic.cnn.com/style/article/2019/10/14/performance-art-egyptian-photographer-medhat-soody","https://static.arabic.cnn.com/sites/default/files/styles/fb_image/public/2019/09/22/images/Capture.JPG?itok=p-qy8NMX","2019-10-14T07:34:41Z","(CNN)A hip-hop festival in Hong Kong, which would have featured American artists Migos and Wiz Khalifa, is the latest event to be canceled due to the city's ongoing unrest.\r\nRolling Loud, the two-day festival, was scheduled for October 19 and 20. Rapper Wiz K… [+2092 chars]")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))