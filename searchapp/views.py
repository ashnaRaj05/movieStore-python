from django.shortcuts import render
from movieapp.models import Snippet
from django.db.models import Q

def SearchResult(request):
    movies=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Snippet.objects.all().filter(Q(name__contains=query) | Q(cat__name__contains=query))
    return render(request,'search/search.html',{'query': query, 'movies': movies})


