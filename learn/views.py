from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import Word

# Create your views here.
@login_required
def index(request):
    return HttpResponse("Hello, World. This is the learning section. Please sign in")

def word(request, w): 
    #replace try/except block with:
    w = get_object_or_404(Word, word=w)
    context = {
        'part1': w.parts()[0],
        'blank_space': w.blank_space,
        'part2': w.parts()[1],
    }
    return render(request, 'learn/word.html',context)
