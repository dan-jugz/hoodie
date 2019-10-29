from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    current_user = request.user
    return render(request,'index.html', locals())


def post(request,id):
    post = Post.objects.get(id = id)
    return render(request, 'post.html', locals())


def business(request):
    profile = UserProfile.objects.get(user = request.user)
    return render(request, 'business.html',locals())


def new_business(request):
    return render(request,'new_business.html',locals)


def profile(request):
    return render(request,'profile.html',locals())


def edit_profile(request):
    return render(request,'edit_profile.html',locals())

