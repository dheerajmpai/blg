from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm, ArticleForm
import numpy as np


# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')

def thank_view(request):
    return HttpResponse('<h1>Thank You</h1>')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            a = form.cleaned_data['your_name']
            ff = open('aa.txt', 'a')
            ff.write(a)
            ff.close()
            print (a)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/article/'+str(a))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
    
    
from .models import ArticleModel

def get_article(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            a = form.cleaned_data['your_name']
            b = form.cleaned_data['title']
            c = form.cleaned_data['p1']
            d = form.cleaned_data['p2']
            e = form.cleaned_data['art_slug']
            s = np.random.randint(99999999)
            slug_e = str(e) + '-' + str(s)
            article = ArticleModel(str(s), author = a, title = b, para1 = c, para2 =d, art_slug = slug_e)
            ff = open('aa.txt', 'a')
            ff.write(a)
            ff.write('\n')
            ff.write(b)
            ff.write('\n')
            ff.write(c)
            ff.write('\n')
            ff.write(d)
            ff.write('\n Slug :')
            ff.write(e)
            ff.write('\nTHis is the String from DB \n')
#            ff.close()
            print (a)
            article.save()
            string_e = str(article.author)+ str(article.title) + str(article.art_slug)
            print (string_e)
            ff.write(string_e)
            ff.write('\n')
            ff.close()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/article/'+str(a))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleForm()

    return render(request, 'name.html', {'form': form})
