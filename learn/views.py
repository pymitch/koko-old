from django.shortcuts import render
from django.http import HttpResponse

from .models import Word

# Create your views here.
def index(request):
    return HttpResponse("Hello, World. This is the learning section. Please sign in")

def word(request, word):
    ##find word 
    ##w = Word( )
    context = {
        'parts': w.parts,
        'blank_space': w.blank_space,
    }
    return render(request, 'learn/word.html',context)