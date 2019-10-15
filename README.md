# NEWS_HIGHLIGHT

  This is a Python-Flask application for displaying News Highlights from various News sources using a [News API](https:newsapi.org/).

## Generated by John Karanja N

### View Live Site here

        To use this application, visit the live application link at:
        

## User Stories

        These are features that the application implements for use by a user.

            >> The home page presents users with an eye catching UI,information about the site and finally a NEWS SOURCE button that directs you to a modal with all news SOURCES.
            >> To view articles from a preferred source the user has to click on that source on the modal displayed.
            >> User can opt to use the navbar which presents a more organized drop down for redirectingto home page.
            >> Users can also choose to read articles from the Read articles button.

## BDD Specifications

| Behaviour      |          Input           |                                 Output                                  |
| :------------- | :----------------------: | :---------------------------------------------------------------------: |
| Homepage loads | Data from index mark up  |                        Displays information on how to use the site together with an Open Source button.                        |
| New page loads | Click on the source button to view displayed news source |               All sources with articles button to read from the source gets displayed                |
| On page load   | Click on any news source | Each article displays an image, title, description and publication date |
| New page loads |    Click on read about    |                 Redirects to the specific article page                  |

## SetUp & Installation Requirements

### Prerequisites

     Clone or download the Repo

1. Create a virtual environment
2. \$ python3.6 -m venv --without-pip virtual
3. \$ source virtual/bin/env
4. \$ curl https://bootstrap.pypa.io/get-pip.py | python
5. Installing Flask and other Modules
   $ python3.6 -m pip install Flask
     $ python3.6 -m pip install Flask-Bootstrap
   \$ python3.6 -m pip install Flask-Script
6. Edit the config.py file with your api key from the news.org website
7. Run manage.py
8. Access the application through `localhost:5000`


## Testing the Application

      - To run the tests for the class files:

             $ python3.6 run.py tests

## Technologies used

        - Python 3.6
        - Flask Framework
        - HTML, CSS and Bootstrap


## copyright

      ©2019 [John Karanja N.]

## Support and contact details

      tel:+254717067537 E_mail : kaiserjohn52@gmail.com

## Bugs

      >> Displaying of news articles images is not well arranged from server side.



## Acknowledge

      It will be a great pleasure for anyone who wishes to use my application and navigate through it.
