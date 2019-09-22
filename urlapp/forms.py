
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name is', max_length=100)

class ArticleForm(forms.Form):
    your_name = forms.CharField(label='Your Name is', max_length=100)
    title = forms.CharField(label='Title of the Article', max_length=500)
    p1 = forms.CharField(label='Paragraph 1', max_length=1000)
    p2 = forms.CharField(label='Paragraph 2', max_length=1000)
    art_slug = forms.CharField(label='Slug', max_length=100)

