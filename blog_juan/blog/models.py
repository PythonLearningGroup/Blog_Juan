from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200)
	text = TextField()
	created_date = DateTimeField(default=timezone.now)
	published_date = DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
