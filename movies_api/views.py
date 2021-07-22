from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Movies
from movies_api.serializers import MoviesSerializer


class MoviesAPIView(APIView):
	serializer_class = MoviesSerializer

	def get(self, request):
		
		movie_id = request.query_params.get('movie', None)

		if movie_id:
			movies = Movies.objects.filter(movie_id=movie_id)
		else:
			movies = Movies.objects.all()

		if movies:
			movie_serializer = self.serializer_class(movies, many=True)
			return Response(movie_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No movies found'}, status=status.HTTP_200_OK)

	def post(self, request):
		
		title = request.data.get('title', None)
		description = request.data.get('description', None)
		category = request.data.get('category', 'Cartoon')

		post_data = {
			'title': title,
			'description': description,
			'category': category
		}

		serializer = self.serializer_class(data=post_data)
		if serializer.is_valid(raise_exception=True):
			movie = serializer.save()

		if movie:
			return Response({'message': 'Successful new movie'}, status=status.HTTP_201_CREATED)
		return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request):
		
		movie_id = request.query_params.get('movie', None)

		movie = Movies.objects.get(movie_id=movie_id)

		if not movie:
			return Response({'message': 'No movies found'})

		title = request.data.get('title', None)
		if title:
			movie.title = title
			movie.save()

		description = request.data.get('description', None)
		if description:
			movie.description = description
			movie.save()

		category = request.data.get('category', None)
		if category:
			movie.category = category
			movie.save()

		return Response({'message': 'Update Complete'}, status=status.HTTP_200_OK)

	def delete(self, request):
		
		movie_id = request.query_params.get('movie', None)
		movie = Movies.objects.get(movie_id=movie_id)

		if not movie:
			return Response({'message': 'No movie found'}, status=status.HTTP_404_NOT_FOUND)

		movie.delete()
		return Response({'message': 'Movie removed'}, status=status.HTTP_200_OK)

