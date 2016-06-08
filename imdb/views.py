from django.http import HttpResponse
import movie_rater


def index(request):
    return HttpResponse("this is an index page")


def print_data(request, movie):
    json_data = movie_rater.json_parser(movie)
    return HttpResponse(json_data)
