from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.all()


    context = {'topics':topics}

    return render(request, 'MainApp/topics.html', context)

## have a key and a value in context -- whatever you use as 
## the key needs to be referred in html, value is what you use in view
## just call them the same thing if possible