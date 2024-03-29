from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse


# Create your views here.
# @login_required 
    # have to decide where/whether a login is required 
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, World. This is the Homepage. Take a test or sign in")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required 
def home(request):
    return HttpResponseRedirect(reverse_lazy('user_profile', args=[request.user.username]))

def user_profile(request, username):
    return render(request, 'user_profile.html', {'username':username})
    #return HttpResponse("coming soon")






from .forms import AddWordForm
def add_word(request):
    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            # do something with form input
            f = form.cleaned_data['new_word']
            user = request.user
            return render(request, 'test_add.html',{'word': f,'user': user.username})
    else:
        form = AddWordForm()
    return render(request, 'add_word.html', {'form': form})

def test_add(request):
    return render(request, 'test_add.html',{'word': added_word})


# def password_reset(request):  
#      password_reset(request)

# def password_change(request):
#     password_change(request)