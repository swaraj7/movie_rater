from django.http import HttpResponse
import movie_rater


def index(request):
  return HttpResponse("Hello World, you are at imdb index")

def print_data(request, movie):
  json_data = movie_rater.json_parser(movie)
  return HttpResponse(json_data)
# Create your views here.
