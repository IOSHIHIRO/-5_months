from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status

#Director
@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director).data
    return Response(serializer)

@api_view(['GET'])
def director_list_api(request):
    directors = Director.objects.all()
    list_ = DirectorSerializer(directors, many=True).data
    return Response(data=list_)

#movie
@api_view(['GET'])
def movies_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie).data
    return Response(serializer)

@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    list_ = MovieSerializer(movies, many=True).data
    return Response(data=list_)

#review
@api_view(['GET'])
def reviews_detail_view(request, id):
    try:
        review = ReviewSerializer.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review).data
    return Response(serializer)

@api_view(['GET'])
def review_list_view(request):
    review = Review.objects.all()
    list_ = ReviewSerializer(review, many=True).data
    return Response(data=list_)