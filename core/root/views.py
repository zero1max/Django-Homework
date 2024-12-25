from django.shortcuts import render
from .models import Posts

# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request, './list.html', {'posts': posts})