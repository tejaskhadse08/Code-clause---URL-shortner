from django.shortcuts import render
from django.shortcuts import redirect as redi
from .models import ShortUrl
from .forms import CreateNewShortURL
from datetime import datetime
import random
import string

# Create your views here.


def home(request):
    return render(request, 'home.html')


def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if (form.is_valid()):
            org_web = form.cleaned_data['long_url']
            asciiChars = list(string.ascii_letters)
            s = ''
            for i in range(8):
                s += random.choice(asciiChars)
            while len(ShortUrl.objects.filter(short_url=s)) != 0:
                s = ''
                for i in range(8):
                    s += random.choice(asciiChars)
        URLObj = ShortUrl(long_url=org_web, short_url=s)
        URLObj.save()
        return render(request, 'urlcreated.html', {'chars': s})
    else:
        form = CreateNewShortURL()
        context = {'form': form}
        return render(request, 'create.html', context)


def redirect(request, url):
    obj = ShortUrl.objects.filter(short_url=url)
    if len(obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj': obj[0]}
    return redi(obj[0].long_url)
