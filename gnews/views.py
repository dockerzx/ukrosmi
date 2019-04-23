from django.shortcuts import render
from .lib import parseg

# Create your views here.
def index(request):
    #print('lol')
    news_list = parseg.scrape()
    #print (news_list)
    context = {
        'news_list': news_list
    }
    return render(request, 'index.html', context)
