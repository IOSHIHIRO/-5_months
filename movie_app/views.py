from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status

#Director
@api_view(['GET','PUT','DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director).data
        return Response(serializer)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def director_list_api(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        list_ = DirectorSerializer(directors, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        name = request.data.get('name')
        search_words = request.data.get('search_words')

        director = Director.objects.create(name=name)
        director.search_words = search_words
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)

#movie
@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie).data
        return Response(serializer)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        list_ = MovieSerializer(movies, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        search_words = request.data.get('search_words')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        movie.search_words = search_words
        movie.save()
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

#review
@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, id):
    try:
        review = ReviewSerializer.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review).data
        return Response(serializer)
    elif request.method == 'PUT':
        review.test = request.data.get('test')
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        list_ = ReviewSerializer(review, many=True).data
        return Response(data=list_)
    if request.method == 'POST':
        test = request.data.get('test')
        movie_id = request.data.get('movie')
        stars = request.data.get('stars')
        search_words = request.data.get('search_words')

        review = Review.objects.create(
            test=test,
            movie_id=movie_id,
            stars=stars
        )
        review.search_words.set(search_words)
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)