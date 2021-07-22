from django.urls import path
from movies_api.views import MoviesAPIView

urlpatterns = [
	path('movies/', MoviesAPIView.as_view()),
]
