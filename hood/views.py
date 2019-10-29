from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html', locals())

def post(request):
    return render(request, 'post.html', locals())
