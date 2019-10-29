from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Business,UserProfile,NeighbourHood,Post

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
    hood = profile.neighbourhood
    posts = Post.objects.filter(neighbourhood = profile.neighbourhood)
    profile = UserProfile.objects.get(user = current_user)
    context = {
        "posts":posts,
        "profile":profile, 
        "businesses": businesses, 
        "hood": hood
    }
    return render(request,'index.html', context)


@login_required(login_url='/accounts/login')
def post(request,id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post = post)
    form = CommentForm(request.POST)
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request, 'post.html', context)


@login_required(login_url='/accounts/login')
def business(request):
    profile = UserProfile.objects.get(user = request.user)
    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
    context = {
        "businesses":businesses
    }
    return render(request, 'business.html',context)


@login_required(login_url='/accounts/login')
def new_business(request):
    profile = UserProfile.objects.get(user = request.user)
    form = BusinessForm()
    context = {
        'form': form
    }
    return render(request,'new_business.html',context)


@login_required(login_url='/accounts/login')
def profile(request):
    user = User.objects.get(username = username)
    profile = UserProfile.objects.get(user = user)
    businesses = Business.objects.filter(user = profile)
    context = {
        'profile': profile,
        'businesses': businesses
    }
    return render(request,'profile.html',context)


@login_required(login_url='/accounts/login')
def edit_profile(request):
    return render(request,'edit_profile.html',locals())

