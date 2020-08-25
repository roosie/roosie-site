from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpRequest
from datetime import datetime
from django.http import HttpResponseRedirect


def home(request):
    """Renders the home page."""
    return render(
        request,
        'index.html',
        {
            'title':'Home Page'
        }
    )
def books(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'books.html',
        {
            'title':'Books',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def lifts(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'lifts.html',
        {
            'title':'Lifts',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def games(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'games.html',
        {
            'title':'Games',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def lola(request):
    return HttpResponseRedirect("http://lol-analytics.ycqim2bgtu.us-west-2.elasticbeanstalk.com/")
