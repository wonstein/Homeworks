import csv
import time
import re
import urllib2
from bs4 import BeautifulSoup
from nltk.util import clean_html

# from http://bobrochel.blogspot.com/2010/11/bad-servers-chunked-encoding-and.html
import httplib
def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except httplib.IncompleteRead, e:
            return e.partial

    return inner
httplib.HTTPResponse.read = patch_http_response_read(httplib.HTTPResponse.read)

def updateUrls(soup):
  for link in soup.findAll('a', {'href': re.compile(r"^http://")}):
    url = link['href']
    if url not in urls and url.startswith("http://www.younghouselove.com"): urls.append(url.encode())


def checkIsPost(soup, url):
  permanent_link = soup.find('a', attrs = {'rel':'bookmark'})
  if permanent_link == None: return False
  elif permanent_link['href'] == url: return True 
  else: return False
  
#posts = soup.findAll("h3", attrs = {'class':'h1'})

def gatherPostData(soup):
  # Find post title
  post_title = clean_html(str(soup.find('a', {'rel':'bookmark'})))
  
  # Find publish date
  date = clean_html(str(soup.find('div', {'class':'date'}).find('span')))
  
  # Find author
  author = clean_html(str(soup.find('a', {'rel':'author'})))
  
  # Find number of comments
  num_comments = int(clean_html(str(soup.find('div', {'class':'comm'}).find('a'))).split()[0].replace(',', ''))

  return [post_title, date, author, num_comments]
  
headers = ["id", "url", "is_post", "post_title", "publish_date", "author", "comment_count"]
is_post = []
post_titles = []
publish_dates = []
authors = []
urls = []
comment_counts = []  
  
blog_root = "http://www.younghouselove.com/2011/01/january-superlatives/"
urls = [blog_root]

with open('blog_data.csv', 'wb') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  i = 0
  while i < len(urls):
    print "\nPage Index: {0}".format(i)
    print "Current URL: {0}".format(urls[i])
    
    try:
      # Open page
      page = urllib2.urlopen(urls[i]) 
      time.sleep(1)
      soup = BeautifulSoup(page.read())
      
      # Update list of URLs
      updateUrls(soup)
      print "URLs to follow: {0}".format(len(urls))
      
      # Write data to CSV file
      if checkIsPost(soup, urls[i]):
        print gatherPostData(soup)
        writer.writerow([i, urls[i], True] + gatherPostData(soup))
      else: 
        print "Not a post"
        writer.writerow([i, urls[i], False, 'NA', 'NA', 'NA', 'NA'])
      page.close()
    except urllib2.HTTPError as e:
      print "{0}: {1}".format(e.errno, e.strerror)
    i += 1
  
  
  
  


