from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)

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


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Sign Up', 'Sign Up', css_class='btn-primary'))
	class Meta:
		model = User
		fields = ('username', 'email', 'password')