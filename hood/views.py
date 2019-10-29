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
    try:
        profile = UserProfile.objects.get(user = current_user)
    except:
        profile = UserProfile.objects.create(name = request.user.username, user = request.user)
        profile.save()
        return redirect('edit_profile',username = current_user.username)
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


def new_post(request):
    profile = UserProfile.objects.get(user = request.user)
    form = PostForm()
    context = {
        "profile":profile,
        "form":form
    } 
    return render(request,'new_post.html', context)


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
    profile = UserProfile.objects.get(user=request.user)
    form = ProfileForm()
    context = {
        "form":form
    }
    return render(request,'edit_profile.html',context)


@login_required(login_url='/accounts/login')
def search(request):
    if 'business' in request.GET and request.GET['business']:
        profile = UserProfile.objects.get(user = request.user)
        search_term = request.GET.get('business')
        results = Business.objects.filter(neighbourhood = profile.neighbourhood, name__icontains = search_term)
        message = f'{search_term}'
        context = {
            'message': message,
            'results': results
        }
        
    return render(request, 'search.html', context)