from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re
import json


def display_all_names(soup, item):
    all_names = []
    all_names = soup.findAll('span', itemprop=item)
    all_names = str(all_names)
    all_names = BeautifulSoup(all_names)
    all_names1 = all_names.findAll('span', itemprop="name")
    str1 = ""
    for values in all_names1:
        str1 = str1 + BeautifulSoup(str(values)).find('span').contents[0]+", "
    return str1


def get_soup(movie):
    movie_search = '+'.join(movie.split())
    url = "http://www.imdb.com/find?q=" + movie_search + "&s=all"
    br = Browser()
    try:
        br.open(url)
        link = br.find_link(url_regex=re.compile(r'/title/tt.*'))
        res = br.follow_link(link)
    except:
        return "error"
    else:
        soup = BeautifulSoup(res.read())
        return str(soup)


def get_movie_name(soup):
    try:
        movie_title = soup.find('title').contents[0]
    except:
        movie_title = "N/A"
    return movie_title


def get_movie_rate(soup):
    try:
        rate = soup.find('span', itemprop='ratingValue')
        rating = str(rate.contents[0])
    except:
        rating = "N/A"
    return rating


def get_writers_name(soup):
    try:
        writers = display_all_names(soup, "creator")
    except:
        writers = "N/A"
    return writers


def get_actors_name(soup):
    try:
        actors = display_all_names(soup, "actors")
    except:
        actors = "N/A"
    return actors


def get_directors_name(soup):
    try:
        directors = display_all_names(soup, "director")
    except:
        directors = "N/A"
    return directors


def json_parser(movie):
    soup = get_soup(movie)
    json_data = {}
    if soup == "error":
        json_data["error"] = "page not found"
        return json.dumps(json_data)
    else:
        soup = BeautifulSoup(soup)
        attributes = ['movie', 'rate', 'director', 'writer', 'actor']
        m_name = get_movie_name(soup)
        m_rate = get_movie_rate(soup)
        m_director = get_directors_name(soup)
        m_writer = get_writers_name(soup)
        m_actor = get_actors_name(soup)
        keywords = [m_name, m_rate, m_director, m_writer, m_actor]
        for index in range(len(attributes)):
            json_data[attributes[index]] = keywords[index]
        return json.dumps(json_data)
