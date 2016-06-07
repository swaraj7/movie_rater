from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re
import json

def display_all_names(soup, item):
  all_names=[]
  all_names = soup.findAll('span', itemprop=item)
  all_names = str(all_names)
  all_names = BeautifulSoup(all_names)
  all_names1 = all_names.findAll('span', itemprop="name")
  str1=""
  for values in all_names1:
    str1 = str1 + BeautifulSoup(str(values)).find('span').contents[0]+", "
  return str1

def get_soup(movie):
  print movie
  movie_search = '+'.join(movie.split())
  url = "http://www.imdb.com/find?q="+ movie_search +"&s=all"
  print url
  br = Browser()
  try:
    br.open(url)
    link = br.find_link(url_regex = re.compile(r'/title/tt.*'))
    res = br.follow_link(link)
  except:
    print "wrong movie name"
    return ""
  else:
    soup = BeautifulSoup(res.read())
    return soup

def get_movie_name(soup):
  movie_title = soup.find('title').contents[0]
  return movie_title

def get_movie_rate(soup):
  rate = soup.find('span',itemprop='ratingValue')
  rating = str(rate.contents[0])
  return rating

def get_writers_name(soup):
  writers = display_all_names(soup, "creator")
  return writers
 
def get_actors_name(soup):
  actors = display_all_names(soup, "actors")
  return actors

def get_directors_name(soup):
  directors = display_all_names(soup, "director")
  return directors

def json_parser(movie):
  soup = get_soup(movie)
  m_name = get_movie_name(soup)
  m_rate = get_movie_rate(soup)
  m_director = get_directors_name(soup)
  m_writer = get_writers_name(soup)
  m_actor = get_actors_name(soup)

  json_data = []
  json_data.append({'movie':m_name})
  json_data.append({'year':m_year})
  json_data.append({'rate':m_rate})
  json_data.append({'director':m_director})
  json_data.append({'writer':m_writer})
  json_data.append({'actor':m_actor})
  return json.dumps(json_data)

if __name__ == '__main__':
  main
  
