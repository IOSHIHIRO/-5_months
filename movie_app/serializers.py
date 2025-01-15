from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews average_rating'.split()

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum(int(i.stars) for i in reviews if i.stars.isdigit())
            average = sum_reviews / len(reviews)
            return average
        return None



class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movie_set.count()

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=100)
    duration = serializers.CharField(required=False, max_length=100)
    director_id = serializers.CharField(required=True, max_length=100)

    def validate_director_id(self, director_id):
        try:
            Movie.objects.get(id=director_id)
        except:
            raise ValidationError('Director does not exist')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    test = serializers.CharField(required=True, max_length=100)
    movie_id = serializers.CharField()
    stars = serializers.CharField(required=True, min_length=1, max_length=100)

    def validate_movie_id(self, movie_id):
        try:
            Review.objects.get(id=movie_id)
        except:
            raise ValidationError('Movie does not exist')
        return movie_id






