from django import forms
from .models import *

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['name',
                  'desc',
                  'cat',
                  'actors',
                  'img',
                  ]
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'desc': forms.Textarea(attrs={'class': "form-control"}),
            'cat': forms.Select( attrs={'class':"form-control"}),
            'actors': forms.TextInput(attrs={'class': "form-control"}),
            'img': forms.FileInput(attrs={'class': "form-control"}),
        }
class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ("comment","rating")