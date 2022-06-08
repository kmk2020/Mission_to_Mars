#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install splinter


# In[2]:


# pip install webdriver_manager


# In[3]:


# pip install bs4


# In[4]:


# pip install pymongo


# In[5]:


# pip install splinter


# In[6]:


# pip install splinter


# In[7]:


# pip install selenium


# In[8]:


# pip install flask_pymongo


# In[ ]:





# In[9]:


import json
import pandas as pd

import numpy as np 


# In[10]:
 

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)



# In[11]:


app = Flask(__name__)


# In[12]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[13]:


@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# In[14]:


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)


# In[ ]:


if __name__ == "__main__":
   app.run()


# In[ ]:


def mars_news():

   # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   slide_elem = news_soup.select_one('div.list_text')

   # Use the parent element to find the first <a> tag and save it as `news_title`
   news_title = slide_elem.find('div', class_='content_title').get_text()

   # Use the parent element to find the paragraph text
   news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

return news_title, news_p

    # Add try/except for error handling
try:
    
    slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
    news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
except AttributeError:

return None, None

return news_title, news_p


# In[ ]:


def featured_image(browser):
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Add try/except for error handling
try:
    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

except AttributeError:
    return None

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

return img_url


# In[ ]:


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

