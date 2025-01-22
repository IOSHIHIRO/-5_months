from django.urls import path
from movie_app import views

urlpatterns = [
    path('api/v1/directors/', views.DirectorListApiView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailView.as_view()),
    path('api/v1/movies/', views.MovieListApiView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailView.as_view()),
    path('api/v1/reviews/', views.ReviewListApiView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView.as_view()),

]