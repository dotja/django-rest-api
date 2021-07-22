from django.db import models


CATEGORY = [
	('', 'Category'),
	('Cartoon', 'Cartoon'),
	('Documentary', 'Documentary'),
	('Action', 'Action')
]


class Movies(models.Model):
	movie_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	added_on = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=100, choices=CATEGORY)
	description = models.TextField(max_length=500)

