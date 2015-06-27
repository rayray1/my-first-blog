from django.db import models
from django.utils import timezone


# Posts model
class Post(models.Model): # an object - defines the model
	author = models.ForeignKey('auth.User') # link to another model
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def approved_comments(self):
		return self.comments.filter(approved=True)


	def __str__(self):
		return self.title



# Comments model
class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name='comments') # allows us to have access to comments from post model
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved = models.BooleanField(default=False)


	def approve(self):
		self.approved = True
		self.save()


	def __str__(self):
		return self.text














