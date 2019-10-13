class News:

  '''
  News class to define News Objects
  '''

  def __init__(self,author,title,description,url,urlToImage,publishedAt,content):

    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = 'https://static.politico.com/8f/41/eaa45a8e4aa7819748b65d8ce6ca/191012-joe-biden-gty-773.jpg'
    self.publishedAt = publishedAt
    self.content = content
