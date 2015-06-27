from django import forms
from .models import Post, Comment

# Postform
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)



# Comments form
class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)
