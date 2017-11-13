from django.http import HttpResponse
import movie_rater


def index(request):
    return HttpResponse("this is an index page")


def print_data(request, movie):
    movie_data = movie_rater.get_movie_info(movie)
    return HttpResponse(movie_data)
