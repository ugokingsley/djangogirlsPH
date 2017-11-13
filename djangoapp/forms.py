from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['title','content']

    def clean_email(self):
        content= self.cleaned_data.get('content')
        return content

    def clean_title(self):
        title=self.cleaned_data.get('title')
        return title





