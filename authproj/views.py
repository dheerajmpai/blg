from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1> <a href="https://sae.news">Hello</a>"""
   return HttpResponse(text)

def art(request, nn):
   text = """<h1>welcome to my app ! """+str(nn) +"""</h1> <a href="https://sae.news">Hello</a>"""
   return HttpResponse(text)


from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if (1):
        return HttpResponseNotFound('<h1>Page not found in the django</h1>')
    else:
        return HttpResponse('<h1>Page was found in the django</h1>')
