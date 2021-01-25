from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'text': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
			}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)
		widgets = {
			'text': forms.Textarea(
				attrs={
					'class': 'form-control',
					'rows' : 4,
				}
			),
		}