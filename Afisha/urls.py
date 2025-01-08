from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_list_api),
    path('api/v1/directors/<int:id>/', views.director_detail_view),
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.movies_detail_view),
    path('api/v1/reviews/', views.review_list_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_view),
]
