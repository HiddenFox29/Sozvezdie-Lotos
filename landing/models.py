from django.db import models

# Create your models here.

class Partners(models.Model):
	class Meta:
		db_table = 'Partners'
		verbose_name = "База Партнеров"
		verbose_name_plural = "База Партнеров"

	name = models.CharField(max_length=100, db_index=True)
	email = models.EmailField(max_length=200, db_index=True)
	message = models.TextField(max_length=1000, blank=True)
	date_pub = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name